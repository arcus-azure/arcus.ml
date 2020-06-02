import sys
import os
import pytest
import pandas as pd 
import arcus.ml.timeseries.timeops as tops
import arcus.ml.dataframes as adf
import logging
from unittest.mock import patch 

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()

time_series_df = pd.read_csv('tests/resources/datasets/sunspots.csv')

def test_time_slice_default():
    df = adf.to_timeseries( time_series_df, 'Date')
    slice_df = tops.time_slice(df, 'Date')
    assert slice_df.shape == (30, 3)
    #df = tops.time_slice(df, '')

def test_time_slice_start():
    df = adf.to_timeseries( time_series_df, 'Date')
    slice_df = tops.time_slice(df, 'Date', start='01/02/2001')
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', start='01/01/2018')
    assert slice_df.shape == (5, 3)

def test_time_slice_end():
    df = adf.to_timeseries( time_series_df, 'Date')
    slice_df = tops.time_slice(df, 'Date', end='01/02/2020')
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', end='01/01/2017')
    assert slice_df.shape == (13, 3)

def test_time_slice_both():
    df = adf.to_timeseries( time_series_df, 'Date')
    slice_df = tops.time_slice(df, 'Date', start = '01/01/2001', end='01/02/2020')
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', start='01/01/2016', end='01/01/2017')
    assert slice_df.shape == (12, 3)

def test_time_windows_default():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    assert len(df)==20  
    assert df.shape == (20, 27)  
    win_size = 6
    col_size = len(df.columns)
    windows, _ = tops.get_windows(df, win_size)
    assert windows.shape == (15, win_size, col_size)

def test_time_windows_targets():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    assert len(df)==20  
    assert df.shape == (20, 27)  
    win_size = 6
    col_size = len(df.columns)
    windows, targets = tops.get_windows(df, win_size, target_column='ttf')
    assert windows.shape == (15, win_size, col_size - 1)
    assert targets.shape == (15, win_size)

def test_time_windows_group_targets():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    assert len(df)==20  
    assert df.shape == (20, 27)  
    win_size = 6
    col_size = len(df.columns)
    windows, targets = tops.get_windows(df, win_size, group_column='engine_id', remove_group_column=True, target_column='ttf')
    assert windows.shape == (10, win_size, col_size - 2)
    assert targets.shape == (10, win_size)

def test_time_windows_padding():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    assert len(df)==20  
    assert df.shape == (20, 27)  
    win_size = 6
    col_size = len(df.columns)
    windows, _ = tops.get_windows(df, win_size, zero_padding=True)
    assert windows.shape == (20, win_size, col_size)

def test_time_windows_group():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    win_size = 6
    col_size = len(df.columns)
    windows, _ = tops.get_windows(df, win_size, group_column='engine_id')
    assert windows.shape == (10, win_size, col_size)

def test_time_windows_group_padding():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    win_size = 6
    col_size = len(df.columns)
    windows, _ = tops.get_windows(df, win_size, group_column='engine_id', zero_padding=True)
    assert windows.shape == (20, win_size, col_size)