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

def visualize(image_sets: dict, image_count: int = 10, randomize: bool = True):
    '''
    Visualizes the images in the image_sets in a grid
    Args:
        image_sets (dict): a dictionary of type (str, list) that indicates the name of an images set and the actual images
        image_count (int): the amount of images to visualize from an image set
        randomize (bool): if True, images will be selected randomly from the imageset, if False, the first n images will be taken

    Example:
        image_sets = {'predicted': y_pred, 'actuals': y_test}
        visualize(image_sets, 6, False)
    '''
    _f, _axes = plt.subplots(len(image_sets), image_count, figsize=(20,20), sharex=False)
    _nr_of_images = len(image_sets[list(image_sets.keys())[0]])
    _image_indices = random.sample(range(0, _nr_of_images - 1), image_count) if randomize else range(0, image_count)
                    

    _set_index = 0
    for _set_name in image_sets.keys():
        _logger.debug('Visualizing images from %s set', _set_name)
        _image_index = 0
        for idx in _image_indices:
            _current_image = image_sets[_set_name][idx]
            _axes[_set_index, _image_index].imshow(_current_image)
            _image_index += 1
        _set_index += 1
    [axi.set_axis_off() for axi in _axes.ravel()]