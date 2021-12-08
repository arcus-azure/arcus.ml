<!-- markdownlint-disable -->

<a href="../../../arcus/ml/timeseries/timeops.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ml.timeseries.timeops`
The timeops module provides interesting standard functionality for timeseries datasets 


---

<a href="../../../arcus/ml/timeseries/timeops.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `set_timeseries`

```python
set_timeseries(df: DataFrame, time_column: str) → DataFrame
```

Transforms the dataframe to a timeseries enabled dataframe by applying a DateTimeIndex to the given column 



**Args:**
 
 - <b>`df`</b> (pd.DataFrame):  The DataFrame that should be time-indexed 



**Returns:**
 
 - <b>`pd.DataFrame`</b>:  The DataFrame, including the DatetimeIndex 


---

<a href="../../../arcus/ml/timeseries/timeops.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_time_reference`

```python
add_time_reference(
    sorted_df: DataFrame,
    n: int,
    reference_column: str,
    new_column: str
) → DataFrame
```

This method will add a reference column to the DataFrame that points to n items before 

**Args:**
 
 - <b>`sorted_df`</b> (pd.DataFrame):  a DataFrame that is sorted by the time 
 - <b>`n`</b> (int):  the number of records to look back for the referencing columns 
 - <b>`new_column`</b> (str):  the name of the new column 

**Returns:**
 
 - <b>`(pd.DataFrame)`</b>:  the dataframe with the new column created 


---

<a href="../../../arcus/ml/timeseries/timeops.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `time_slice`

```python
time_slice(
    df: DataFrame,
    time_column: str,
    start: datetime = None,
    end: datetime = None
)
```

This method takes a time series DataFrame and only returns the time slice, based on the start & end date 

**Args:**
 
 - <b>`df`</b> (pd.DataFrame):  The indexed Data Frame , which should be a DatetimeIndex 
 - <b>`start`</b> (datetime):  The start time of the time slice.  When skipped, the time slice begins at the beginning of the index 
 - <b>`end`</b> (datetime):  The end time of the time slice.  When skipped, the time slice end at the end of the index 

**Returns:**
 
 - <b>`(pd.DataFrame)`</b>:  the dataframe only containing the records inside the time slice 


---

<a href="../../../arcus/ml/timeseries/timeops.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_windows`

```python
get_windows(
    sorted_df: DataFrame,
    window_size: int,
    window_stride: int = 1,
    group_column: str = None,
    zero_padding: bool = False,
    remove_group_column: bool = False,
    target_column: str = None
) → <built-in function array>
```






---

<a href="../../../arcus/ml/timeseries/timeops.py#L119"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `combine_time_ranges`

```python
combine_time_ranges(*args: DataFrame)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
