"""
   This script computes the blurry input psnr and ssim of each test set.
"""
import time
import os
import threading
import sys
import getopt
import math
import numpy
import random
import logging
import numpy as np
import os
from skimage.measure import compare_ssim,compare_psnr
from scipy.misc import imsave
import matplotlib as mpl
import numpy
from scipy.misc import imread, imsave, imshow, imresize, imsave
import shutil
import  time

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


DO_GOTest = False

test_or_train = 'test'  # 'test'

val_fps = 30  # output 48fps
DO_GO = True

Output_PATH = "/DATA/wangshen_data/ShortLongDataset/Adobe240"
GO_Other_DATA = Output_PATH + '/' + test_or_train + "_blur"
GO_Other_GT = Output_PATH + '/'  + test_or_train + '_sharp'
IMG_LIST = Output_PATH + '/' + test_or_train + "_list"


print("We check the our blurry inputs using the " + test_or_train + " dataset to check psnr and ssim!")



def Compute_go_pro_large():

    total_run_time = AverageMeter()

    if DO_GO:
        subdir = sorted(os.listdir(GO_Other_DATA))  # folder 0 1 2 3...

        psnr_total = AverageMeter()
        ssim_total = AverageMeter()

        for dir in subdir:

            psnr_total.reset()

            img_list = os.path.join(IMG_LIST, dir+'_im_list.txt')
            f = open(img_list, "r")
            subfolders = f.read().split('\n')

            for index, its in enumerate(subfolders):

                subfolder, _ = its.split('/')

                # blurry
                b1 = os.path.join(GO_Other_DATA, dir, subfolder, '00006.png')  
                b2 = os.path.join(GO_Other_DATA, dir, subfolder, '00016.png')  

                gt1 = os.path.join(GO_Other_GT, dir, subfolder, '00006.png')
                gt2 = os.path.join(GO_Other_GT, dir, subfolder, '00016.png')  

                gt1_img = imread(gt1)
                gt2_img = imread(gt2)
                b1_img =  imread(b1)
                b2_img =  imread(b2)

                psnr_1 = compare_psnr(b1_img, gt1_img)
                psnr_2 = compare_psnr(b2_img, gt2_img)

                psnr = (psnr_1 + psnr_2)*0.5
                pstring = "blurry PSNR : "  + str( round(psnr, 4)) 
                print(pstring)

                psnr_total.update(psnr, 1)



            pstring = "The results for dir:" + dir
            print(pstring)
            print(pstring, file=open(os.path.join(Output_PATH, test_or_train+"_statis_dir.txt"), "a"))
            # end for folders
            pstring = "Avg PSNR " + str(psnr_total.avg) 
            print(pstring)
            print(pstring, file=open(os.path.join(Output_PATH, test_or_train+"_statis_dir.txt"), "a"))






if __name__ == '__main__':
    Compute_go_pro_large( )
