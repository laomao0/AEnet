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


test_or_train = 'test'  # 'train'  # 'test'
DO_GO = True

Output_PATH = "/DATA/wangshen_data/ShortLongDataset/Combined_Dataset"
GO_Other_DATA = Output_PATH + '/' + test_or_train + "_noise_random"
GO_Other_GT = Output_PATH + '/' + test_or_train + "_sharp"
IMG_LIST = Output_PATH + '/' + test_or_train + "_list"

print("We check the our blurry inputs using the " + test_or_train + " dataset to check psnr and ssim!")

# already = ['2C0094', 'C0041', 'C0058', 'C0072',
#            'C0079', 'C0085', 'GOPR0384_11_00',
#            'GOPR0384_11_05', 'GOPR0385_11_01', 'GOPR0396_11_00']

def test():
    total_run_time = AverageMeter()

    if DO_GO:
        subdir = sorted(os.listdir(GO_Other_DATA))  # folder 0 1 2 3...

        psnr_total = AverageMeter()
        ssim_total = AverageMeter()

        for dir in subdir:

            # if dir in already:
            #     continue

            psnr_total.reset()

            img_list = os.path.join(IMG_LIST, dir + '_im_list.txt')
            f = open(img_list, "r")
            subfolders = f.read().split('\n')

            for index, its in enumerate(subfolders):
                subfolder, _ = its.split('/')

                # blurry
                b1 = os.path.join(GO_Other_DATA, dir, subfolder, '00006.png')
                b2 = os.path.join(GO_Other_DATA, dir, subfolder, '00016.png')

                gt1 = os.path.join(GO_Other_GT, dir, subfolder, '00006.png')
                gt2 = os.path.join(GO_Other_GT, dir, subfolder, '00016.png')

                # try:
                gt1_img = imread(gt1)
                gt2_img = imread(gt2)
                b1_img = imread(b1)
                b2_img = imread(b2)
                # except:

                try:
                    psnr_1 = compare_psnr(b1_img, gt1_img)
                except:
                    print(gt1)

                try:
                    psnr_2 = compare_psnr(b2_img, gt2_img)
                except:
                    print(gt2)

                psnr = (psnr_1 + psnr_2) * 0.5
                pstring = "Noise PSNR : " + str(round(psnr, 4))
                print(pstring)

                psnr_total.update(psnr, 1)

            pstring = "The results for dir:" + dir
            print(pstring)
            print(pstring, file=open(os.path.join(Output_PATH, test_or_train + "_statis_dir.txt"), "a"))
            # end for folders
            pstring = "Avg PSNR " + str(psnr_total.avg)
            print(pstring)
            print(pstring, file=open(os.path.join(Output_PATH, test_or_train + "_statis_dir.txt"), "a"))


if __name__ == '__main__':
    test()
