'''
The timeops module provides interesting standard functionality for timeseries datasets
'''

import pandas as pd
import math
import numpy as np
import datetime

def set_timeseries(df: pd.DataFrame, time_column:str) -> pd.DataFrame:
    '''
    Transforms the dataframe to a timeseries enabled dataframe
    by applying a DateTimeIndex to the given column

    Args:
        df (pd.DataFrame): The DataFrame that should be time-indexed
    
    Returns:
        pd.DataFrame: The DataFrame, including the DatetimeIndex
    '''
    df.index = pd.DatetimeIndex(df[time_column])
    pd.to_datetime(df[time_column], errors='coerce')
    return df

def add_time_reference(sorted_df: pd.DataFrame, n: int, reference_column: str, new_column: str) -> pd.DataFrame:
    '''
    This method will add a reference column to the DataFrame that points to n items before
    Args:
        sorted_df (pd.DataFrame): a DataFrame that is sorted by the time
        n (int): the number of records to look back for the referencing columns
        new_column (str): the name of the new column
    Returns:
        (pd.DataFrame): the dataframe with the new column created
    '''
    sorted_df[new_column] = sorted_df[reference_column].shift(n)

def time_slice(df: pd.DataFrame, time_column:str, start: datetime.datetime = None, end: datetime.datetime = None):
    if(df.index is not None and type(df.index) == pd.DatetimeIndex):
        return df.loc[start:end]
    return df