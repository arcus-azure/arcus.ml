import sys
import os
import pytest
import pandas as pd 
import arcus.ml.neuralnetworks.keras as nnk
import logging

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()


def test_gpu():
    # print dataframe. 
    assert nnk.enable_gpu() == True