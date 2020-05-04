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

def prepare(image: np.array, image_size:int = -1, 
            convert_to_grey: bool = False, keep_3d_shape = False) -> np.array:
    '''
    Takes an image and applies preformatting
    Args:
        image (np.array): The array representation of the image to process
        image_size (int): If the image_size is larger than 0, the images will be resized to a square of this size
        convert_to_grey (bool): This would reduce the size (and shape) of the image in making it a greyscale
        keep_3d_shape (bool): Only used when convert_to_grey is true.  Will keep the images in shape (H,W,1) in that case
    Returns: 
        np.array: A numpy array that represents the preprocessed image
    '''
    
    if(image_size > 0):
        image = transform.resize(image,(image_size, image_size),mode='constant',anti_aliasing=True)

    if(convert_to_grey):
        if(len(image.shape) == 3):
            image = np.dot(image, [0.3, 0.59, 0.11])
        if(len(image.shape)==2 and keep_3d_shape):
            image = np.expand_dims(image, -1)
    
    return image

def crop(image: np.array, x: int, y: int, width: int, height: int) -> np.array:
    '''
    Crops an image based on the specified size
    Args:
        image (np.array): The array representation of the image to crop
        x (int): The x coordinate of the rectangle to keep (horizontal position from the left)
        y (int): The y coordinate of the rectangle to keep (vertical position from the top)
        width (int): The width of the cropped image
        height (int): The height of the cropped image
    Returns: 
        np.array: A numpy array that represents the cropped part of the image
    '''
    return image[y:y + height,x: x+width]

def get_fragments(image: np.array, stride: tuple = (1,1), fragment_size: tuple = (1,1), rectangle = None):
    '''
    
    '''
    portion_list = list()
    if(rectangle!=None):
        # First we will crop the rectangle to scan from the original image
        # Verify the rectangle is valid
        if(len(rectangle)!=4):
            raise TypeError('The rectangle should be a vector of 4 integers: (x, y, width, height)')
        image = crop(image, rectangle[0], rectangle[1], rectangle[2], rectangle[3])
    
    image_width = image.shape[1]
    image_height = image.shape[0]
    fragment_width = fragment_size[0]
    fragment_height = fragment_size[1]

    current_Y = 0
    while current_Y < image_height:
        current_X = 0
        while current_X < image_width:
            if(current_Y + fragment_height) <= image_height and (current_X + fragment_width) <= image_width:
                portion_list.append(crop(image, current_X, current_Y, fragment_width, fragment_height))
            current_X += stride[0]
        current_Y += stride[1]
    
    print(len(portion_list))
    return np.array(portion_list)