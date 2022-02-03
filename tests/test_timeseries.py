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
from hypothesis import given, strategies as st, assume
from hypothesis.extra.pandas import data_frames, columns

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

class WinGroup():
    def __init__(self, column_name, strategy):
        self.column_name = column_name
        self.strategy = strategy
    def assign(self, draw, df):
        df[self.column_name] = draw(self.strategy)

@st.composite
def tables(draw, win_group = None):
    colls_length = draw(st.integers(min_value=1, max_value=10))
    colls_names = ["engine_id", "cycle", "setting1", "setting2", "sensor4", "seonsor4", "sensor10"]
    colls = draw(st.lists(st.sampled_from(colls_names), min_size=colls_length, max_size=colls_length))
    df = draw(data_frames(columns=columns(colls_names, dtype=float, elements=st.floats(allow_nan=False))))
    if win_group is not None:
        win_group.assign(draw, df)
    assume(len(df) > 1)
    return df

def get_random_window_size_within(df, data):
    return data.draw(st.integers(min_value=1, max_value=len(df)))

@given(tables(), st.data())
def test_time_windows_default_property(df, data):
    win_size = get_random_window_size_within(df, data)
    windows, _ = tops.get_windows(df, win_size)
    assert_all_windows_equals(df, windows, win_size)

def test_time_windows_default_example():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    assert len(df)==20  
    assert df.shape == (20, 27)  
    win_size = 6
    col_size = len(df.columns)
    windows, _ = tops.get_windows(df, win_size)
    assert windows.shape == (15, win_size, col_size)
    assert_all_windows_equals(df, windows, win_size)

@given(tables(), st.integers(max_value=0))
def test_time_windows_negative_windows_size_fails(df, win_size):
    with pytest.raises(ValueError, match=r'.* window_size .*'):
        tops.get_windows(df, win_size)

def test_time_windows_targets_example():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    assert len(df)==20  
    assert df.shape == (20, 27)  
    win_size = 6
    col_size = len(df.columns)
    windows, targets = tops.get_windows(df, win_size, target_column='ttf')
    assert windows.shape == (15, win_size, col_size - 1)
    assert targets.shape == (15, win_size)
    assert_all_windows_equals(df.drop('ttf', axis=1), windows, win_size)
    assert_all_windows_equals(df['ttf'], targets, win_size)

@given(tables(), st.data())
def test_time_windows_targets_property(df : pd.DataFrame, data):
    win_size = get_random_window_size_within(df, data)
    target_column_example = data.draw(st.sampled_from(list(df.columns)))
    windows, targets = tops.get_windows(df, win_size, target_column=target_column_example)
    assert_all_windows_equals(df.drop(target_column_example, axis=1), windows, win_size)
    assert_all_windows_equals(df[target_column_example], targets, win_size)

@given(tables(), st.data())
def test_time_windows_nonpresent_targets_property(df, data):
    win_size = get_random_window_size_within(df, data)
    with pytest.raises(ValueError, match=r'.* target_column .*'):
        tops.get_windows(df, win_size, target_column='non_present_column')

def test_time_windows_group_targets_example():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    assert len(df)==20  
    assert df.shape == (20, 27)  
    win_size = 6
    col_size = len(df.columns)
    windows, targets = tops.get_windows(df, win_size, group_column='engine_id', remove_group_column=True, target_column='ttf')
    assert windows.shape == (10, win_size, col_size - 2)
    assert targets.shape == (10, win_size)
    assert_all_windows_equals_with_group_targets(df, windows, targets, win_size, group_column='engine_id', target_column='ttf')

group_column_example = 'device_id'
@given(tables(win_group=WinGroup(group_column_example, st.sampled_from([0, 1]))), st.data())
def test_time_windows_group_targets_property(df, data):
    win_size = get_random_window_size_within(df, data)
    target_column_example = data.draw(st.sampled_from(list(df.columns[df.columns != group_column_example])))
    windows, targets = tops.get_windows(df, win_size, group_column=group_column_example, remove_group_column=True, target_column=target_column_example)
    assert_all_windows_equals_with_group_targets(df, windows, targets, win_size, group_column_example, target_column_example)

def test_time_windows_padding_example():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    assert len(df)==20  
    assert df.shape == (20, 27)  
    win_size = 6
    col_size = len(df.columns)
    windows, _ = tops.get_windows(df, win_size, zero_padding=True)
    assert windows.shape == (20, win_size, col_size)
    assert_all_windows_equals_with_padding(df, windows, win_size)

@given(tables(), st.data())
def test_time_windows_padding_property(df, data):
    win_size = get_random_window_size_within(df, data)
    windows, _ = tops.get_windows(df, win_size, zero_padding=True)
    assert_all_windows_equals_with_padding(df, windows, win_size)

def test_time_windows_group_example():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    win_size = 6
    col_size = len(df.columns)
    windows, _ = tops.get_windows(df, win_size, group_column='engine_id')
    assert windows.shape == (10, win_size, col_size)
    assert_all_windows_equals_with_grouping(df, windows, win_size, 'engine_id')

@given(tables(win_group=WinGroup(group_column_example, st.sampled_from([0, 1]))), st.data())
def test_time_windows_group_property(df, data):
    win_size = get_random_window_size_within(df, data)
    windows, _ = tops.get_windows(df, win_size, group_column=group_column_example)
    assert_all_windows_equals_with_grouping(df, windows, win_size, group_column_example)

@given(tables(win_group=WinGroup(group_column_example, st.just(0))), st.data())
def test_time_windows_single_group_property(df, data):
    win_size = get_random_window_size_within(df, data)
    windows_group, _ = tops.get_windows(df, win_size, group_column=group_column_example)
    windows, _ = tops.get_windows(df, win_size)
    assert_sequence_equals(windows_group, windows)

@given(tables(), st.data())
def test_time_windows_nonpresent_group_property(df, data):
    win_size = get_random_window_size_within(df, data)
    with pytest.raises(ValueError, match=r'.* group_column .*'):
        tops.get_windows(df, win_size, group_column='non_exist_column')

def test_time_windows_group_padding_example():
    df = pd.read_csv('tests/resources/datasets/engine-sensors.csv')
    win_size = 6
    col_size = len(df.columns)
    windows, _ = tops.get_windows(df, win_size, group_column='engine_id', zero_padding=True)
    assert windows.shape == (20, win_size, col_size)
    assert_all_windows_equals_with_padding_grouping(df, windows, win_size, 'engine_id')

@given(tables(win_group=WinGroup(group_column_example, st.sampled_from([0, 1]))), st.data())
def test_time_windows_group_padding_property(df, data):
    win_size = get_random_window_size_within(df, data)
    windows, _ = tops.get_windows(df, win_size, group_column=group_column_example, zero_padding=True)
    assert_all_windows_equals_with_padding_grouping(df, windows, win_size, group_column_example)

def assert_all_windows_equals(df, windows, win_size):
    expected_windows = list()
    add_windows(expected_windows, df, win_size)
    assert_sequence_equals(expected_windows, windows)

def assert_all_windows_equals_with_padding(df, windows, win_size):
    expected_windows = list()
    add_padding_windows(expected_windows, df, win_size)
    add_windows(expected_windows, df, win_size)
    assert_sequence_equals(expected_windows, windows)

def add_padding_windows(expected_windows, df, win_size):
    for win_index in range(1, win_size):
        expected_values = df[0:win_index].values
        padding = np.zeros((win_size - win_index, len(df.columns)))
        expected_window = np.concatenate((padding, expected_values))
        expected_windows.append(expected_window)

def assert_all_windows_equals_with_grouping(df, windows, win_size, group_column):
    expected_windows = list()
    for name, group in df.groupby(group_column):
        add_windows(expected_windows, group, win_size)
    assert_sequence_equals(expected_windows, windows)

def assert_all_windows_equals_with_padding_grouping(df, windows, win_size, group_column):
    expected_windows = list()
    for name, group in df.groupby(group_column):
        add_padding_windows(expected_windows, group, win_size)
        add_windows(expected_windows, group, win_size)
    assert_sequence_equals(expected_windows, windows)

def assert_all_windows_equals_with_group_targets(df, windows, targets, win_size, group_column, target_column):
    expected_windows = list()
    expected_targets = list()
    for name, group in df.groupby(group_column):
        add_windows(expected_windows, group.drop([group_column, target_column], axis=1), win_size)
        add_windows(expected_targets, group[target_column], win_size)
    assert_sequence_equals(expected_windows, windows)
    assert_sequence_equals(expected_targets, targets)

def add_windows(expected_windows, df, win_size):
    for win_index in range(win_size, len(df) + 1):
        index = win_index - win_size
        expected_window = df[index:win_index].values
        expected_windows.append(expected_window)

def assert_sequence_equals(expected_seq, actual_seq):
    assert len(expected_seq) == len(actual_seq)
    for i in range(0, len(expected_seq)):
        expected = expected_seq[i]
        actual = actual_seq[i]
        assert np.equal(expected, actual).all()