# Net definitions
from keras.layers import Input, Dense, Reshape, Flatten, Dropout
from keras.layers import BatchNormalization, Activation, ZeroPadding2D, GaussianNoise
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Sequential, Model
from keras.optimizers import Adam, SGD
from keras import backend as K

import matplotlib.pyplot as plt

import sys

import numpy as np
from utils import *

def makeG(noise_dim, channels):
    gaussian_stddev = 0.01

    inputs = Input(shape=(noise_dim,))
    fc = Dense(128 * 32 * 32)(inputs)
    fc = LeakyReLU(alpha=0.2)(fc)
    reshape = Reshape((32, 32, 128))
    up_sample = UpSampling2D()(reshape)
    up_sample = GaussianNoise(gaussian_stddev)(up_sample)

    c1 = Conv2D(128, kernel_size=3, padding='same')(up_sample)
    c1 = LeakyReLU(alpha=0.2)(c1)
    c1 = BatchNormalization(momentum=0.8)(c1)
    c1 = UpSampling2D()(c1)
    c1 = Dropout(0.1)(c1)

    c2 = Conv2D(128, kernel_size=3, padding='same')(c1)
    c2 = LeakyReLU(alpha=0.2)(c2)
    c2 = BatchNormalization(momentum=0.8)(c2)
    c2 = UpSampling2D()(c2)
    c2 = Dropout(0.1)(c2) 

    c3 = Conv2D(128, kernel_size=3, padding='same')(c2)
    c3 = LeakyReLU(alpha=0.2)(c3)
    c3 = BatchNormalization(momentum=0.8)(c3)

    c4 = Conv2D(channels, kernel_size=3, padding='same')(c3)
    outputs = Activation('tanh')(c4)
    G = Model(inputs=inputs, outputs=outputs)
    G.summary()

    return G


def makeD(img_shape):
    gaussian_stddev = 0.1

    inputs = Input(shape=img_shape)
    c1 = Conv2D(32, kernel_size=3, padding='same')(inputs)
    c1 = Conv2D(32, kernel_size=3, padding='same')(c1)
    c1 = LeakyReLU(alpha=0.2)(c1)
    c1 = BatchNormalization(momentum=0.8)(c1)
    c1 = GaussianNoise(gaussian_stddev)(c1)
    c1 = Dropout(0.5)(c1)

    c2 = Conv2D(64, kernel_size=3, padding='same')(c1)
    c2 = Conv2D(64, kernel_size=3, padding='same')(c2)
    c2 = LeakyReLU(alpha=0.2)(c2)
    c2 = BatchNormalization(momentum=0.8)(c2)
    c2 = GaussianNoise(gaussian_stddev)(c2)
    c2 = Dropout(0.5)(c2)

    c3 = Conv2D(128, kernel_size=3, padding='same')(c2)
    c3 = Conv2D(128, kernel_size=3, padding='same')(c3)
    c3 = LeakyReLU(alpha=0.2)(c3)
    c3 = BatchNormalization(momentum=0.8)(c3)
    c3 = Dropout(0.25)(c3)

    c3 = Flatten()(c3)
    outputs = Dense(1, activation='sigmoid')(c3)
    D = Model(inputs=inputs, outputs=outputs)
    D.summary()
    
    return D

# GAN loss
def D_loss(y_true, y_pred):
    res = -1.0 * K.log(y_pred)
    return res