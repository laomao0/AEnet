import os

dst_path = '/DATA/wangshen_data/ShortLongDataset/Gopro240/full_sharp'
# src_path_train = '/DATA/wangshen_data/GoPro_Large_dataset/GOPRO_Large_all/train_all'
# src_path_test = '/DATA/wangshen_data/GoPro_Large_dataset/GOPRO_Large_all/test_all'

src_path_train = '/DATA/wangshen_data/GOPRO_Large_All/train_all'
src_path_test = '/DATA/wangshen_data/GOPRO_Large_All/test_all'



src = src_path_train


all_dirs = os.listdir(src)

for folder in all_dirs:
    os.system('ln -s {} {}'.format(os.path.join(src, folder), os.path.join(dst_path, folder)))