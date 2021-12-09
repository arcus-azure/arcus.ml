# ml.timeseries package

## Submodules

## ml.timeseries.timeops module

The timeops module provides helpful functionality for timeseries datasets


### ml.timeseries.timeops.add_time_reference(sorted_df: pandas.core.frame.DataFrame, n: int, reference_column: str, new_column: str)
This method will add a reference column to the DataFrame that contains the value of reference column of n items before


* **Parameters**

    
    * **sorted_df** (*pd.DataFrame*) – a DataFrame that is sorted by the time


    * **n** (*int*) – the number of records to look back for the referencing columns


    * **new_column** (*str*) – the name of the new column



* **Returns**

    the dataframe with the new column created



* **Return type**

    pd.DataFrame



### ml.timeseries.timeops.combine_time_ranges(\*args: pandas.core.frame.DataFrame)
This method combines multiple timeseries (as DataFrame) and removes the overlapping time sections


* **Parameters**

    **\*args** (*pd.DataFrame*) – A list of DataFrames, containing time series and the same layout.



* **Returns**

    A DataFrame, containing all unique, ordered time series data from the given DataFrames



* **Return type**

    pd.DataFrame



### ml.timeseries.timeops.get_windows(sorted_df: pandas.core.frame.DataFrame, window_size: int, window_stride: int = 1, group_column: Optional[str] = None, zero_padding: bool = False, remove_group_column: bool = False, target_column: Optional[str] = None)
This method take a DataFrame and returns a set of time windows of a specific length and a given column, eventually grouped by another column


* **Parameters**

    
    * **sorted_df** (*pd.DataFrame*) – A sorted Data Frame by a DatetimeIndex, that contains all time values


    * **window_size** (*int*) – The size of a window.  How much record values should be added in every window.  Consider this as a slice of the time series.


    * **window_stride** (*int*) – How much records should be between the different windows?  (Default: 1)


    * **group_column** (*str*) – The name of the column on which you should group the time windows.  This could be something like device_id.  Optional.


    * **zero_padding** (*bool*) – If True, zeros will be added in the first time windows, to fill the array, prior to the first values.


    * **remove_group_column** (*bool*) – Indicates if the actual group column should be removed from the destination data frame


    * **target_column** (*str*) – Used to return a related array of values, taking from the column with this name.  Commonly used to specify classes in training sets.


Returns: a tuple with the following objects:

    np.array: A multi dimensional array with all the windows, eventuall grouped
    np.array: An array, with all the linked target values


### ml.timeseries.timeops.set_timeseries(df: pandas.core.frame.DataFrame, time_column: str)
Transforms the dataframe to a timeseries enabled dataframe
by applying a DateTimeIndex to the given column


* **Parameters**

    **df** (*pd.DataFrame*) – The DataFrame that should be time-indexed



* **Returns**

    The DataFrame, including the DatetimeIndex



* **Return type**

    pd.DataFrame



### ml.timeseries.timeops.time_slice(df: pandas.core.frame.DataFrame, time_column: str, start: Optional[datetime.datetime] = None, end: Optional[datetime.datetime] = None)
This method takes a time series DataFrame and only returns the time slice, based on the start & end date


* **Parameters**

    
    * **df** (*pd.DataFrame*) – The indexed Data Frame , which should be a DatetimeIndex


    * **start** (*datetime*) – The start time of the time slice.  When skipped, the time slice begins at the beginning of the index


    * **end** (*datetime*) – The end time of the time slice.  When skipped, the time slice end at the end of the index



* **Returns**

    the dataframe only containing the records inside the time slice



* **Return type**

    pd.DataFrame


## Module contents
