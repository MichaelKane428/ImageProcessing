#!python2
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

# Task to Complete.






# Opening an image from a file:
I = cv2.imread("image.jpg")

# Opening an image using a File Open dialog:
# f = easygui.fileopenbox()
# I = cv2.imread(f)


# Writing an image:
# cv2.imwrite("image.jpg",I)

# Converting to different colour spaces:
# RGB = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
# HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# YUV = cv2.cvtColor(I, cv2.COLOR_BGR2YUV)
# G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

#Showing an image on the screen (OpenCV):
# cv2.imshow("RGB", RGB)
# cv2.imshow("HSV", HSV)
# cv2.imshow("YUV", YUV)
# cv2.imshow("Greyscale", G)
# cv2.imshow("BGR", I)
# key = cv2.waitKey(0)

# Showing an image on the screen (MatPlotLib):
# I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
# plt.imshow(I) 
# plt.show() 

# Keeping a copy:
# Original = I.copy() 

# # Drawing a line:
#cv2.line(img = I, pt1 = (10,10), pt2 = (50,50), color = (255,255,255), thickness = 5) 
# # Drawing a circle:
#cv2.circle(img = I, center = (100,100), radius = 50, color = (0,0,255), thickness = -1)

# # Drawing a rectangle:
#cv2.rectangle(img = I, pt1 = (100,100), pt2 = (150,150), color = (255,0,255), thickness = 10)

# # Accessing a pixel's value:
# B = I[100,100,2]
# BGR = I[100,100]
# print B
# print BGR

# Setting a pixel's value:
# I[166,6,0] = 0
# cv2.imwrite("imagetest.jpg",I)

# Using the colon operator:
# I[100:130,140:170] = (255,0,0)
# cv2.imshow("image", I)
# key = cv2.waitKey(0)

# H = HSV[:,:,0]
# cv2.imshow("image", H)
# key = cv2.waitKey(0)

#cv2.imshow("image", I)

#key = cv2.waitKey(0)

# Capturing user input:
# def draw(event,x,y,flags,param): 
	# if event == cv2.EVENT_LBUTTONDOWN: 
		# cv2.circle(img = I, center = (x,y),radius = 5, color = (255,255,255), thickness = -1) 
		# cv2.imshow("image", I) 
			
# cv2.namedWindow("image") 
# cv2.setMouseCallback("image", draw) 
# cv2.imshow("image", I)
# key = cv2.waitKey(0)