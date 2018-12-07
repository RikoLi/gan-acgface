from gan import *
from keras.preprocessing import image as IMG_prepro
import os
import matplotlib.pyplot as pyplot
dcgan = DCGAN()
dcgan.train(epochs=40000, batch_size=64, save_interval=50)