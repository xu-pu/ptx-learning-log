#!/bin/env python2.7

SOCCER_ORIGINAL = 'soccer-original.jpg'

import numpy as np
import cv2

def read_image():
    return cv2.imread(SOCCER_ORIGINAL)
#    return cv2.imread(SOCCER_ORIGINAL, 0)

def pixel_manipulation():
    img = read_image()

    # bad way to set/get single pixel, better for ragion
    print(img[10,10]) # BGR point
    print(img[10,10, 0]) # blue only
    img[10,10] = [0,0,0] # set

    # better way for single pixel
    img.item(10, 10, 0)
    img.itemset((10, 10, 0), 255)

def region_manipulation():
    img = read_image()
    
    ball = img[280:340, 330:390]
    img[180:240, 230:290] = ball
    
    cv2.imwrite('pixel-after.jpg', img)

def image_info():
    img = read_image()
    print(img.shape)
    print(img.size)
    print(img.dtype)

def split_image():
    img = read_image()
    b,g,r = cv2.split(img)

    cv2.imwrite('color-split-r.jpg', r)
    cv2.imwrite('color-split-g.jpg', g)
    cv2.imwrite('color-split-b.jpg', b)


if __name__ == '__main__':
    pass
