import sys
import os
import pytest
import pandas as pd 
import arcus.ml.timeseries.timeops as tops
import arcus.ml.dataframes as adf
import logging
from unittest.mock import patch 
from datetime import datetime

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