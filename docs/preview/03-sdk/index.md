<!-- markdownlint-disable -->

# API Overview

## Modules

- [`ml`](./ml.md#module-ml)
- [`ml.dataframes`](./ml.dataframes.md#module-mldataframes): The dataframes module provides a lot of common operations for dataframe handling
- [`ml.evaluation`](./ml.evaluation.md#module-mlevaluation)
- [`ml.evaluation.classification`](./ml.evaluation.classification.md#module-mlevaluationclassification): The classification module allows users to evaluate and visualize classifiers
- [`ml.images`](./ml.images.md#module-mlimages)
- [`ml.images.conversion`](./ml.images.conversion.md#module-mlimagesconversion): The conversion module allows users to transform images freely
- [`ml.images.explorer`](./ml.images.explorer.md#module-mlimagesexplorer): The image explorer module provides standard helper functions to explore and visualize images
- [`ml.images.io`](./ml.images.io.md#module-mlimagesio): The io module provides standard helper functions to load images from disk
- [`ml.neuralnetworks`](./ml.neuralnetworks.md#module-mlneuralnetworks)
- [`ml.neuralnetworks.keras`](./ml.neuralnetworks.keras.md#module-mlneuralnetworkskeras): The keras module provides additions to work and visualize Keras neural networks
- [`ml.timeseries`](./ml.timeseries.md#module-mltimeseries)
- [`ml.timeseries.timeops`](./ml.timeseries.timeops.md#module-mltimeseriestimeops): The timeops module provides helpful functionality for timeseries datasets

## Classes

- No classes

## Functions

- [`dataframes.distribute_class`](./ml.dataframes.md#function-distribute_class): Makes sure a DataFrame is returned with an equal class distribution
- [`dataframes.keep_numeric_features`](./ml.dataframes.md#function-keep_numeric_features): Takes the DataFrame and removes all non-numeric columns or features
- [`dataframes.one_hot_encode`](./ml.dataframes.md#function-one_hot_encode): Take a categorical column and pivots the DataFrame to add columns (0 or 1 value) for every category
- [`dataframes.plot_features`](./ml.dataframes.md#function-plot_features): Plots the distribution of the relevant columns of a DataFrame
- [`dataframes.shuffle`](./ml.dataframes.md#function-shuffle): Shuffles the DataFrame and returns it
- [`dataframes.to_timeseries`](./ml.dataframes.md#function-to_timeseries): This is deprecated and it is advised to use the timeseries.set_timeseries function for this
- [`classification.evaluate_model`](./ml.evaluation.classification.md#function-evaluate_model): Will predict and evaluate a model against a test set
- [`classification.plot_roc_curve`](./ml.evaluation.classification.md#function-plot_roc_curve): Will plot the Receiver Operating Characteristic (ROC) Curve for binary classifiers
- [`conversion.crop`](./ml.images.conversion.md#function-crop): Crops an image based on the specified size
- [`conversion.get_fragments`](./ml.images.conversion.md#function-get_fragments): Scans an image and return the resulted parts as a list of image sections
- [`conversion.prepare`](./ml.images.conversion.md#function-prepare): Takes an image and applies preformatting
- [`conversion.to_blackwhite`](./ml.images.conversion.md#function-to_blackwhite): Transforms an image to a black & white image
- [`explorer.show_image`](./ml.images.explorer.md#function-show_image): Visualizes an image
- [`explorer.visualize`](./ml.images.explorer.md#function-visualize): Visualizes the images in the image_sets in a grid
- [`explorer.visualize_classes`](./ml.images.explorer.md#function-visualize_classes): Visualizes the images from the image_set in a grid and print the corresponding class on the charts
- [`io.load_image_from_disk`](./ml.images.io.md#function-load_image_from_disk): Loads an image from file, applying preformatting
- [`io.load_image_from_url`](./ml.images.io.md#function-load_image_from_url): Loads an image from a given url, applying preformatting and supporting file caching
- [`io.load_images`](./ml.images.io.md#function-load_images): Loads the images from a specific folder
- [`io.load_images_from_dataframe`](./ml.images.io.md#function-load_images_from_dataframe): Loads a set images from disk, based on the file name in a Data Frame.  
- [`keras.enable_gpu`](./ml.neuralnetworks.keras.md#function-enable_gpu): Enables Keras to run on the GPU
- [`timeops.add_time_reference`](./ml.timeseries.timeops.md#function-add_time_reference): This method will add a reference column to the DataFrame that contains the value of reference column of n items before
- [`timeops.combine_time_ranges`](./ml.timeseries.timeops.md#function-combine_time_ranges): This method combines multiple timeseries (as DataFrame) and removes the overlapping time sections
- [`timeops.get_windows`](./ml.timeseries.timeops.md#function-get_windows): This method take a DataFrame and returns a set of time windows of a specific length and a given column, eventually grouped by another column
- [`timeops.set_timeseries`](./ml.timeseries.timeops.md#function-set_timeseries): Transforms the dataframe to a timeseries enabled dataframe
- [`timeops.time_slice`](./ml.timeseries.timeops.md#function-time_slice): This method takes a time series DataFrame and only returns the time slice, based on the start & end date


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
