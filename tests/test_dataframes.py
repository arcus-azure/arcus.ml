import sys
import os
import pytest
import pandas as pd 
import arcus.ml.dataframes as adf
import logging

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()

# initialize list of lists 
categorical_data = [['BE', 10], ['FR', 15], ['BE', 14], ['UK', 14], ['SE', 14], ['SE', 14]] 


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

def test_one_hot_encoding_default():
    # Create the pandas DataFrame 
    test_df = pd.DataFrame(categorical_data, columns = ['Country', 'Infected']) 

    # One hot encode the Country column
    encoded_df = adf.one_hot_encode(test_df, 'Country')
    assert len(encoded_df.columns) == 5
    assert 'Country_BE' in encoded_df.columns
    assert len(encoded_df.loc[encoded_df['Country_BE'] == 1]) == 2
    assert len(encoded_df.loc[encoded_df['Country_FR'] == 0]) == 5


def test_one_hot_encoding_keepcolumn():
    # Create the pandas DataFrame 
    test_df = pd.DataFrame(categorical_data, columns = ['Country', 'Infected']) 

    # One hot encode the Country column
    encoded_df = adf.one_hot_encode(test_df, 'Country', drop_column=False)
    assert len(encoded_df.columns) == 6
    assert 'Country_SE' in encoded_df.columns
    assert len(encoded_df.loc[encoded_df['Country_UK'] == 1]) == 1


def test_one_hot_encoding_prefix():
    # Create the pandas DataFrame 
    test_df = pd.DataFrame(categorical_data, columns = ['Country', 'Infected']) 
    encoded_df = adf.one_hot_encode(test_df, 'Country', prefix='cnt')

    # One hot encode the Country column
    assert len(encoded_df.columns) == 5
    assert 'cnt_BE' in encoded_df.columns
    assert len(encoded_df.loc[encoded_df['cnt_UK'] == 1]) == 1
