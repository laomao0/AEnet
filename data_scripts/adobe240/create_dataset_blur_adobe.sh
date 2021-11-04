#!/usr/bin/env bash

# 310 server
# python create_dataset_blur_adobe.py \
#     --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
#     --dataset adobe240fps_blur \
#     --enable_train 1 \
#     --dataset_folder /DATA/wangshen_data/ShortLongDataset/Adobe240 \
#     --videos_folder  /DATA/wangshen_data/Adobe_240fps_dataset/Adobe_240fps_original_high_fps_videos

# 410 server
# python create_dataset_blur_adobe.py \
#     --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
#     --dataset adobe240fps_blur \
#     --enable_train 1 \
#     --dataset_folder /DATA/wangshen_data/ShortLongDataset/Adobe240 \
#     --videos_folder  /DATA/wangshen_data/Adobe_240fps_dataset/Adobe_240fps_original_high_fps_videos

python create_dataset_blur_adobe_ln.py \
    --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
    --dataset adobe240fps_blur \
    --enable_train 1 \
    --dataset_folder /DATA/wangshen_data/ShortLongDataset/Adobe240 \
    --videos_folder  /DATA/wangshen_data/Adobe_240fps_dataset/Adobe_240fps_original_high_fps_videos