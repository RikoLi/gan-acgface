from gan import *
import os
import matplotlib.pyplot as pyplot
from keras.models import *
from keras.utils import *

import numpy as np

# Train
dcgan = DCGAN()
dcgan.train(epochs=50000, batch_size=16, save_interval=50)

