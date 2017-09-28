#!python2

######################################################
#
#	(C) Michael Kane 2017
#
#	Student No: C14402048
#	Course: DT211C
# 	Date: 22/09/2017
#
#	Title: Lab 2 Task.
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


import numpy as np
import cv2
##from matplotlib import pyplot as plt
##from matplotlib import image as image
import easygui

# Opening an image using a File Open dialog:
f = easygui.fileopenbox()
I = cv2.imread(f)

height, width, channels = I.shape
print height, width

# Capturing user input:
def draw(event,x,y,flags,param): 
	if event == cv2.EVENT_LBUTTONDOWN:
		if y+100 < height and x+100 < width and y-100 > 0 and x-100 > 0:
			print y+100, x+100
			cv2.rectangle(img = I, pt1 = (x+100, y+100), pt2 = (x-100,y-100), color = (0,0,255), thickness = 5)
			I[y-100:y+100, x-100:x+100] = cv2.cvtColor(I[y-100:y+100, x-100:x+100], cv2.COLOR_BGR2YUV)
			cv2.imshow("image", I)
		
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw) 
cv2.imshow("image", I)
key = cv2.waitKey(0)
