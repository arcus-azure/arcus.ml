'''
The image scanner module provides possibilities to scan through an image
'''

import logging
import numpy as np
from cv2 import imread

_logger = logging.getLogger()



def get_portion(image: np.array, stride: tuple = (1,1), portion_size: tuple = (1,1), rectangle = None):
    '''

    '''