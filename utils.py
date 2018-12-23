import os
import matplotlib.pyplot as pyplot
import numpy as np
from PIL import Image

def loadData(path):
    '''
    Load data from folder.\n
    Para: dataset path\n
    Return: Numpy array
    '''
    # Import real image list
    img_name_list = os.listdir(path)
    img_list = []
    counter = 0
    # Import real images
    for item in img_name_list:
        img = pyplot.imread(path+item)
        img_list.append(img)
        counter += 1
        per = float((counter / len(img_name_list))*100)
        print('Process percentage:', str(round(per, 2)), '/ 100')
    print('Total', len(img_name_list), 'images.')
    print('Training data has been loaded.')
    array = np.array(img_list)
    return array

# Resize images
def resizeImg(from_path, save_path, size):
    img_list = os.listdir(from_path)
    for img in img_list:
        new_img = Image.open(from_path+img)
        new_img = new_img.resize((size,size), Image.ANTIALIAS)
        new_img.save(save_path+'_'+str(size)+'.jpg', 'jpeg', quality=95)

# resizeImg('../datasets/hqfaces/', '../datasets/112_hqfaces/', 112)

# Batch rename
def dataRename(path, new_name):
    old_name_list = os.listdir(path)
    for item in old_name_list:
        os.rename(path+item, path+str(new_name)+item)

# Plot training process
def save_imgs(epoch, noise_dim, which_generator):
    r, c = 3, 3
    noise = np.random.normal(0, 1, (r * c, noise_dim))
    gen_imgs = which_generator.predict(noise)

    gen_imgs = (gen_imgs + 1) / 2 * 255
    gen_imgs = gen_imgs.astype(np.uint8)

    fig, axs = pyplot.subplots(r, c)
    cnt = 0
    for i in range(r):
        for j in range(c):
            axs[i,j].imshow(gen_imgs[cnt,:,:,:])
            axs[i,j].axis('off')
            cnt += 1
    fig.savefig("images/iteration_%d.png" % epoch)
    pyplot.close()
