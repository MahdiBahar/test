# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 12:29:02 2023

@author: ASUS
"""
## import part

import imageio

#opencv
import cv2 as cv

#scikit image
import skimage

import matplotlib.pyplot as plt

import numpy as np

#pilow
from PIL import Image


#reading image

img_one = cv.imread(r'dataset/images/b.jpg')
print('shape of image one: ' , img_one.shape)

#print(img_one)

plt.imshow(img_one)
plt.title('Image1')
plt.axis('off')

#pillow 

img_one_pil = Image.open(r'dataset/images/b.jpg')
plt.imshow(img_one_pil)
plt.title('Image1 pil')
plt.axis('off')

#color space conversion

img_2_cv = cv.imread(r'dataset/images/b.jpg')
img_2_cv_RGB = cv.cvtColor(img_2_cv,cv.COLOR_RGB2BGR)
plt.imshow(img_2_cv_RGB)


#Gray
img_two_cv_gray = cv.imread(r'dataset/images/b.jpg',0)
plt.imshow(img_two_cv_gray)
print('shape of gray image',img_two_cv_gray.shape)

#color
img_two_cv_color = cv.imread(r'dataset/images/b.jpg',1)
plt.imshow(img_two_cv_color)
print('shape of color image',img_two_cv_color.shape)

#unchange
img_two_cv_unchange = cv.imread(r'dataset/images/b.jpg',-1)
plt.imshow(img_two_cv_unchange)
print('shape of unchange image',img_two_cv_unchange.shape)


#color to Gray 
img_two_cv = cv.imread(r'dataset/images/b.jpg')
img_2_cv_gray = cv.cvtColor(img_two_cv,cv.COLOR_RGB2GRAY)
cv.imshow('image cv 2 gray',img_2_cv_gray)
cv.waitKey(0)

#color image channnels

img_channels = cv.imread(r'dataset/images/b.jpg')

#bgr
blue_ch = img_channels[:,:,0]
green_ch = img_channels[:,:,1]
red_ch = img_channels[:,:,2]

plt.subplot(2,2,1)
plt.imshow(img_channels)
plt.title("orginal image")
plt.axis('off')


plt.subplot(2,2,2)
plt.imshow(blue_ch)
plt.title("blue ch")
plt.axis('off')



plt.subplot(2,2,3)
plt.imshow(green_ch)
plt.title("green ch")
plt.axis('off')
 

plt.subplot(2,2,4)
plt.imshow(red_ch)
plt.title("red ch")
plt.axis('off')





