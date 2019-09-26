from gan import *
import os
import matplotlib.pyplot as pyplot
from keras.models import *
from keras.utils import *
import numpy as np

# Predict
batch_size = 50
generator = load_model('../gan_models/12.12/generator.h5')

for i in range(batch_size):
    noise = np.random.normal(0, 1, (1,100))
    img = generator.predict(noise)
    img = (img + 1) / 2 * 255
    img = img.astype(np.uint8)
    pic = img[0,:,:,:]
    pyplot.imsave(fname='./gen_face/'+str(i)+'.png', arr=pic)
print('Done!')