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



# dataset_path = '/DATA/wangshen_data/ShortLongDataset/Combined_Dataset'

# dataset_path = '/DATA/wangshen_data/ShortLongDataset/Sony240'
# dataset_path = '/DATA/wangshen_data/ShortLongDataset/Gopro240'
dataset_path = '/DATA/wangshen_data/ShortLongDataset/Adobe240'
type_img = ['sharp']
mode = ['train']


print(dataset_path)
for  mode_ in mode:
    print(mode_)
    for type_ in type_img:
        print(type_)
        data_path = os.path.join(dataset_path, mode_+'_'+type_)
        list_path = os.path.join(dataset_path, mode_+'_list')
        items = sorted(os.listdir(list_path))
        for it in items:
            it_name = it[:-12]
            list_file_path = os.path.join(list_path, it)
            f = open(list_file_path, "r")
            subits = f.read().split('\n')
            for subit in subits:
                subit = subit.split('/')[0]
                img_folder_path = os.path.join(data_path, it_name, subit)
                # print(img_folder_path)
                imgs = sorted(os.listdir(img_folder_path))
                if (mode_ == 'noise') or (mode_ == 'sharp'):
                    assert len(imgs) == 21
                for img in imgs:
                    img_path = os.path.join(img_folder_path, img)
                    # counter = counter + 1
                    try:
                        # print(img_path)
                        a = imread(img_path)
                        # print(counter)
                    except:
                        print(img_path)
