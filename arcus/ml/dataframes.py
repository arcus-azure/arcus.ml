'''
The dataframes module provides a lot of common operations for dataframe handling
'''

import pandas as pd

def shuffle(df: pd.DataFrame) -> pd.DataFrame:
    '''Shuffles the DataFrame and returns it

    Args:
        df (pd.DataFrame): The DataFrame that should have its records shuffled

    Returns: 
        pd.DataFrame: The DataFrame that is shuffled
    '''

    return df.sample(frac=1).reset_index(drop=True)

def one_hot_encode(df: pd.DataFrame, column_name: str, drop_column:bool = True, prefix: str = None):
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