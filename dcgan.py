# DCGAN model
from keras.layers import Input, Dense, Reshape, Flatten, Dropout
from keras.layers import BatchNormalization, Activation, ZeroPadding2D, GaussianNoise
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Sequential, Model
from keras.optimizers import Adam, SGD
from keras import backend as K
from keras.models import load_model

import matplotlib.pyplot as plt
import sys
import numpy as np

from utils import *
from nets import *

# Set training parameters
iterations = 50000
save_interval = 50

isLoadModel = False
model_path = {'d': '../models/discrimator.h5', 'g': '../models/generator.h5'}

batch_size = 16
img_width = img_height = 256
channels = 3
noise_dim = 100

img_shape = (img_height, img_width, channels)
optimizer = Adam(0.0002, 0.5)

# Import dataset
X_train = loadData('../datasets/acg_faces/')
# Rescale -1 to 1
X_train = X_train / 127.5 - 1.

# Build nets
if isLoadModel:
    discriminator = load_model(model_path['d'], compile=False)
    discriminator.compile(optimizer=optimizer, loss='binary_crossentropy')
    generator = load_model(model_path['g'], compile=False)
else:
    # Build discriminator
    discriminator = makeD(img_shape=img_shape)
    discriminator.compile(optimizer=optimizer, loss='binary_crossentropy')
    # Build generator
    generator = makeG(noise_dim=noise_dim, channels=channels)

# Define the routine of the tensors
input_noise = Input(shape=(noise_dim,))
img = generator(input_noise)
discriminator.trainable = False
d_out = discriminator(img)
# Build G+D combined model
combined = Model(inputs=input_noise, outputs=d_out)
combined.compile(optimizer=optimizer, loss='binary_crossentropy')

# Training
for iteration in range(iterations):
    #### Train the discriminator
    # Sample mini-batch from noise
    noise = np.random.normal(0, 1, (batch_size, noise_dim))
    fake_img_batch = generator.predict(noise)

    # Select mini-batch from real images
    real_img_ids = np.random.randint(0, X_train.shape[0], batch_size)
    real_img_batch = X_train[real_img_ids]

    # Update the discriminator
    real_labels = np.ones((batch_size, 1))
    d_real_loss = discriminator.train_on_batch(real_img_batch, real_labels)
    fake_labels = np.zeros((batch_size, 1))
    d_fake_loss = discriminator.train_on_batch(fake_img_batch, fake_labels)
    
    #### Train the generator
    labels_placeholder = np.ones((batch_size, 1))
    g_loss = combined.train_on_batch(noise, labels_placeholder)

    #### Training process data saving & displaying
    # Display loss
    d_loss = np.add(d_real_loss, d_fake_loss)
    print("Iteration: %d [D loss: %f, acc.: %.2f%%]" % (iteration, d_loss[0], 100*d_loss[1]))

    # If at save interval => save generated image samples
    if iteration % save_interval == 0:
        discriminator.save('../models/discriminator.h5')
        generator.save('../models/generator.h5')
        save_imgs(iteration, noise_dim, generator)
