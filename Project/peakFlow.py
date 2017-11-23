"""
	Name:		Elizabeth Govan, Michael Kane, David McCahill, Dara Marshall.
	Course:		DT211C/4
	StartDate:	28/08/17
	
	Title: Peak flow meter value detection.
	
	Introduction: 
	1. Segment the red and yellow parts of the image.
	2. Find all the contours in the image, and return the largest contour.
	3. Using the Largest contour find the red pointer inside the image.
	4. Crop a static areas around the image to capture the value the pointer is on.
	5. Use OCR on the newly cropped image to find return the number value of the pointer.
	
	step-by-step:
	1. Select an image of a red/yellow peakFlow meter. This program will not work with other color varients of the peakFlow meter.
	2. Use the inrange function to find the yellow and red parts of an image.
	3. Use a bitwise or to create a combined mask of red and yellow.
	4. Find the contours of the new mask using 
		shape = cv2.getStructuringElement(cv2.MORPH_RECT,(30,30))
		contourMask = cv2.morphologyEx(B,cv2.MORPH_CLOSE,shape)
		alteredImage = cv2.bitwise_and(image,image,mask=contourMask)
		contourMask,contours,_ = cv2.findContours(contourMask,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
	5. Find the largest contour and crop it with the following:
		areas = [cv2.contourArea(contour) for contour in contours]
		maxIndex = np.argmax(areas)
		largestContour = contours[maxIndex]
		x,y,width,height = cv2.boundingRect(largestContour)
		croppedImage = alteredImage[y:y+200,x:x+200]
	6. Find the Red pointer in the new cropped image. Crop a area around the image to find the pointer value.
		points = np.argwhere(croppedRed==255)
		points = np.fliplr(points)
		x, y, width, height = cv2.boundingRect(points)
		x, y, width, height = x, y, width+50, height+100
		croppedColorImage = croppedImage[y:y+height,x:x+width]

	Give an Overview:
	The purpose of this program is to find the current value on a peak flow meter, 
	record it an display the value to the user.
	
	Comment on experiments:

	Comment on performance:

	References:
	https://docs.opencv.org/3.2.0/d4/d73/tutorial_py_contours_begin.html
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
		B = cv2.bitwise_or(B1,B2)
		
		#Find all contours.
		shape = cv2.getStructuringElement(cv2.MORPH_RECT,(30,30))
		contourMask = cv2.morphologyEx(B,cv2.MORPH_CLOSE,shape)
		alteredImage = cv2.bitwise_and(image,image,mask=contourMask)
		contourMask,contours,_ = cv2.findContours(contourMask,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
		#test = cv2.drawContours(image, contours, -1, (0,255,0), 3)
		
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
		croppedImage = alteredImage[y:y+200,x:x+200]
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