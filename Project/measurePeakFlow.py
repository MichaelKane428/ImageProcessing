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
#
#       [3] https://stackoverflow.com/questions/44588279/find-and-draw-the-largest-contour-in-opencv-on-a-specific-color-python
# 	
################################################################################################################################

import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class measurePeakFlow():
	def start(self):
		#Find the red and yellow areas.
		I = self.get_image()
		B1 = self.find_yellow(I)
		B2 = self.find_red(I)
		B3 = self.find_black(I) 
		
		RED = cv2.bitwise_and(I,I,mask=B2)
		B = cv2.bitwise_or(B1,B2)
		ROI = cv2.bitwise_and(I,I,mask=B)
		
		#Find all contours.
		shape = cv2.getStructuringElement(cv2.MORPH_RECT,(30,30))
		NewMask = cv2.morphologyEx(B,cv2.MORPH_CLOSE,shape)
		NEW = cv2.bitwise_and(I,I,mask=NewMask)
		NewMask,contours,_ = cv2.findContours(NewMask,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
		
		#Code Taken from Source Number [3]
		#Crop the largestContour.
		areas = [cv2.contourArea(contour) for contour in contours]
		maxIndex = np.argmax(areas)
		largestContour = contours[maxIndex]
		x,y,width,height = cv2.boundingRect(largestContour)
		croppedImage = NEW[y:y+height,x:x+width]
		
		cv2.imshow("NEW", croppedImage)
		key = cv2.waitKey(0)
		
	def get_image(self):

		f = easygui.fileopenbox()
		I = cv2.imread(f)
		return I

	def find_yellow(self,I):
		RangeLower = (0,90,100)
		RangeUpper = (45,150,255)
		B1 = cv2.inRange(I, RangeLower, RangeUpper)
		

		return B1
	
	def find_red(self,I):
		# RED
		RangeLower = (0,0,150)
		RangeUpper = (100,100,255)
		B2 = cv2.inRange(I, RangeLower, RangeUpper)
		return B2


	def find_black(self,I):
		# BLACk
		G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
		B3 = cv2.adaptiveThreshold(G, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 5,C = 11)
		
		return B3
		
if __name__ =="__main__":
	instance = measurePeakFlow()
	instance.start()