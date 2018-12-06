from gan import *
from keras.preprocessing import image as IMG_prepro
import os
import matplotlib.pyplot as pyplot

# Import real image list
img_name_list = os.listdir('../datasets/acg_faces')

img_list = []
counter = 0
# Import real images
for item in img_name_list:
    img = pyplot.imread('../datasets/acg_faces/'+item)
    img_list.append(img)
    counter += 1
    print('Process:', counter, '/', len(img_name_list), 'Percentage:', counter/len(img_name_list))

# dcgan = DCGAN()
# dcgan.train(epochs=4000, batch_size=32, save_interval=50)