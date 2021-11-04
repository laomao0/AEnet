#!/usr/bin/env bash

# on 310 server
# python create_dataset_blur_sony.py \
#     --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
#     --dataset sony240fps_blur \
#     --enable_train 1 \
#     --dataset_folder /DATA/wangshen_data/ShortLongDataset/Sony240 \
#     --videos_folder  /DATA/wangshen_data/Sony240Videos


# on 410 server
# python create_dataset_blur_sony.py \
#     --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
#     --dataset sony240fps_blur \
#     --enable_train 1 \
#     --dataset_folder /DATA/wangshen_data/ShortLongDataset/Sony240 \
#     --videos_folder  /DATA/wangshen_data/JinSloMo/original_high_fps

python create_dataset_blur_sony_ln.py \
    --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
    --dataset sony240fps_blur \
    --enable_train 1 \
    --dataset_folder /DATA/wangshen_data/ShortLongDataset/Sony240 \
    --videos_folder  /DATA/wangshen_data/JinSloMo/original_high_fps