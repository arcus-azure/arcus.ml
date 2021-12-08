<!-- markdownlint-disable -->

<a href="../../../arcus/ml/dataframes.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ml.dataframes`
The dataframes module provides a lot of common operations for dataframe handling 


---

<a href="../../../arcus/ml/dataframes.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `shuffle`

```python
shuffle(df: DataFrame) → DataFrame
```

Shuffles the DataFrame and returns it 



**Args:**
 
 - <b>`df`</b> (pd.DataFrame):  The DataFrame that should have its records shuffled 



**Returns:**
 
 - <b>`pd.DataFrame`</b>:  The DataFrame that is shuffled 


---

<a href="../../../arcus/ml/dataframes.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `one_hot_encode`

```python
one_hot_encode(
    df: DataFrame,
    column_name: str,
    drop_column: bool = True,
    prefix: str = None
) → DataFrame
```

Take a categorical column and pivots the DataFrame to add columns (0 or 1 value) for every category 



**Args:**
 
 - <b>`df`</b> (pd.DataFrame):  The DataFrame that contains the column to be encoded 
 - <b>`column_name`</b> (str):  The name of the column that contains the categorical values 
 - <b>`drop_column`</b> (bool):  Will remove the original column from the dataframe 
 - <b>`prefix`</b> (str):  The prefix of the new columns.  By default the original column name will be taken 



**Returns:**
 
 - <b>`pd.DataFrame`</b>:  The DataFrame with the one hot encoded features 


---

<a href="../../../arcus/ml/dataframes.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `keep_numeric_features`

```python
keep_numeric_features(df: DataFrame) → DataFrame
```

Takes the DataFrame and removes all non-numeric columns or features 



**Args:**
 
 - <b>`df`</b> (pd.DataFrame):  The DataFrame that should have its non-numerics removed 



**Returns:**
 
 - <b>`pd.DataFrame`</b>:  The DataFrame with only the numeric features 


---

<a href="../../../arcus/ml/dataframes.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_features`

```python
plot_features(
    df: DataFrame,
    column_names: <built-in function array> = None,
    grid_shape=None,
    fig_size=None
)
```

Plots the distribution of the relevant columns of a DataFrame 



**Args:**
 
 - <b>`df`</b> (pd.DataFrame):  The DataFrame that should have its non-numerics removed 
 - <b>`column_names`</b> (np.array):  The columns that should be plotted.  If None, all numeric columns will be taken 
 - <b>`grid_shape`</b> (int, int):  The shape of the plotting grid (rows, cols).  If None, the grid will have maximum 5 columns 
 - <b>`fig_size`</b> (int, int):  The size of the full plotting grid.  If None, auto size will be applied 



**Returns:**
 
 - <b>`figure, axes (tuple)`</b>:  The figure of the plot and the axes of the plot will be returned for further tuning where needed 


---

<a href="../../../arcus/ml/dataframes.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_timeseries`

```python
to_timeseries(df: DataFrame, time_column: str) → DataFrame
```

This is deprecated and it is advised to use the timeseries.set_timeseries function for this 


---

<a href="../../../arcus/ml/dataframes.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `distribute_class`

```python
distribute_class(
    df: DataFrame,
    class_column: str,
    class_size: int = None,
    shuffle_result: bool = True
)
```

Makes sure a DataFrame is returned with an equal class distribution For every class a number of samples will be taken The class size is defined by the minimum of the passed class_size parameter and the smallest class in the Dataframe 



**Args:**
 
 - <b>`df`</b> (pd.DataFrame):  the DataFrame that contains all records 
 - <b>`class_column`</b> (str):  the name of the column that contains the class feature 
 - <b>`class_size`</b> (int):  the size of the class.  defaults to the minimum available class size 
 - <b>`shuffle_result`</b> (bool):  indicates the DataFrame should be shuffled before returning.  Default to True 



**Returns:**
 
 - <b>`pd.DataFrame`</b>:  the DataFrame that contains the records with the equal class distribution 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
