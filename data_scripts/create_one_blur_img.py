from scipy.ndimage import imread
from scipy.misc import imsave
import os
        

base_path = '/DATA/wangshen_data/ShortLongDataset/Adobe240/train/IMG_0037/00202'
save_path = '/DATA/wangshen_data/ShortLongDataset/Adobe240/train_blur/IMG_0037/00202'
img_list_2 = [12,13,14,15,16,17,18,19,20]


sum = 0.0
for it in img_list_2:
    image_name = '{:05d}.png'.format(it)
    sum = sum + imread(os.path.join(base_path, image_name)).astype("float32")
sum = sum / float(len(img_list_2))
sum = sum.astype("uint8")
imsave(os.path.join(save_path, '00016.png'), sum)