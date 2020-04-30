'''
The conversion module allows users to transform images freely
'''

import logging
import os
import numpy as np
from cv2 import imread
from skimage import transform

_logger = logging.getLogger()

def to_blackwhite(image_list: np.array, threshold = 128) -> np.array:
    '''
    Transforms an image to a black & white image
    Args:
        image_list (np.array): A numpy array that contains all selected images represented as np.array
        threshold (int): The threshold (between 0 and 255) that decides a pixel will be 0 or 255 (W/B)
    Returns: 
        np.array: A numpy array that contains all black & white images represented as np.array
    '''
    images = []
    for img in image_list:
        # Check if the image is scaled down by 255 or not
        if(np.count_nonzero(img > 1)==0):
            img *= 255
        if(len(img.shape) == 3):
            if(img.shape[2] == 3):
                # Convert to grey scale
                img = np.dot(img, [0.3, 0.59, 0.11])
        # make all pixels < threshold black
        img = 1.0 * (img > threshold) 
        images.append(img)
    
    return np.array(images)