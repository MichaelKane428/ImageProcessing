
# Starter Pack for Image Processing

# (C) Dr Jane Courtney 2017

# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

# Opening an image from a file:
# I = cv2.imread("colours.jpg")

# Opening an image using a File Open dialog:
f = easygui.fileopenbox()
I = cv2.imread(f)

# Getting the size of the image:
# size = np.shape(I)

# Capturing an image from a webcam:
# camera = cv2.VideoCapture(0)
# (grabbed, I) = camera.read()

# Video Capture:
# grabbed = True
# while grabbed:
	# (grabbed, I) = camera.read()

	# cv2.imshow("image", I)
	# key = cv2.waitKey(1)

	## if the 'q' key is pressed, quit:
	# if key == ord("q"):
		# break

# camera.release()

# Writing an image:
# cv2.imwrite("image.jpg",I)

# Showing an image on the screen (OpenCV):
cv2.imshow("image", I)
key = cv2.waitKey(0)

# Showing an image on the screen (MatPlotLib):
# I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
# plt.imshow(I) 
# plt.show() 

# Converting to different colour spaces:
# RGB = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
# HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
# YUV = cv2.cvtColor(I, cv2.COLOR_BGR2YUV)
# G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Keeping a copy:
# Original = I.copy() 

# # Drawing a line:
# cv2.line(img = I, pt1 = (200,200), pt2 = (500,600), color = (255,255,255), thickness = 5) 

# # Drawing a circle:
# cv2.circle(img = I, center = (800,400), radius = 50, color = (0,0,255), thickness = -1)

# # Drawing a rectangle:
# cv2.rectangle(img = I, pt1 = (500,100), pt2 = (800,300), color = (255,0,255), thickness = 10)

# # Accessing a pixel's value:
# B = I[400,800,0]
# BGR = I[400,800]
# print B
# print BGR

# Setting a pixel's value:
# I[400,800,0] = 255
# cv2.imshow("image", I)
# key = cv2.waitKey(0)

# I[400,800] = (255,0,0)
# cv2.imshow("image", I)
# key = cv2.waitKey(0)

# Using the colon operator:
# I[390:410,790:810] = (255,0,0)
# cv2.imshow("image", I)
# key = cv2.waitKey(0)

# I[:,:,2] = 0
# cv2.imshow("image", I)
# key = cv2.waitKey(0)

# Capturing user input:
# def draw(event,x,y,flags,param): 
	# if event == cv2.EVENT_LBUTTONDOWN: 
		# cv2.circle(img = I, center = (x,y),radius = 5, color = (255,255,255), thickness = -1) 
		# cv2.imshow("image", I) 
			
# cv2.namedWindow("image") 
# cv2.setMouseCallback("image", draw) 
# cv2.imshow("image", I)
# key = cv2.waitKey(0)

# A handy way to use the waitkey....

# while True:
	# cv2.imshow("image", I)
	# key = cv2.waitKey(0)

	# # if the 'r' key is pressed, reset the image:
	# if key == ord("r"):
		# I = Original.copy()

	# # if the 'q' key is pressed, quit:
	# elif key == ord("q"):
		# break

