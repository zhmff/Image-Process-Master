#!/usr/bin/env python3
import os
from PIL import Image

"""
file:           /Users/zhangmengfeifei/Desktop/self_learning/test_files/img_test/png
output_dir:     /Users/zhangmengfeifei/Desktop/self_learning/test_files/img_test/
log:            /Users/zhangmengfeifei/Desktop/self_learning/test_files/log.txt


Unsupported file types: 
.jpg
.raw

"""
# TODO ADD function to judge if the processing file is a dir. If so, ignore it.


def open_image(image_path):
    img = Image.open(image_path)
    print(img)


if __name__ == '__main__':
    path = "/Users/zhangmengfeifei/Desktop/self_learning/test_files/img_test/"
    parent_path = path + os.listdir(path + os.sep)[0] + os.sep
    images = os.listdir(parent_path)
    for image in images:
        image_file = parent_path + image
        open_image(image_file)
