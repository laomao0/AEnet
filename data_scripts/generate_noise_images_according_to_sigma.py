import os.path
import os
import random
import math
from scipy.misc import imsave
import cv2
import numpy as np
from skimage.util import random_noise
import math

def add_noise(img, mode='gaussian', mean=0, var=0.01, level=None):
    """
    img: 0-1 or 0-255
    noisy_img: 0-255
    """
    if level:
        var = (level/255.0)**2
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

def make_dataset(root, list_file_folder, shuffle=False):
    raw_im_list = []
    items = sorted(os.listdir(os.path.join(root, list_file_folder)))
    for it in items:
        it_name = it[:-12]
        it_path = os.path.join(root, list_file_folder, it)
        f = open(it_path, "r")
        subits = f.read().split('\n')
        for idx, subit in enumerate(subits):
            if idx == 10:
                break
            key = '{}/{}'.format(it_name, subit.split('/')[0])
            raw_im_list.append(key)
    if shuffle == True:
        random.shuffle(raw_im_list)
    return  raw_im_list



def ShortLong_loader(root, im_path, output_root, img_list, level):

    

    folder, subfolder = im_path.split('/')


    short_root = os.path.join(root, 'test_sharp', folder, subfolder)

    output_folder = os.path.join(output_root, folder)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    output_subfolder = os.path.join(output_root, folder, subfolder)
    if not os.path.exists(output_subfolder):
        os.mkdir(output_subfolder)

    # add gaussion noise to short imgs
    # noise_var = np.random.uniform(0.01, 0.1)
    noise_var = level

    for i in range(1, 22):
        img_name = '{:05d}.png'.format(i)
        path_short_path = os.path.join(short_root, img_name)
        output_path = os.path.join(output_subfolder, img_name)
        if not os.path.exists(output_path):
            img_short = imread(path_short_path)
            img_short_noisy = add_noise(img_short, var=None, level=level)
            imsave(output_path, img_short_noisy)
        print(noise_var, output_path)

    img_list.append(im_path+'/'+str(noise_var)+'/'+str(math.sqrt(noise_var)*255.0))

    return img_list

    

level = 60
root = '/DATA/wangshen_data/ShortLongDataset/Combined_Dataset'
out_root = '/DATA/wangshen_data/ShortLongDataset/Combined_Dataset/test_noise_random'
out_root = out_root+'_{}'.format(level)


random.seed(0)
np.random.seed(0)

if not os.path.exists(out_root):
    os.mkdir(out_root)

test_list = make_dataset(root,"test_list", shuffle=False)

WRIList = []
for it in test_list:
    WRIList = ShortLong_loader(root, it, out_root, WRIList, level)

# fl = open(os.path.join(out_root, "noise_str.txt"), 'w')
# sep = '\n'
# fl.write(sep.join(WRIList))
# fl.close()
