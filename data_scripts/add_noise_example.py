import torch.utils.data as data
import os
import os.path
from scipy.misc import imsave
import cv2
import numpy as np
import random
from skimage.util import random_noise

def add_noise(img, mode='gaussian', mean=0, var=0.01):
    noisy_img = random_noise(img, mode=mode, clip=True, mean=mean, var=var)
    noisy_img = (noisy_img*255.0).clip(0,255).astype('uint8')
    return noisy_img


def imread(path):
    # print(path)
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)  # HWC
    # convert BGR to RGB
    img = img[:,:,[2, 1, 0]]
    return img

def imsave(path, img):
    # convert RGB to BGR
    img = img[:,:,[2, 1, 0]]
    # save
    cv2.imwrite(path, img)


path = '/DATA/wangshen_data/ShortLongDataset/Combined_Dataset/test_sharp/2C0094/00000/00001.png'
save_path = '/DATA/wangshen_data/CODES/low-lit-enhance/data_scripts/noisy_img.png'

img = imread(path)

img  = img / 255.0

noisy_img = add_noise(img)

imsave(save_path, noisy_img)




