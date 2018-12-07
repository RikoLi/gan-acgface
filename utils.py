import os
import matplotlib.pyplot as pyplot
import numpy as np

def loadData(path):
    '''
    Load data from folder.\n
    Para: dataset path\n
    Return: Numpy array
    '''
    # Import real image list
    img_name_list = os.listdir(path)
    img_list = np.array()
    counter = 0
    # Import real images
    for item in img_name_list:
        img = pyplot.imread(path+item)
        img = img.reshape(1, -1)
        img_list.append(img)
        counter += 1
        per = float((counter / len(img_name_list))*100)
        print('Process percentage:', str(round(per, 2)), '/ 100')
    print('Total', len(img_name_list), 'images.')
    print('Training data has been loaded.')
    array = np.array(img_list)
    return array