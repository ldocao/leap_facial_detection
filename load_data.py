##PURPOSE: operations on raw data
from constants import *
import os
import ipdb
import pandas as pd
import numpy as np
import sklearn


def _rescale_coordinates(target):
    """Convert coordinates to [-1,1]

    Parameters:
    ----------
    target: np.array
        all target values
    """

    target = (target - HALF_SIZE_IMAGE) / HALF_SIZE_IMAGE  # scale target coordinates to [-1, 1]
    return target.astype(np.float32)

def _as_normalized_grayscale(serie):
    """Convert to float np.array, and normalize to [0,1]

    Parameters:
    ----------
    serie: pd.Series
        list of value of pixels [0,255] of image
    """
    features = np.vstack(serie.values) / GRAYSCALE  # scale pixel values to [0, 1]
    return features.astype(np.float32)

def _separate_pixels(image):
    """Return an array where each pixel values has been separated

    Parameters:
    ----------
    image: pd.Series
    """

    return image.apply(lambda im: np.fromstring(im, sep=' ')) # the Image column has pixel values separated by space; convert the values to numpy arrays





def training(cols=None):
    """Return features and target separately


    """

    df = pd.read_csv(os.path.expanduser(FTRAIN)) 
    df['Image'] = _separate_pixels(df['Image'])
    if cols: df = df[list(cols) + ['Image']]

    ##renormalisation, cleanup
    df = df.dropna() 
    features = _as_normalized_grayscale(df['Image'])  # scale pixel values to [0, 1]
    target = _rescale_coordinates(df[df.columns[:-1]].values)

    return sklearn.utils.shuffle(features, target, random_state=42)  # shuffle train data





def test(cols=None):
    """Loads data from FTEST if *test* is True, otherwise from FTRAIN.
    Pass a list of *cols* if you're only interested in a subset of the
    target columns.
    """

    df = pd.read_csv(os.path.expanduser(FTEST))  # load pandas dataframe
    df['Image'] = _separate_pixels(df['Image'])
    if cols: df = df[list(cols) + ['Image']]

    ##renormalisation and clean up
    df = df.dropna()  # drop all rows that have missing values in them
    features = _as_normalized_grayscale(df['Image'])

    return features
