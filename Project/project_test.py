################################################################################################################################
#	Name:		Michael Kane
#	Student 	Number: C14402048
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


class peakFlow():
	"""
	Purpose of function:
	Allow portablity of the peakFlow code
	
	Example Function:
	instance = peakFlow()
	
	Args:
		None
	return:
		None
	"""
	def findRedMask(self, image):
		# RED
		RangeLower = (0,0,150)
		RangeUpper = (100,100,255)
		redMask = cv2.inRange(image, RangeLower, RangeUpper)
		return redMask
		
	def findBlackMask(self, image):
		# BLACk
		greyScaleMask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		blackMask = cv2.adaptiveThreshold(greyScaleMask, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 9,C = 20)
		
		blackMask = 255-blackMask
		
		return blackMask, greyScaleMask
	
	def getImage(self):
		"""
		Purpose of function:
		Allow a user to select an image.
		
		Example Function:
		instance.getImage()
		
		Args:
			None
		return:
			None
		"""
		try:
			#Opening an image from a file:
			print("Please Select a image:")
			file = easygui.fileopenbox()
			image = cv2.imread(file)
			
			redMask = self.findRedMask(image)

			blackMask, greyScaleMask = self.findBlackMask(image)
			
			ROI = cv2.bitwise_or(redMask, blackMask)

		except:
			print("User failed to select an image.")
		while True:
			# Showing an image on the screen (OpenCV):
			cv2.imshow("Reading", ROI)
			key = cv2.waitKey(0)

			# if the 'q' key is pressed, quit:
			if key == ord("q"):
				break

if __name__ == "__main__":
	reading = peakFlow()
	reading.getImage()
