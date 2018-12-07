# A GAN Demo: ACG-Style Faces Generating
## Introduction
Try to build a GAN to generate ACG-style faces. I can pick some out as my SNS avatar, maybe...(if I make it :D)

## Prerequisite
### Codes
* main.py
* gan.py
* utils.py

`main.py` is for training, predicting process controlling.

`gan.py` is for net construction.

`utils.py` is for other tool functions.

### Datasets
Downloaded from the Internet, thanks for the data provider!
* faces.zip

`faces.zip` is an ACG-style avatar images dataset, collected from a well-known ACG image website [Konachan](http://konachan.net "Konachan~")

All images in the dataset have been reshaped to appropriate sizes. They are all ACG-style face images.

## Evironment
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
* matplotlib (version unconfirmed)
* PIL (version unconfirmed)

## References
Code references: [GAN-Zoo](https://github.com/hindupuravinash/the-gan-zoo)

Paper references: 
* [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661v1) (arxiv id: 1406.2661v1)
* [Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784v1) (arxiv id: 1411.1784v1)
* [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434v2) (arxiv id: 1511.06434v2)
