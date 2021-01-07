import cv2
import easygui
import numpy as np
import imageio

import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image





def cartoonify(image):
    originalImage=image
    originalImage-cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)

    if originalImage is None:
        print("Can't find any image, choosea correct file")
        sys.exit()

    Resized1=cv2.resize(originalImage,(960,540))
    #plt.imshow(Resized1,cmap='gray')

    grayScaleImage=cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)
    Resized2=cv2.resize(grayScaleImage,(960,540))
    #plt.imshow(Resized2,cmap='gray')

    smoothGrayScale=cv2.medianBlur(grayScaleImage,5)
    Resized3=cv2.resize(smoothGrayScale,(960,540))
    #plt.imshow(Resized3,cmap='gray')

    getEdge=cv2.adaptiveThreshold(smoothGrayScale,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    Resized4=cv2.resize(getEdge,(960,540))
    #plt.imshow(Resized4,cmap='gray')

    colorImage=cv2.bilateralFilter(originalImage,9,300,300)
    Resized5=cv2.resize(colorImage,(960,540))

    cartoonImage=cv2.bitwise_and(colorImage,colorImage,mask=getEdge)

    Resized6=cv2.resize(cartoonImage,(960,540))
    cv2.imshow('',Resized6)
    cv2.waitKey(0)
    #images=[Resized1,Resized2,Resized3,Resized4,Resized5,Resized6]

img=cv2.imread('flowers.jpg')
cartoonify(img)

    
    
