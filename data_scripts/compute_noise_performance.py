"""
   This script computes the noise input psnr and ssim of each test set.
"""
import os
from skimage.measure import compare_ssim, compare_psnr
from scipy.misc import imread, imsave, imshow, imresize, imsave


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


DO_GO = True

Output_PATH = "/DATA/wangshen_data/ShortLongDataset/Combined_Dataset"
GO_Other_DATA = "/DATA/wangshen_data/CODES/low-lit-enhance/results/VBM4d_nonbline_nonclip"
GO_Other_GT = Output_PATH + '/'  + "test_sharp"
IMG_LIST = Output_PATH + '/' + "test_list"

print("We check the our blurry inputs using the test dataset to check psnr and ssim!")


def test():
    total_run_time = AverageMeter()

    if DO_GO:

        subdir = sorted(os.listdir(GO_Other_DATA))  # folder 0 1 2 3...

        psnr_total = AverageMeter()
        ssim_total = AverageMeter()

        sum_psnr = 0

        for dir in subdir:

            # if dir in already:
            #     continue

            psnr_total.reset()

            img_list = os.path.join(IMG_LIST, dir + '_im_list.txt')

            if not os.path.exists(img_list):
                continue

            f = open(img_list, "r")
            subfolders = f.read().split('\n')

            for index, its in enumerate(subfolders):
                subfolder, _ = its.split('/')

                b1 = os.path.join(GO_Other_DATA, dir, subfolder, '00011.png')
                gt1 = os.path.join(GO_Other_GT, dir, subfolder, '00011.png')
    

                # try:
                gt1_img = imread(gt1)
                b1_img = imread(b1)

                if not (b1_img.shape == gt1_img.shape):
                    print('crop')
                    [H,W,C]=gt1_img.shape
                    if (H==1080) and (W==1920):
                        w = 1280
                        h = 1080
                        gt1_img=gt1_img[(int(H/2)-int(h/2)):(int(H/2)+int(h/2)),(int(W/2)-int(w/2)):(int(W/2)+int(w/2)),:]
                    # except:

                try:
                    psnr_1 = compare_psnr(b1_img, gt1_img)
                except:
                    print(gt1)

                psnr = psnr_1
                pstring = "PSNR : {} ".format(b1) + str(round(psnr, 4))
                print(pstring)
                print(pstring, file=open(os.path.join(GO_Other_DATA, "statis_dir.txt"), "a"))

                psnr_total.update(psnr, 1)

            pstring = "The results for dir:" + dir
            print(pstring)
            print(pstring, file=open(os.path.join(GO_Other_DATA, "statis_dir.txt"), "a"))
            # end for folders
            pstring = "Avg PSNR " + str(psnr_total.avg)
            print(pstring)
            print(pstring, file=open(os.path.join(GO_Other_DATA, "statis_dir.txt"), "a"))

            sum_psnr = sum_psnr + psnr_total.avg

        pstring = "DATASET Avg PSNR " + str(sum_psnr/14.0)
        print(pstring)
        print(pstring, file=open(os.path.join(GO_Other_DATA, "statis_dir.txt"), "a"))


if __name__ == '__main__':
    test()
