#!python2

"""
	(C) Michael Kane 2017

	Student No: C14402048
	Course: DT211C
	Date: 06/10/2017

	Title: Lab 4 Histograms.

	Introduction:
	1. Open image “Wartime.jpg”;
	2. View its histogram alongside the image;
	3. Use histogram equalisation to improve its contrast;
	4. View the new histogram alongside the new image.
	Advanced Task:
	Try this on a poor quality colour image.

	Step-by-step:
	1. Open an image of your choice.
	2. Convert the image to its grayscale version.
	3. Unravel the image from its matrix and get the pixel values using G.ravel() where G is the grayscale image.
	4. Plot the Histogram using plot.hist(Values,bins=256,range=[0,256]).
	5. Equalise the Histogram using H = cv2.equalizeHist(G) where G is the grayscale image.
	6. Show the Hisograms and the images.
	
	Give an overview:
	
	Comment on experiments:
	For colour images there seems to be some trouble equalizing the Histograms, will do more research into this.
	
	Use References: 
	
"""

# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

# Opening an image from a file:
color = cv2.imread("color.jpg")
wartime = cv2.imread("wartime.jpg")

RGB = cv2.cvtColor(color, cv2.COLOR_BGR2RGB)
G = cv2.cvtColor(wartime, cv2.COLOR_BGR2GRAY)
Values = G.ravel()
plt.hist(Values,bins=256,range=[0,256])
plt.show()

H = cv2.equalizeHist(G)
Values = H.ravel()
plt.hist(Values,bins=256,range=[0,256])
plt.show()

cv2.imshow("H", H)
key = cv2.waitKey(0)