import cv2
import numpy as np
import random
import os

def imread(path):
    # print(path)
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    # covert BRG to RGB
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # convert BGR to RGB
    img = img[:,:,[2, 1, 0]]
    return img

def imsave(path, img):
    # convert RGB to BGR
    img = img[:,:,[2, 1, 0]]
    # save
    cv2.imwrite(path, img)


# dataset_path = '/DATA/wangshen_data/ShortLongDataset/Sony240/full_sharp'
dataset_path = '/DATA/wangshen_data/ShortLongDataset/Sony240/test'
all_dirs = sorted(os.listdir(dataset_path))
# counter = 0
for  dir in all_dirs:
    list_path = os.path.join(dataset_path, dir)
    items = sorted(os.listdir(list_path))  # imgs
    num = len(items)
    print(list_path, num)
    for it in items:
        img_path = os.path.join(list_path, it)
        # counter = counter + 1
        try:
            # print(img_path)
            a = imread(img_path)
            # print(counter)
        except:
            print(img_path)


