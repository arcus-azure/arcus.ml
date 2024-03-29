'''
The timeops module provides helpful functionality for timeseries datasets
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
    This method will add a reference column to the DataFrame that contains the value of reference column of n items before

    Args:
        sorted_df (pd.DataFrame): a DataFrame that is sorted by the time
        n (int): the number of records to look back for the referencing columns
        new_column (str): the name of the new column

    Returns:
        pd.DataFrame: the dataframe with the new column created
    '''
    sorted_df[new_column] = sorted_df[reference_column].shift(n)

def time_slice(df: pd.DataFrame, time_column:str, start: datetime.datetime = None, end: datetime.datetime = None):
    '''
    This method takes a time series DataFrame and only returns the time slice, based on the start & end date

    Args:
        df (pd.DataFrame): The indexed Data Frame , which should be a DatetimeIndex
        start (datetime): The start time of the time slice.  When skipped, the time slice begins at the beginning of the index
        end (datetime): The end time of the time slice.  When skipped, the time slice end at the end of the index
    
    Returns:
        pd.DataFrame: the dataframe only containing the records inside the time slice
    '''
    if(df.index is None or type(df.index) != pd.DatetimeIndex):
        df = set_timeseries(df, time_column)
    df = df.sort_index()
    return df.loc[start:end]

def get_windows(sorted_df: pd.DataFrame, 
                window_size: int, 
                window_stride: int = 1, 
                group_column: str = None, 
                zero_padding: bool = False, 
                remove_group_column: bool = False, 
                target_column: str = None) -> np.array:
    '''
    This method take a DataFrame and returns a set of time windows of a specific length and a given column, eventually grouped by another column

    Args:
        sorted_df (pd.DataFrame): A sorted Data Frame by a DatetimeIndex, that contains all time values
        window_size (int): The size of a window.  How much record values should be added in every window.  Consider this as a slice of the time series.
        window_stride (int): How much records should be between the different windows?  (Default: 1)
        group_column (str): The name of the column on which you should group the time windows.  This could be something like device_id.  Optional.
        zero_padding (bool): If True, zeros will be added in the first time windows, to fill the array, prior to the first values.
        remove_group_column (bool): Indicates if the actual group column should be removed from the destination data frame
        target_column (str): Used to return a related array of values, taking from the column with this name.  Commonly used to specify classes in training sets.
    
    Returns: a tuple with the following objects:
        np.array: A multi dimensional array with all the windows, eventuall grouped
        np.array: An array, with all the linked target values
    '''

    if window_size <= 0: 
        raise ValueError('Requires a positive (> 0 ) window_size for getting time windows of a data frame')
    if group_column is not None and group_column not in sorted_df.columns:
        raise ValueError('Requires a group_column when getting grouped time windows that is presnet in the data frame')
    if target_column is not None and target_column not in sorted_df.columns:
        raise ValueError('Requires a target_column when getting targeted windows that is present in the data frame ' + target_column)

    if group_column is None:
        return __get_windows_from_group(sorted_df, window_size, window_stride, zero_padding, target_column)

    else:
        windows = None
        targets = None
        
        _unique_groups = sorted_df[group_column].unique()

        for key in _unique_groups:
            _group_df = sorted_df[:][sorted_df[group_column] == key]
            if remove_group_column:
                _group_df.drop(group_column, axis=1, inplace=True)
            
            _current_windows, _current_targets = __get_windows_from_group(
                _group_df, window_size, window_stride, zero_padding, target_column)
            
            if windows is None:
                windows = _current_windows
            else:
                windows = np.concatenate((windows, _current_windows))

            if target_column is not None:
                if targets is None:
                    targets = _current_targets
                else:
                    targets = np.concatenate((targets, _current_targets))

        return windows, targets

def __get_windows_from_group(sorted_df: pd.DataFrame, window_size: int, 
                             window_stride: int = 1, zero_padding: bool = False,
                             target_column:str = None) -> np.array:
    # zero based row to take the leading window from - this row will be last row in the window
    _start_row_idx = 0 if zero_padding else window_size - 1
    _row_count = len(sorted_df)

    windows = list()
    targets = list()
    
    for _current_row_idx in range(_start_row_idx, _row_count):
        _slice_begin_idx = (_current_row_idx - window_size + 1) if _current_row_idx >= window_size else 0
        
        window_df = sorted_df.copy()

        time_slice = window_df.iloc[_slice_begin_idx:_current_row_idx + 1, :]
        time_array = np.array(time_slice.values)
        
        if zero_padding:
            _rows_to_pad = window_size - _current_row_idx - 1
            if _rows_to_pad > 0:
                padding_matrix = np.zeros((_rows_to_pad, len(sorted_df.columns)))
                time_array = np.concatenate((padding_matrix, time_array))
        
        if target_column is not None:
            _target_colidx = sorted_df.columns.get_loc(target_column)
            time_array, target_array = __pop_from_array(time_array, _target_colidx)
            targets.append(target_array)

        windows.append(time_array)
    
    print(len(targets))
    return np.array(windows), np.array(targets) if target_column is not None else None

def __pop_from_array(my_array, pc):
    i = pc
    pop = my_array[:, i]
    new_array = np.hstack((my_array[:, :i], my_array[:, i+1:]))
    return new_array, pop


def combine_time_ranges(*args: pd.DataFrame):
    '''
    This method combines multiple timeseries (as DataFrame) and removes the overlapping time sections

    Args:
        *args (pd.DataFrame): A list of DataFrames, containing time series and the same layout.
    
    Returns: 
        pd.DataFrame: A DataFrame, containing all unique, ordered time series data from the given DataFrames
    '''
    _result_df = pd.concat(args)
    _result_df = _result_df.drop_duplicates()
    return _result_df