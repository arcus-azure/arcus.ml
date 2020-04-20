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

