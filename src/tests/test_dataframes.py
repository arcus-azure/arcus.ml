import sys
import os
import pytest
import pandas as pd 
import arcus.ml.dataframes as adf
import logging

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()

def setup_module(module):
    ''' Setup for the entire module '''
    # Do the actual setup stuff here
    pass

def setup_function(func):
    ''' Setup for test functions '''


def test_shuffle():
    # initialize list of lists 
    data = [['tom', 10], ['nick', 15], ['juli', 14]] 
    
    # Create the pandas DataFrame 
    test_df = pd.DataFrame(data, columns = ['Name', 'Age']) 
    
    # print dataframe. 
    shuffled_df = adf.shuffle(test_df)
    assert len(shuffled_df)==len(test_df)
    assert shuffled_df[shuffled_df.Name == 'nick'].iloc[0].Age == 15