'''
The image explorer module provides standard helper functions to explore and visualize images
'''

import logging
import numpy as np
from cv2 import imread
from skimage import transform
import matplotlib.pyplot as plt
import random

_logger = logging.getLogger()

def show_image(image: np.array, hide_grid: bool = True, grid_size = None):
    '''
    Visualizes an image
    Args:
        image (np.array): the image to visualize, represented as numpy array
        hide_grid (bool): indicating if the grid (with the pixel positions) should be hidden
        grid_size ((int, int)): the size of the grid to plot the images in.  By default auto size is being applied
    '''
    _image_shape = image.shape
    _is_grey_scale = len(_image_shape) == 2
    if(len(_image_shape)==3):
        if(_image_shape[2]==1): # Grey scale image in 3D shape
            _is_grey_scale = True
            image = image.reshape(_image_shape[0], _image_shape[1])
    _cmap = 'Greys_r' if _is_grey_scale else None

    plt.imshow(image, interpolation='nearest', cmap = _cmap)
    if(hide_grid):
        plt.axis('off')
    plt.show()

def visualize(image_sets: dict, image_count: int = 10, randomize: bool = True, grid_size = None, hide_grid: bool = True):
    '''
    Visualizes the images in the image_sets in a grid
    Args:
        image_sets (dict): a dictionary of type (str, list) that indicates the name of an images set and the actual images
        image_count (int): the amount of images to visualize from an image set
        randomize (bool): if True, images will be selected randomly from the imageset, if False, the first n images will be taken
        grid_size ((int, int)): the size of the grid to plot the images in.  By default auto size is being applied
        hide_grid (bool): indicates if the grid with pixellocations should be hidden

    Example:
        image_sets = {'predicted': y_pred, 'actuals': y_test}
        visualize(image_sets, 6, False)
    '''
    _f, _axes = plt.subplots(len(image_sets), image_count, figsize=grid_size, sharex=False)
    _nr_of_images = len(image_sets[list(image_sets.keys())[0]])
    if(image_count > _nr_of_images):
        image_count = _nr_of_images
    if(image_count == 1):
        _image_indices = [0]
    else:
        _image_indices = random.sample(range(0, _nr_of_images - 1), image_count) if randomize else range(0, image_count)
                    

    _set_index = 0
    for _set_name in image_sets.keys():
        _logger.debug('Visualizing images from %s set', _set_name)
        _image_index = 0
        for idx in _image_indices:
            _current_image = image_sets[_set_name][idx]
            _image_shape = _current_image.shape
            _is_grey_scale = len(_image_shape) == 2
            if(len(_image_shape)==3):
                if(_image_shape[2]==1): # Grey scale image in 3D shape
                    _is_grey_scale = True
                    _current_image = _current_image.reshape(_image_shape[0], _image_shape[1])
            _cmap = 'Greys_r' if _is_grey_scale else None
            if(len(image_sets) > 1):
                _axes[_set_index, _image_index].imshow(_current_image, cmap = _cmap)
            else:
                _axes[_image_index].imshow(_current_image, cmap = _cmap)
            _image_index += 1
        _set_index += 1
    if(hide_grid):
        [axi.set_axis_off() for axi in _axes.ravel()]
    
def visualize_classes(image_set: np.array, classes: np.array, image_count: int = 10, randomize: bool = True, grid_size = None):
    '''
    Visualizes the images from the image_set in a grid and print the corresponding class on the charts
    Args:
        image_set (np.array): an array of images to pick from
        classes (np.array): the corresponding labels of the classes for the images
        image_count (int): the amount of images to visualize from an image set
        randomize (bool): if True, images will be selected randomly from the imageset, if False, the first n images will be taken
        grid_size ((int, int)): the size of the grid to plot the images in.  By default auto size is being applied
    Example:
        image_sets = {'predicted': y_pred, 'actuals': y_test}
        visualize(image_sets, 6, False)
    '''
    _f, _axes = plt.subplots(1, image_count, figsize=grid_size, sharex=False)
    _nr_of_images = len(image_set)
    if(image_count > _nr_of_images):
        image_count = _nr_of_images
    if(image_count == 1):
        _image_indices = [0]
    else:
        _image_indices = random.sample(range(0, _nr_of_images - 1), image_count) if randomize else range(0, image_count)
                    

    _image_index = 0
    for idx in _image_indices:
        _ax = _axes[_image_index]
        _current_image = image_set[idx]
        _current_class = classes[idx]
        _image_shape = _current_image.shape
        _is_grey_scale = len(_image_shape) == 2
        if(len(_image_shape)==3):
            if(_image_shape[2]==1): # Grey scale image in 3D shape
                _is_grey_scale = True
                _current_image = _current_image.reshape(_image_shape[0], _image_shape[1])
        _cmap = 'Greys_r' if _is_grey_scale else None
        _ax.imshow(_current_image, cmap = _cmap)
        _ax.set_title(classes[idx])
        _image_index += 1
    [axi.set_axis_off() for axi in _axes.ravel()]
    