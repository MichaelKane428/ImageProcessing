#!python2

######################################################
#
#	(C) Michael Kane 2017
#
#	Student No: C14402048
#	Course: DT211C
# 	Date: 28/09/2017
#
#	Title: Lab 3 Googly.
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
image = cv2.imread("Googly.jpg")

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold = np.mean(grayscale) + np.std(grayscale)

threshold, B = cv2.threshold(grayscale, thresh = threshold, maxval = 255,
type = cv2.THRESH_BINARY)

# Showing an image on the screen (OpenCV):
cv2.imshow("googly", B)
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

