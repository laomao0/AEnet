import os

# modes = ['train']
dataset_name = 'Sony240' #'Adobe240' # or Gopro240 or Sony240
src_path = '/DATA/wangshen_data/ShortLongDataset'
dst_path = '/DATA/wangshen_data/ShortLongDataset/Combined_Dataset'



# for mode in modes:
all_dirs  = os.listdir(os.path.join(src_path, dataset_name, 'full_sharp'))
for folder in all_dirs:
    os.system('ln -s {} {}'.format(os.path.join(src_path, dataset_name, 'full_sharp', folder), os.path.join(dst_path, 'full_sharp', folder)))