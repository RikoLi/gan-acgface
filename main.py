from gan import *
from keras.preprocessing import image as IMG_prepro
import os
import matplotlib.pyplot as pyplot
x = loadData('../datasets/acg_faces/')
# dcgan = DCGAN()
# dcgan.train(epochs=4000, batch_size=32, save_interval=50)