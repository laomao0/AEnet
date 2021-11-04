import torch.utils.data as data
import os
import os.path
from scipy.misc import imsave
import cv2
import numpy as np
import random
from skimage.util import random_noise
from PIL import Image, ImageEnhance

'''
for deepslomo motion dataloader
only use center img
'''


def add_noise(img, mode='gaussian', mean=0, var=0.01):
    """
    img: 0-1 or 0-255
    noisy_img: 0-255
    """
    noisy_img = random_noise(img, mode=mode, clip=True, mean=mean, var=var)
    noisy_img = (noisy_img * 255.0).clip(0, 255).astype('uint8')
    return noisy_img


def imread(path):
    # print(path)
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)  # HWC
    # convert BGR to RGB
    try:
        img = img[:, :, [2, 1, 0]]
    except:
        print(path)
    return img


def imsave(path, img):
    # convert RGB to BGR
    img = img[:, :, [2, 1, 0]]
    # save
    cv2.imwrite(path, img)

def create_blur(path_list):
    sum = 0.0
    for it in path_list:
        sum = sum + imread(it).astype("float32")
    sum = sum / float(len(path_list))
    sum = sum.astype("uint8")
    return sum


D1  = [6] 
D2  = [7,8,9, 10,11,12, 13,14,15]
D3  = [16] 
D4  = [17,18,19, 20,21,22, 23,24,25]
D5  = [26] 
D6  = [27,28,29, 30,31,32, 33,34,35]
D7  = [36]
D8  = [37,38,39,40,41,42,43,44,45]
D9  = [46]
D10 = [47,48,49,50,51,52,53,54,55]
D11 = [56]
D12 = [57,58,59,60,61,62,63,64,65]
D13 = [66]
D14 = [67,68,69,70,71,72,73,74,75]

All = [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14]

Num = 14


PathGT = '/DATA/wangshen_data/CODES/low-lit-enhance/results/SYN_GOPR0854_11_00'

PathOutBase = '/DATA/wangshen_data/CODES/low-lit-enhance/results/test_GOPR0854_11_00'

if not os.path.exists(PathOutBase):
    os.mkdir(PathOutBase)

a = 0.01
b= 0.1
noise_var = np.random.uniform(a, b)

for i in range(Num):

    PathOut=  os.path.join(PathOutBase, '{:05d}.png'.format(i))
    if i % 2 == 0: # short
        im_short = []
        for it in All[i]:
            im_short.append(os.path.join(PathGT, '{:05d}.png'.format(it)))
        im = create_blur(im_short)
        
        im = add_noise(im, var=noise_var)
        imsave(PathOut,im)
    else:
        im_long = []
        for it in All[i]:
            im_long.append(os.path.join(PathGT, '{:05d}.png'.format(it)))
        im = create_blur(im_long)
        imsave(PathOut,im)

    print(PathOut)





