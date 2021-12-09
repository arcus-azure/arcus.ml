# ml package

## Subpackages


* ml.evaluation package


    * Submodules


    * ml.evaluation.classification module


    * Module contents


* ml.images package


    * Submodules


    * ml.images.conversion module


    * ml.images.explorer module


    * ml.images.io module


    * Module contents


* ml.neuralnetworks package


    * Submodules


    * ml.neuralnetworks.keras module


    * Module contents


* ml.timeseries package


    * Submodules


    * ml.timeseries.timeops module


    * Module contents


## Submodules

## ml.dataframes module

The dataframes module provides a lot of common operations for dataframe handling


### ml.dataframes.distribute_class(df: pandas.core.frame.DataFrame, class_column: str, class_size: Optional[int] = None, shuffle_result: bool = True)
Makes sure a DataFrame is returned with an equal class distribution
For every class a number of samples will be taken
The class size is defined by the minimum of the passed class_size parameter and the smallest class in the Dataframe


* **Parameters**

    
    * **df** (*pd.DataFrame*) – the DataFrame that contains all records


    * **class_column** (*str*) – the name of the column that contains the class feature


    * **class_size** (*int*) – the size of the class.  defaults to the minimum available class size


    * **shuffle_result** (*bool*) – indicates the DataFrame should be shuffled before returning.  Default to True



* **Returns**

    the DataFrame that contains the records with the equal class distribution



* **Return type**

    pd.DataFrame



### ml.dataframes.keep_numeric_features(df: pandas.core.frame.DataFrame)
Takes the DataFrame and removes all non-numeric columns or features


* **Parameters**

    **df** (*pd.DataFrame*) – The DataFrame that should have its non-numerics removed



* **Returns**

    The DataFrame with only the numeric features



* **Return type**

    pd.DataFrame



### ml.dataframes.one_hot_encode(df: pandas.core.frame.DataFrame, column_name: str, drop_column: bool = True, prefix: Optional[str] = None)
Take a categorical column and pivots the DataFrame to add columns (0 or 1 value) for every category


* **Parameters**

    
    * **df** (*pd.DataFrame*) – The DataFrame that contains the column to be encoded


    * **column_name** (*str*) – The name of the column that contains the categorical values


    * **drop_column** (*bool*) – Will remove the original column from the dataframe


    * **prefix** (*str*) – The prefix of the new columns.  By default the original column name will be taken



* **Returns**

    The DataFrame with the one hot encoded features



* **Return type**

    pd.DataFrame



### ml.dataframes.plot_features(df: pandas.core.frame.DataFrame, column_names: Optional[numpy.array] = None, grid_shape=None, fig_size=None)
Plots the distribution of the relevant columns of a DataFrame


* **Parameters**

    
    * **df** (*pd.DataFrame*) – The DataFrame that should have its non-numerics removed


    * **column_names** (*np.array*) – The columns that should be plotted.  If None, all numeric columns will be taken


    * **grid_shape** (*int**, **int*) – The shape of the plotting grid (rows, cols).  If None, the grid will have maximum 5 columns


    * **fig_size** (*int**, **int*) – The size of the full plotting grid.  If None, auto size will be applied



* **Returns**

    The figure of the plot and the axes of the plot will be returned for further tuning where needed



* **Return type**

    figure, axes (tuple)



### ml.dataframes.shuffle(df: pandas.core.frame.DataFrame)
Shuffles the DataFrame and returns it


* **Parameters**

    **df** (*pd.DataFrame*) – The DataFrame that should have its records shuffled



* **Returns**

    The DataFrame that is shuffled



* **Return type**

    pd.DataFrame



### ml.dataframes.to_timeseries(df: pandas.core.frame.DataFrame, time_column: str)
This is deprecated and it is advised to use the timeseries.set_timeseries function for this

## Module contents
