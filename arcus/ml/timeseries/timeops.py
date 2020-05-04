'''
The timeops module provides interesting standard functionality for timeseries datasets
'''

import pandas as pd
import math
import numpy as np

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