import sys
import os
import pytest
import pandas as pd 
import arcus.ml.images.explorer as exp
import arcus.ml.images.io as imgio
import logging

image_path_1 = 'tests/resources/images/lungs'
image_path_2 = 'tests/resources/images/lungmasks'

def test_visualize_random_images():
    lungs = imgio.load_images(image_path_1)
    masks = imgio.load_images(image_path_2)

    exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=True)

def test_visualize_first_images():
    lungs = imgio.load_images(image_path_1)
    masks = imgio.load_images(image_path_2)

    exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=False)

def test_visualize_3d_shape_images():
    lungs = imgio.load_images(image_path_1, convert_to_grey=True, keep_3d_shape=True)
    masks = imgio.load_images(image_path_2, convert_to_grey=True, keep_3d_shape=True)

    exp.visualize({'lungs': lungs, 'masks': masks}, image_count = 6, randomize=True)


def test_visualize_oneset_images():
    lungs = imgio.load_images(image_path_1)

    exp.visualize({'lungs': lungs}, image_count = 6, randomize=True)
