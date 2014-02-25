#!/bin/env python2.7

import numpy as np
import cv2

IMAGE_1 = 'image-1.png'
IMAGE_2 = 'image-2.png'

img1 = cv2.imread(IMAGE_1)
img2 = cv2.imread(IMAGE_2)

def add_images():
    added = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
    cv2.imwrite('added.jpg', added)

def image_mask():
#    roi = img1[0:rows, 0:cols ]
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 50, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    cv2.imwrite('mask.jpg', mask)
    cv2.imwrite('mask-inverse.jpg', mask_inv)

    cv2.imwrite('test-bitwise-and.jpg', cv2.bitwise_and(img1, img1, mask=mask_inv))

    # img1_bg = cv2.bitwise_and(img1,img1,mask = mask_inv)
    # img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    # dst = cv2.add(img1_bg,img2_fg)
    # img1[0:rows, 0:cols ] = dst

    
if __name__ == '__main__':
    pass
