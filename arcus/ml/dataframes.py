'''
The dataframes module provides a lot of common operations for dataframe handling
'''

import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
from arcus.ml.timeseries import timeops

def shuffle(df: pd.DataFrame) -> pd.DataFrame:
    '''Shuffles the DataFrame and returns it

    Args:
        df (pd.DataFrame): The DataFrame that should have its records shuffled

    Returns: 
        pd.DataFrame: The DataFrame that is shuffled
    '''

    return df.sample(frac=1).reset_index(drop=True)

def one_hot_encode(df: pd.DataFrame, column_name: str, drop_column:bool = True, prefix: str = None) -> pd.DataFrame:
    '''Take a categorical column and pivots the DataFrame to add columns (0 or 1 value) for every category

    Args:
        df (pd.DataFrame): The DataFrame that contains the column to be encoded
        column_name (str): The name of the column that contains the categorical values
        drop_column (bool): Will remove the original column from the dataframe
        prefix (str): The prefix of the new columns.  By default the original column name will be taken

    Returns: 
        pd.DataFrame: The DataFrame with the one hot encoded features
    '''
    # Apply logic for previx columns
    if prefix == None:
        prefix = column_name

    # Apply one hot encoding
    df = pd.concat(
        [df, pd.get_dummies(df[column_name], prefix=prefix)], axis=1)

    if(drop_column):
        df.drop([column_name], axis=1, inplace=True)

    return df

def keep_numeric_features(df: pd.DataFrame) -> pd.DataFrame:
    '''Takes the DataFrame and removes all non-numeric columns or features

    Args:
        df (pd.DataFrame): The DataFrame that should have its non-numerics removed

    Returns: 
        pd.DataFrame: The DataFrame with only the numeric features
    '''
    return df.select_dtypes(include=np.number)

def plot_features(df: pd.DataFrame, column_names: np.array = None, grid_shape = None, fig_size = None):
    '''Plots the distribution of the relevant columns of a DataFrame

    Args:
        df (pd.DataFrame): The DataFrame that should have its non-numerics removed
        column_names (np.array): The columns that should be plotted.  If None, all numeric columns will be taken
        grid_shape (int, int): The shape of the plotting grid (rows, cols).  If None, the grid will have maximum 5 columns
        fig_size (int, int): The size of the full plotting grid.  If None, auto size will be applied

    Returns: 
        figure, axes (tuple): The figure of the plot and the axes of the plot will be returned for further tuning where needed
    '''
    # Take column names of all numeric columns
    if(column_names==None):
        # Default to all numeric columns
        column_names = keep_numeric_features(df).columns

    # Define grid shape
    if (grid_shape==None):
        # We will use 5 plots side/side by default or less in case of less columns
        grid_width = min(5, len(column_names))
        # Checking how much rows we need 
        grid_height = math.ceil(len(column_names) / grid_width) 
    else:
        grid_height, grid_width = grid_shape

    f, axes = plt.subplots(grid_height, grid_width, figsize=fig_size, sharex=False)

    _it = 0
    for col in column_names:
        _row = math.floor(_it / grid_width)
        _col = _it % grid_width
        try:
            sns.distplot(df[col], color='skyblue', ax= axes.ravel()[_it], label=col)
        except Exception as e:
            print('Exception in printing column', col, ':', _row, _col, e)
        _it += 1
    
    return f, axes

def to_timeseries(df: pd.DataFrame, time_column:str) -> pd.DataFrame:
    '''
    This is deprecated and it is advised to use the timeseries.set_timeseries function for this
    '''
    return timeops.set_timeseries(df, time_column)

def distribute_class(df: pd.DataFrame, class_column: str, class_size:int = None, shuffle_result: bool = True):
    '''
    Makes sure a DataFrame is returned with an equal class distribution
    For every class a number of samples will be taken
    The class size is defined by the minimum of the passed class_size parameter and the smallest class in the Dataframe

    Args:
        df (pd.DataFrame): the DataFrame that contains all records
        class_column (str): the name of the column that contains the class feature
        class_size (int): the size of the class.  defaults to the minimum available class size
        shuffle_result (bool): indicates the DataFrame should be shuffled before returning.  Default to True
    
    Returns:
        pd.DataFrame: the DataFrame that contains the records with the equal class distribution
    '''
    _class_distribution = Counter(df[class_column])
    if(class_size is None):
        class_size = min(_class_distribution.values())
    else:
        class_size = min(min(_class_distribution.values()), class_size)

    _result_df = None
    for _class in _class_distribution.keys():
        _df_add = df[df[class_column] == _class].sample(class_size)
        if(_result_df is None):
            _result_df = _df_add.copy()
        else:
            _result_df = _result_df.append(_df_add)

    if(shuffle_result):
        _result_df = shuffle(_result_df)
    return _result_df