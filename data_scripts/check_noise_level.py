import os

path = '/DATA/wangshen_data/ShortLongDataset/Combined_Dataset/noise_str.txt'

f = open(path, "r")
subits = f.read().split('\n')

all_level = {}
all_sigmma = {}

for it in subits:
    folder, indx, sigmma, level = it.split('/')
    sigmma = float(sigmma)
    level = float(level)

    if not folder in  all_level:
        all_level[folder] = []
        all_sigmma[folder] = []

    all_level[folder].append(level)
    all_sigmma[folder].append(sigmma)


for folder in all_sigmma:

    level_avg = sum(all_level[folder])/len(all_level[folder])
    sigmma_avg = sum(all_sigmma[folder])/len(all_sigmma[folder])

    print('{}, {}, {}'.format(folder,sigmma_avg,level_avg))


    
