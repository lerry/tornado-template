#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-05 15:19
'''
import _envi

import os
import Image
from config import img_type


def scan_folder(dir_path):
    from models.main import Dir, Img
    dir_list = []
    img_list = []
    for i in os.listdir(dir_path):
        full_path = os.path.join(dir_path, i)
        if os.path.isfile(full_path) and full_path.split('.')[-1] in img_type:
            img_list.append(Img(full_path))
        elif os.path.isdir(full_path):
            dir_list.append(Dir(full_path))
    return dir_list, img_list

def resize_img(img_path, save_path, size=[640,480], quality=87):
    if len(size) == 1:
        return cut_img(img_path, save_path, size, quality)
    img = Image.open(img_path)
    img.thumbnail(size)
    img.save(save_path, quality=quality)

def cut_img(img_path, save_path, size=[270], quality=87):
    img = Image.open(img_path)
    w, h = img.size
    side_len = min(w, h)
    offset = (max(w, h) - side_len)/2
    if w > h:
        _size = [offset, 0, side_len+offset, side_len] 
    elif w < h:
        _size = [0, offset, side_len, side_len+offset]
    else:
        _size = [0, 0, w, h]
    img = img.crop(_size)
    img = img.resize(size*2, Image.ANTIALIAS)
    img.save(save_path, quality=quality)
    
            
if __name__ == '__main__':
    #print scan_folder('static')
    cut_img('/home/lerry/My-Photo-Lib/static/1.jpg','/home/lerry/My-Photo-Lib/static/3.jpg')
