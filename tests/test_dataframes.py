import sys
import os
import pytest
import pandas as pd 
import arcus.ml.dataframes as adf
import logging
from unittest.mock import patch 
from collections import Counter

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


@patch("matplotlib.pyplot.show")
def test_one_hot_encoding_prefix(mock_show):
    # Create the pandas DataFrame 
    test_df = pd.DataFrame(categorical_data, columns = ['Country', 'Infected']) 
    encoded_df = adf.one_hot_encode(test_df, 'Country', prefix='cnt')

    # One hot encode the Country column
    assert len(encoded_df.columns) == 5
    assert 'cnt_BE' in encoded_df.columns
    assert len(encoded_df.loc[encoded_df['cnt_UK'] == 1]) == 1

@patch("matplotlib.pyplot.show")
def test_plot_features_selectedcols(mock_show):
    df = pd.read_csv('tests/resources/datasets/car-fuel.csv')
    _, _axes = adf.plot_features(df, column_names=['speed', 'temp_outside'])
    assert len(_axes.ravel()) == 2
    _ax = _axes[0]
    assert _ax.numCols == 2
    assert _ax.numRows == 1

@patch("matplotlib.pyplot.show")
def test_plot_features_onerow(mock_show):
    df = pd.read_csv('tests/resources/datasets/car-fuel.csv')
    _, _axes = adf.plot_features(df, column_names=['speed', 'temp_outside'])
    assert len(_axes.ravel()) == 2
    _ax = _axes[0]
    assert _ax.numCols == 2
    assert _ax.numRows == 1

@patch("matplotlib.pyplot.show")
def test_plot_features_grid_size(mock_show):
    df = pd.read_csv('tests/resources/datasets/car-fuel.csv')
    _, _axes = adf.plot_features(df, grid_shape=(2,3))
    assert len(_axes.ravel()) == 6
    _ax = _axes[0][0]
    assert _ax.numCols == 3
    assert _ax.numRows == 2

@patch("matplotlib.pyplot.show")
def test_plot_features_default(mock_show):
    df = pd.read_csv('tests/resources/datasets/car-fuel.csv')
    _, _axes = adf.plot_features(df)
    assert len(_axes.ravel()) == 5
    assert _axes[0].numCols == 5
    assert _axes[0].numRows == 1

def test_keep_numeric_features():
    test_df = pd.DataFrame(categorical_data, columns = ['Country', 'Infected']) 
    num_df = adf.keep_numeric_features(test_df)
    assert len(num_df.columns) == 1

def test_keep_numeric_features_onehotencoded():
    test_df = pd.DataFrame(categorical_data, columns = ['Country', 'Infected'])
    encoded_df = adf.one_hot_encode(test_df, 'Country', prefix='cnt') 
    num_df = adf.keep_numeric_features(encoded_df)
    assert len(num_df.columns) == 5

def test_keep_numeric_features_csv():
    df = pd.read_csv('tests/resources/datasets/car-fuel.csv')
    num_df = adf.keep_numeric_features(df)
    assert len(num_df.columns) == 5

def test_class_distribution_default():
    df = pd.read_csv('tests/resources/datasets/car-fuel.csv')
    cnt1 = Counter(df.gas_type)
    df = adf.distribute_class(df, 'gas_type')
    cnt2 = Counter(df.gas_type)
    # Smallest class size from first should be same as largest from new
    assert min(cnt1.values()) == max (cnt2.values())
    # Sizes of new df should be the same
    assert min(cnt2.values()) == max (cnt2.values())
    assert len(df) == min(cnt1.values()) * 2

def test_class_distribution_class_size():
    cs = 30
    df = pd.read_csv('tests/resources/datasets/car-fuel.csv')
    cnt1 = Counter(df.gas_type)
    df = adf.distribute_class(df, 'gas_type', cs)
    cnt2 = Counter(df.gas_type)
    # Sizes of new df should be the same
    assert min(cnt2.values()) == max (cnt2.values())
    assert len(df) == cs * 2

def test_class_distribution_noshuffle():
    cs = 30
    df = pd.read_csv('tests/resources/datasets/car-fuel.csv')
    cnt1 = Counter(df.gas_type)
    df = adf.distribute_class(df, 'gas_type', cs, False)
    cnt2 = Counter(df.iloc[0:cs].gas_type)
    assert len(cnt2.keys()) == 1