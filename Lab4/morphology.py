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
Trump = cv2.imread("Trump.jpg")
cow = cv2.imread("cow.jpg")

# Keeping a copy:
Original = Trump.copy()

HSVTrump = cv2.cvtColor(Trump, cv2.COLOR_BGR2HSV)

rangeLower = (0, 48, 80)
rangeHigher = (20, 255, 255)

shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,50))
B = cv2.inRange(HSVTrump,rangeLower,rangeHigher)
open = cv2.morphologyEx(B,cv2.MORPH_OPEN,shape)
closed = cv2.morphologyEx(open,cv2.MORPH_CLOSE,shape)
ROI1 = cv2.bitwise_and(Trump,Trump,mask=closed)

B2 = cv2.bitwise_not(closed)
ROI2 = cv2.bitwise_and(cow,cow,mask=B2)

ROI = ROI1 + ROI2



# A handy way to use the waitkey....

while True:
	cv2.imshow("Trump", ROI)
	key = cv2.waitKey(0)

	# if the 'r' key is pressed, reset the image:
	if key == ord("r"):
		I = Original.copy()

	# if the 'q' key is pressed, quit:
	elif key == ord("q"):
		break

