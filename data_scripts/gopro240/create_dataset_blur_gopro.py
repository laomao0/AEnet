import argparse
import os
import os.path
from shutil import rmtree, move, copy
import random
import cv2
import shutil
import math
from random import choice
random.seed(0)

# For parsing commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument("--ffmpeg_dir", type=str, default='/home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static',
     help='path to ffmpeg.exe')
parser.add_argument("--dataset", type=str, default="gopro240fps_blur", help='specify if using "adobe240fps" or custom video dataset')
# parser.add_argument("--videos_folder", type=str, required=True, help='path to the folder containing videos')
parser.add_argument("--dataset_folder", type=str, default='/DATA/wangshen_data/ShortLongDataset/Gopro240s', help='path to the output dataset folder')
parser.add_argument("--train_test_split", type=tuple, default=(90, 10), help="train test split for custom dataset")
parser.add_argument("--enable_train", default=1, type=int, help="generate train data or not")
args = parser.parse_args()

debug = False
delte_extract = False
#print(args)


def create_clips_overlap(video, root, destination, destionation_blur, listpath):

    # tau_list = [1,3,5,7,9]
    tau_list = [9]

    file = video[0]  #[:-4]

    images = os.listdir(os.path.join(root, file))
    images = sorted(images)
    assert (images[0] == '00001.png')

    n_length = len(images)

    N = 21
    Num = int(n_length/N)

    img_list = []

    for i in range(Num):

        tau = choice(tau_list)

        img_list_1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        img_list_2 = [12,13,14,15,16,17,18,19,20]

        all_imgs = []
        for it in range(N):
            all_imgs.append('{:05d}.png'.format(int(i * N + it + 1)))

        all_imgs_list_1 = []
        for it in img_list_1:
            all_imgs_list_1.append('{:05d}.png'.format(int(i * N + it )))

        all_imgs_list_2 = []
        for it in img_list_2:
            all_imgs_list_2.append('{:05d}.png'.format(int(i * N + it )))


        # make blur data
        blur_folder = os.path.join(destionation_blur, file)
        blur_subfolder = os.path.join(destionation_blur, file, '{:05d}'.format(i))
        os.makedirs(blur_folder, exist_ok=True)
        os.makedirs(blur_subfolder, exist_ok=True)

        # make gt
        gt_folder = os.path.join(destination, file)
        gt_subfolder = os.path.join(destination, file, '{:05d}'.format(i))
        os.makedirs(gt_folder, exist_ok=True)
        os.makedirs(gt_subfolder, exist_ok=True)

        sum = 0.0
        for it in all_imgs_list_1:
            image_name = it
            sum = sum + cv2.imread(os.path.join(root, file, image_name)).astype("float32")
        sum = sum / float(len(all_imgs_list_1))
        sum = sum.astype("uint8")
        cv2.imwrite(os.path.join(blur_subfolder, '00006.png'), sum)

        sum = 0.0
        for it in all_imgs_list_2:
            image_name = it
            try:
                sum = sum + cv2.imread(os.path.join(root, file, image_name)).astype("float32")
            except:
                 print(os.path.join(root, file, image_name))
        sum = sum / float(len(all_imgs_list_2))
        sum = sum.astype("uint8")
        cv2.imwrite(os.path.join(blur_subfolder, '00016.png'), sum)


        for idx, it in enumerate(all_imgs):
            image_name = it
            src = os.path.join(root, file, image_name)
            dst = os.path.join(gt_subfolder, '{:05d}.png'.format(idx+1))
            shutil.copy(src, dst)

        img_list.append('{:05d}/{:04d}'.format(i, tau))

        print(img_list[-1])

    fl = open(os.path.join(listpath, file+ "_im_list.txt"), 'w')
    sep = '\n'
    fl.write(sep.join(img_list))
    fl.close()

    # fl = open(os.path.join(destionation_blur, file+"_im_list.txt"), 'w')
    # sep = '\n'
    # fl.write(sep.join(im_list))
    # fl.close()



def main():
    # Create dataset folder if it doesn't exist already.
    if not os.path.isdir(args.dataset_folder):
        os.makedirs(args.dataset_folder, exist_ok=True)

    extractPath = os.path.join(args.dataset_folder, "full_sharp")

    trainPath = os.path.join(args.dataset_folder, "train")
    testPath = os.path.join(args.dataset_folder, "test")

    trainPath_blur = os.path.join(args.dataset_folder, "train_blur")
    testPath_blur = os.path.join(args.dataset_folder, "test_blur")

    trainPath_list = os.path.join(args.dataset_folder, "train_list")
    testPath_list = os.path.join(args.dataset_folder, "test_list")


    os.makedirs(extractPath, exist_ok=True)
    os.makedirs(trainPath, exist_ok=True)
    os.makedirs(testPath, exist_ok=True)
    os.makedirs(trainPath_list, exist_ok=True)
    os.makedirs(testPath_list, exist_ok=True)
    os.makedirs(trainPath_blur, exist_ok=True)
    os.makedirs(testPath_blur, exist_ok=True)

    if (args.dataset == "gopro240fps_blur"):
        f = open('/DATA/wangshen_data/CODES/low-lit-enhance/data_scripts/gopro240/gopro_test_list.txt', "r" )
        if debug == True:
            videos = [f.read().split('\n')[0]]
        else:
            videos = f.read().split('\n')

        for video in videos:
            print(video)
            create_clips_overlap([video], extractPath, testPath, testPath_blur, testPath_list)
            # pass


        if args.enable_train == 1:
            print("train")
            f = open('/DATA/wangshen_data/CODES/low-lit-enhance/data_scripts/gopro240/gopro_train_list.txt', "r")
            videos = f.read().split('\n')
            if debug == True:
                videos = [videos[0]]

            for video in videos:
                print(video)
                create_clips_overlap([video], extractPath, trainPath, trainPath_blur, trainPath_list)
                # pass


    if delte_extract == True:
        rmtree(extractPath)


main()
