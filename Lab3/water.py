#!python2

######################################################
#
#	(C) Michael Kane 2017
#
#	Student No: C14402048
#	Course: DT211C
# 	Date: 29/09/2017
#
#	Title: Lab 3 Water.
#
# 	Introduction:
#	
#	Describe the algorithm here
#	Preferably use a systematic approach
#	e.g. step-by-step
#	or pseudo-code
#	Give an overview
#	Comment on experiments
# 	Use References (Harvard Referencing Standard) - no Web Links


# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui


#Opening an image from a file:
orange = cv2.imread("orange.png")
water = cv2.imread("water.jpg")

rangeLower = (0,0,0)
rangeHigher = (245, 240, 255)

B = cv2.inRange(orange,rangeLower,rangeHigher)
ROI1 = cv2.bitwise_and(orange,orange,mask=B)

B2 = cv2.bitwise_not(B)
ROI2 = cv2.bitwise_and(water,water,mask=B2)

ROI = ROI1 + ROI2


# Showing an image on the screen (OpenCV):
cv2.imshow("orange", ROI)
key = cv2.waitKey(0)


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

