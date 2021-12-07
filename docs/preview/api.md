<!-- markdownlint-disable -->

# API Overview

## Modules

- [`evaluation`](./evaluation.md#module-evaluation)
- [`evaluation.classification`](./evaluation.classification.md#module-evaluationclassification): The classification module allows users to evaluate and visualize classifiers
- [`images`](./images.md#module-images)
- [`images.conversion`](./images.conversion.md#module-imagesconversion): The conversion module allows users to transform images freely
- [`images.explorer`](./images.explorer.md#module-imagesexplorer): The image explorer module provides standard helper functions to explore and visualize images
- [`neuralnetworks`](./neuralnetworks.md#module-neuralnetworks)
- [`neuralnetworks.keras`](./neuralnetworks.keras.md#module-neuralnetworkskeras): The keras module provides additions to work and visualize Keras neural networks
- [`timeseries`](./timeseries.md#module-timeseries)
- [`timeseries.timeops`](./timeseries.timeops.md#module-timeseriestimeops): The timeops module provides interesting standard functionality for timeseries datasets

## Classes

- No classes

## Functions

- [`classification.evaluate_model`](./evaluation.classification.md#function-evaluate_model): Will predict and evaluate a model against a test set
- [`classification.plot_roc_curve`](./evaluation.classification.md#function-plot_roc_curve): Will plot the Receiver Operating Characteristic (ROC) Curve for binary classifiers
- [`conversion.crop`](./images.conversion.md#function-crop): Crops an image based on the specified size
- [`conversion.get_fragments`](./images.conversion.md#function-get_fragments): Scans an image and return the resulted parts as a list of image sections
- [`conversion.prepare`](./images.conversion.md#function-prepare): Takes an image and applies preformatting
- [`conversion.to_blackwhite`](./images.conversion.md#function-to_blackwhite): Transforms an image to a black & white image
- [`explorer.show_image`](./images.explorer.md#function-show_image): Visualizes an image
- [`explorer.visualize`](./images.explorer.md#function-visualize): Visualizes the images in the image_sets in a grid
- [`explorer.visualize_classes`](./images.explorer.md#function-visualize_classes): Visualizes the images from the image_set in a grid and print the corresponding class on the charts
- [`keras.enable_gpu`](./neuralnetworks.keras.md#function-enable_gpu): Enables Keras to run on the GPU
- [`timeops.add_time_reference`](./timeseries.timeops.md#function-add_time_reference): This method will add a reference column to the DataFrame that points to n items before
- [`timeops.combine_time_ranges`](./timeseries.timeops.md#function-combine_time_ranges)
- [`timeops.get_windows`](./timeseries.timeops.md#function-get_windows)
- [`timeops.set_timeseries`](./timeseries.timeops.md#function-set_timeseries): Transforms the dataframe to a timeseries enabled dataframe
- [`timeops.time_slice`](./timeseries.timeops.md#function-time_slice): This method takes a time series DataFrame and only returns the time slice, based on the start & end date


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
