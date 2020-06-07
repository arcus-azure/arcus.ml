import sys
import os
import pytest
import pandas as pd 
import arcus.ml.timeseries.timeops as tops
import arcus.ml.dataframes as adf
import logging
from unittest.mock import patch 
from datetime import datetime
import numpy as np 

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()

time_series_df = pd.read_csv('tests/resources/datasets/sunspots.csv')

def test_time_slice_default_str():
    df = time_series_df.copy()
    slice_df = tops.time_slice(df, 'Date')
    assert slice_df.shape == (30, 3)
    #df = tops.time_slice(df, '')

def test_time_slice_start_str():
    df = time_series_df.copy()
    slice_df = tops.time_slice(df, 'Date', start='01/02/2001')
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', start='01/01/2018')
    assert slice_df.shape == (5, 3)

def test_time_slice_end_str():
    df = time_series_df.copy()
    slice_df = tops.time_slice(df, 'Date', end='01/02/2020')
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', end='01/01/2017')
    assert slice_df.shape == (13, 3)

def test_time_slice_both_str():
    df = time_series_df.copy()
    slice_df = tops.time_slice(df, 'Date', start = '01/01/2001', end='01/02/2020')
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', start='01/01/2016', end='01/01/2017')
    assert slice_df.shape == (12, 3)


def test_time_slice_start_date():
    df = time_series_df.copy()
    slice_df = tops.time_slice(df, 'Date', start=datetime.strptime('01/02/2001', '%d/%m/%Y'))
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', start=datetime.strptime('01/01/2018', '%d/%m/%Y'))
    assert slice_df.shape == (5, 3)

def test_time_slice_end_date():
    df = time_series_df.copy()
    slice_df = tops.time_slice(df, 'Date', end=datetime.strptime('01/02/2020', '%d/%m/%Y'))
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', end=datetime.strptime('01/01/2017', '%d/%m/%Y'))
    assert slice_df.shape == (13, 3)

def test_time_slice_both_date():
    df = time_series_df.copy()
    slice_df = tops.time_slice(df, 'Date', start=datetime.strptime('01/01/2001', '%d/%m/%Y'), end=datetime.strptime('01/02/2020', '%d/%m/%Y'))
    assert slice_df.shape == (30, 3)
    slice_df = tops.time_slice(df, 'Date', start=datetime.strptime('01/01/2016', '%d/%m/%Y'), end=datetime.strptime('01/01/2017', '%d/%m/%Y'))
    assert slice_df.shape == (12, 3)

def test_add_timerange():
    range01 = pd.date_range('2018-03-01', periods=6, freq='1M')
    df01 = pd.DataFrame({'A': np.ones(6), 'Timestamp': range01})
    range02 = pd.date_range('2018-01-01', periods=6, freq='1M')
    df02 = pd.DataFrame({'A': np.ones(6), 'Timestamp': range02})
    range03 = pd.date_range('2018-05-01', periods=6, freq='1M')
    df03 = pd.DataFrame({'A': np.ones(6), 'Timestamp': range03})

    full_range = tops.combine_time_ranges(df01, df02, df03)
    assert len(full_range) == 10

def test_add_empty_df_timerange():
    df00 = None
    range01 = pd.date_range('2018-03-01', periods=6, freq='1M')
    df01 = pd.DataFrame({'A': np.ones(6), 'Timestamp': range01})

    full_range = tops.combine_time_ranges(df00, df01)
    assert len(full_range) == 6