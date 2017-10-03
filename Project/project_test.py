################################################################################################################################
#	Name:		Elizabeth Govan
#	Student 	Number: C14307346
#	Course:		DT211C/4
#	StartDate:	28/08/17
#	FinishDate: 
#	
#	Title: Project testing
#	Introduction: 
#		Describe the algorithm here
#		preferably use a systematic approach
#		e.g step-by-step
#		Give an Overview
#		Comment on experiments
#		use references (Harvard Referencing System) - not weblink
#		Comment on performance
# 	
################################################################################################################################

import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

f = easygui.fileopenbox()
I = cv2.imread(f)

# RED
RangeLower = (0,0,150)
RangeUpper = (100,100,255)
B2 = cv2.inRange(I, RangeLower, RangeUpper)

# BLACk
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
B3 = cv2.adaptiveThreshold(G, maxValue = 255,
adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
thresholdType = cv2.THRESH_BINARY,
blockSize = 9,C = 20)
B3 = 255-B3

shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
ROI = cv2.bitwise_or(B2,B3)
eroded_mask = cv2.erode(ROI,shape)
boundary = ROI - eroded_mask

#ROI = cv2.bitwise_and(I,I,mask=boundary)
#TEST = cv2.morphologyEx(NEWB,cv2.MORPH_CLOSE,shape)
#ROI = cv2.morphologyEx(TEST,cv2.MORPH_OPEN,shape)
cv2.imshow("NEW",ROI)
key = cv2.waitKey(0)

#YELLOW
# RangeLower = (0,90,100)
# RangeUpper = (255,200,200)
#RangeLower = (0,90,100)
#RangeUpper = (45,150,255)
#B1 = cv2.inRange(I, RangeLower, RangeUpper)
# cv2.imwrite("bwPeakFlow.jpg",B1)

#cv2.imshow("image",B1)
#key = cv2.waitKey(0) 

# B = cv2.bitwise_or(B1,B2)
# cv2.imshow("image",B)
# key = cv2.waitKey(0)
# ROI = cv2.bitwise_and(I,I,mask=B)
#ROI = 255-ROI
# shape = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
# NewMask = cv2.morphologyEx(ROI,cv2.MORPH_CLOSE,shape)
# cv2.imshow("image",NewMask)
# key = cv2.waitKey(0)