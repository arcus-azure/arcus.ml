<!-- markdownlint-disable -->

<a href="../../../arcus/ml/timeseries/timeops.py#L0"><img align="right"  src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `ml.timeseries.timeops`
The timeops module provides helpful functionality for timeseries datasets 


---

<a href="../../../arcus/ml/timeseries/timeops.py#L10"><img align="right"  src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

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

<a href="../../../arcus/ml/timeseries/timeops.py#L25"><img align="right"  src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `add_time_reference`

```python
add_time_reference(
    sorted_df: DataFrame,
    n: int,
    reference_column: str,
    new_column: str
) → DataFrame
```

This method will add a reference column to the DataFrame that contains the value of reference column of n items before 



**Args:**
 
 - <b>`sorted_df`</b> (pd.DataFrame):  a DataFrame that is sorted by the time 
 - <b>`n`</b> (int):  the number of records to look back for the referencing columns 
 - <b>`new_column`</b> (str):  the name of the new column 



**Returns:**
 
 - <b>`pd.DataFrame`</b>:  the dataframe with the new column created 


---

<a href="../../../arcus/ml/timeseries/timeops.py#L39"><img align="right"  src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

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
 
 - <b>`pd.DataFrame`</b>:  the dataframe only containing the records inside the time slice 


---

<a href="../../../arcus/ml/timeseries/timeops.py#L56"><img align="right"  src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

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

This method take a DataFrame and returns a set of time windows of a specific length and a given column, eventually grouped by another column 



**Args:**
 
 - <b>`sorted_df`</b> (pd.DataFrame):  A sorted Data Frame by a DatetimeIndex, that contains all time values 
 - <b>`window_size`</b> (int):  The size of a window.  How much record values should be added in every window.  Consider this as a slice of the time series. 
 - <b>`window_stride`</b> (int):  How much records should be between the different windows?  (Default: 1) 
 - <b>`group_column`</b> (str):  The name of the column on which you should group the time windows.  This could be something like device_id.  Optional. 
 - <b>`zero_padding`</b> (bool):  If True, zeros will be added in the first time windows, to fill the array, prior to the first values. 
 - <b>`remove_group_column`</b> (bool):  Indicates if the actual group column should be removed from the destination data frame 
 - <b>`target_column`</b> (str):  Used to return a related array of values, taking from the column with this name.  Commonly used to specify classes in training sets. 

Returns: a tuple with the following objects: 
 - <b>`np.array`</b>:  A multi dimensional array with all the windows, eventuall grouped 
 - <b>`np.array`</b>:  An array, with all the linked target values 


---

<a href="../../../arcus/ml/timeseries/timeops.py#L159"><img align="right"  src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `combine_time_ranges`

```python
combine_time_ranges(*args: DataFrame)
```

This method combines multiple timeseries (as DataFrame) and removes the overlapping time sections 



**Args:**
 
 - <b>`*args (pd.DataFrame)`</b>:  A list of DataFrames, containing time series and the same layout. 



**Returns:**
 
 - <b>`pd.DataFrame`</b>:  A DataFrame, containing all unique, ordered time series data from the given DataFrames 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
