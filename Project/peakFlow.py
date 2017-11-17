"""
	Name:		Elizabeth Govan
	Student 	Number: C14307346
	Course:		DT211C/4
	StartDate:	28/08/17
	FinishDate: 
	
	Title: Project testing
	Introduction: 
		Describe the algorithm here
		preferably use a systematic approach
		e.g step-by-step
		Give an Overview
		Comment on experiments
		use references (Harvard Referencing System) - not weblink
		Comment on performance
		

      [3] https://stackoverflow.com/questions/44588279/find-and-draw-the-largest-contour-in-opencv-on-a-specific-color-python
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class peakFlow():
	def start(self):
		#Find the red and yellow areas.
		image = self.get_image()
		B1 = self.find_yellow(image)
		B2 = self.find_red(image)
		#B3 = self.find_black(image) 
		
		#RED = cv2.bitwise_and(image,image,mask=B2)
		B = cv2.bitwise_or(B1,B2)
		#ROI = cv2.bitwise_and(image,image,mask=B)
		
		#Find all contours.
		shape = cv2.getStructuringElement(cv2.MORPH_RECT,(30,30))
		contourMask = cv2.morphologyEx(B,cv2.MORPH_CLOSE,shape)
		alteredImage = cv2.bitwise_and(image,image,mask=contourMask)
		contourMask,contours,_ = cv2.findContours(contourMask,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
		
		croppedImage = self.cropLargestContour(alteredImage, contours)
		
		croppedRed = self.find_red(croppedImage)
		
		ROI = self.cropROI(croppedImage, croppedRed)
		
		cv2.imshow("NEW", ROI)
		key = cv2.waitKey(0)

	def cropROI(self, croppedImage, croppedRed):
		points = np.argwhere(croppedRed==255)
		points = np.fliplr(points)
		x, y, width, height = cv2.boundingRect(points)
		x, y, width, height = x, y, width+50, height+100
		croppedColorImage = croppedImage[y:y+height,x:x+width]
		return croppedColorImage
	
	def cropLargestContour(self, alteredImage, contours):
		#Code Taken from Source Number [3]
		#Crop the largestContour.
		areas = [cv2.contourArea(contour) for contour in contours]
		maxIndex = np.argmax(areas)
		largestContour = contours[maxIndex]
		x,y,width,height = cv2.boundingRect(largestContour)
		croppedImage = alteredImage[y:y+height,x:x+width]
		return croppedImage
	
	def get_image(self):
		f = easygui.fileopenbox()
		image = cv2.imread(f)
		return image

	def find_yellow(self,image):
		RangeLower = (0,75,75)
		RangeUpper = (45,150,255)
		B1 = cv2.inRange(image, RangeLower, RangeUpper)
		

		return B1
	
	def find_red(self,image):
		# RED
		RangeLower = (0,0,150)
		RangeUpper = (100,100,255)
		B2 = cv2.inRange(image, RangeLower, RangeUpper)
		return B2


	def find_black(self,image):
		# BLACk
		G = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		B3 = cv2.adaptiveThreshold(G, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 5,C = 11)
		
		return B3
		
if __name__ =="__main__":
	instance = peakFlow()
	instance.start()