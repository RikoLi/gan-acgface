# A GAN Demo: ACG-Style Faces Generating
---
## Introduction
---
Try to build a GAN to generate ACG-style faces. I can pick some out as my SNS avatar, maybe...(if I make it :D)

## Prerequisite
---
### Codes
* main.py
* gan.py

`main.py` is for training, predicting process controlling.

`gan.py` is for net construction.

### Datasets
Downloaded from the Internet, thanks for the data provider!
* faces.zip

`faces.zip` is an ACG-style avatar images dataset, collected from a well-known ACG image website [Konachan](http://konachan.net "Konachan~")

All images in the dataset have been reshaped to appropriate sizes. They are all ACG-style face images.

## Evironment
---
### OS
* Linux CentOS
* Windows 10

The linux server mainly serves as training platform. Win10 is for coding.

### GPU
* Nvidia 920MX
* Nvidia Tesla K40M

920MX is my laptop's GPU, which may not be actully used in this demo.

K40M is from ZJUSPC. Thanks for the authorization of the usage of K40M from ZJUSPC!

### Language and libs
* Python 3.6
* Tensorflow-gpu (version unconfirmed)
* Keras (version unconfirmed)
* matplotlab (version unconfirmed)
* PIL (version unconfirmed)
