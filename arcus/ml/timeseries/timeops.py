import pandas as pd
import math
import numpy as np

def add_time_reference(sorted_df: pd.DataFrame, n: int, reference_column: str, new_column: str) -> pd.DataFrame:
    sorted_df[new_column] = sorted_df[reference_column].shift(n)