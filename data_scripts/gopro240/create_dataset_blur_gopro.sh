#!/usr/bin/env bash

# 310 server
# python create_dataset_blur_gopro.py \
#     --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
#     --dataset gopro240fps_blur \
#     --enable_train 1 \
#     --dataset_folder /DATA/wangshen_data/ShortLongDataset/Gopro240


# 410 server
# python create_dataset_blur_gopro.py \
#     --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
#     --dataset gopro240fps_blur \
#     --enable_train 1 \
#     --dataset_folder /DATA/wangshen_data/ShortLongDataset/Gopro240

python create_dataset_blur_gopro_ln.py \
    --ffmpeg_dir /home/shenwang/Software/ffmpeg-git-amd64-static/ffmpeg-git-20190701-amd64-static \
    --dataset gopro240fps_blur \
    --enable_train 1 \
    --dataset_folder /DATA/wangshen_data/ShortLongDataset/Gopro240


    