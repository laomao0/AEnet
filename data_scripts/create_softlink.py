import os

# modes = ['test', 'train']
modes = ['train']
dataset_name = 'Sony240' #'Adobe240' # or Gopro240 or Sony240
src_path = '/DATA/wangshen_data/ShortLongDataset'
dst_path = '/DATA/wangshen_data/ShortLongDataset/Combined_Dataset'

for mode in modes:
    all_dirs  = os.listdir(os.path.join(src_path, dataset_name, '{}_sharp'.format(mode)))
    for folder in all_dirs:
        #os.system('ln -s {} {}'.format(os.path.join(src_path, dataset_name, '{}_sharp'.format(mode), folder), os.path.join(dst_path, '{}_sharp'.format(mode), folder)))
        os.system('ln -s {} {}'.format(os.path.join(src_path, dataset_name, '{}_blur'.format(mode), folder), os.path.join(dst_path, '{}_blur'.format(mode), folder)))
        # os.system('ln -s {} {}'.format(os.path.join(src_path, dataset_name, 'test_noise', folder), os.path.join(dst_path, 'test_noise', folder)))
        #os.system('ln -s {} {}'.format(os.path.join(src_path, dataset_name, '{}_list'.format(mode), '{}_im_list.txt'.format(folder)), os.path.join(dst_path, '{}_list'.format(mode), '{}_im_list.txt'.format(folder))))