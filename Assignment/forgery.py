#!python2

######################################################
#
#	(C) Michael Kane 2017
#
#	Student No: C14402048
#	Course: DT211C
# 	Date: 29/09/2017
#
#	Title: Master Forgery Assignment.
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
boss = cv2.imread("boss.bmp")
trump = cv2.imread("Trump.jpg")
signature = cv2.imread("signatue.jpg")

height, width, channels = boss.shape
size = (width, height)
size = str(size).replace('L','')
signature = cv2.resize(signature, size)

G = cv2.cvtColor(boss, cv2.COLOR_BGR2GRAY)
#G = cv2.cvtColor(trump, cv2.COLOR_BGR2GRAY)

B = cv2.adaptiveThreshold(G, maxValue = 255,
			adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
			thresholdType = cv2.THRESH_BINARY,
			blockSize = 15,C = 10)
# B = cv2.inRange(boss,rangeLower,rangeHigher)
ROI1 = cv2.bitwise_and(boss,boss,mask=B)

B2 = cv2.bitwise_not(B)
ROI2 = cv2.bitwise_and(signature,signature,mask=B2)

ROI = ROI1 + ROI2

while True:
	# Showing an image on the screen (OpenCV):
	cv2.imshow("boss", ROI)
	key = cv2.waitKey(0)

	# if the 'r' key is pressed, reset the image:
	# if key == ord("r"):
		# I = Original.copy()

	# if the 'q' key is pressed, quit:
	if key == ord("q"):
		break

