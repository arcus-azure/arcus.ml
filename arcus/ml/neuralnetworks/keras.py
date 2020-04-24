'''
The keras module provides additions to work and visualize Keras neural networks
'''

import tensorflow as tf
from tensorflow import keras
import logging
import os

_logger = logging.getLogger()

def enable_gpu() -> bool:
    '''Enables Keras to run on the GPU
    First it checks if there's a "physical device" available of type GPU
    If not, it will try to leverage plaidml for GPU enabling

    Returns: 
        bool: A boolean value indicating if the GPU enablement succeeded
    '''

    gpu_enabled = False
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    if(len(physical_devices)>0):
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        _logger.info('Physical GPU enabled for tensorflow')
        gpu_enabled = True
    else:
        _logger.info('No physical GPU found, trying plaidml now')
        try:
            import plaidml.keras
            gpu_enabled = True
            plaidml.keras.install_backend()
            os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
        except ImportError as e:
            _logger.warning('GPU could not be enabled, as plaidml package was not installed')
    
    return gpu_enabled
