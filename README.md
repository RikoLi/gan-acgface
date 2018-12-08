# A GAN Demo: ACG-Style Faces Generating
## Introduction
Try to build a GAN to generate ACG-style faces. I can pick some out as my SNS avatar, maybe...(if I make it :D)

## Prerequisite
### Codes
* main.py
* gan.py
* utils.py
* generate.py

`main.py` is for training, predicting process controlling.

`gan.py` is for net construction.

`utils.py` is for other tool functions.

`generate.py` is for generating face images.

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

## References
Code references: [GAN-Zoo](https://github.com/hindupuravinash/the-gan-zoo)

Paper references: 
* [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661v1) (arxiv id: 1406.2661v1)
* [Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784v1) (arxiv id: 1411.1784v1)
* [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434v2) (arxiv id: 1511.06434v2)


## Results
Here are some generated avatars. I used a 300-d noise as input and trained for 40k epoches. In each epoch, I used 64 training images to feed the model.

![14](example/14.png "No.14") ![72](example/72.png "No.72") ![77](example/77.png "No.77") ![216](example/216.png "No.216") ![221](example/221.png "No.221") ![238](example/238.png "No.238") ![239](example/239.png "No.239") ![249](example/249.png "No.249") ![250](example/250.png "No.250") ![258](example/258.png "No.258") ![260](example/260.png "No.260") ![276](example/276.png "No.276") ![277](example/277.png "No.277")

As you can see, the quality of these avatars are not good enough. In fact, for most of the generated images you can only recognize blurry faces so I just picked out some well-performed results. It is hard but worth to improve the model's performance.