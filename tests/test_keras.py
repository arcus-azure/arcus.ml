import sys
import os
import pytest
import pandas as pd 
import arcus.ml.neuralnetworks.keras as nnk
import logging

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()

def check_gpu():
    from tensorflow.python.client import device_lib

    local_device_protos = device_lib.list_local_devices()
    return len([x.name for x in local_device_protos if x.device_type == 'GPU']) > 0

def test_gpu():
    if not check_gpu():
        import pytest
        pytest.skip('Test requires GPU')

    # print dataframe. 
    assert nnk.enable_gpu() == True

