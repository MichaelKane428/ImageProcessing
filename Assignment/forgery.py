#!python2
"""
	(C) Michael Kane 2017

	Student No: C14402048
	Course: DT211C
	Date: 29/09/2017

	Title: Master Forgery Assignment.

	Introduction:
	1. Clean Boss.bmp to give a more convincing and usable signature for your forged documents. 
    2. Make sure the system cleans the whole picture and not just the signature.
    Challenge : Find, isolate and clean the signature pictured in 'Trump.jpg'

	Step-by-step:
	1. Open a signature of your choice.
	2. Convert the image to its grayscale version.
	3. Find the area where the signature is located using.
	4. 
	5. 
	6. 
	
	Give an overview:
	
	Comment on experiments:
	
	
	References: 
	Convert References to harvard style.
	1. https://stackoverflow.com/questions/44383209/how-to-detect-edge-and-crop-an-image-in-python
	2. https://stackoverflow.com/questions/4337902/how-to-fill-opencv-image-with-one-solid-color
	
"""


# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class forgery():
	def getImage(self):
		#Opening an image from a file:
		print("Please Select a Signature you wish to forge:")
		file = easygui.fileopenbox()
		image = cv2.imread(file)
		forged_image = self.signature(image)

		while True:
			# Showing an image on the screen (OpenCV):
			cv2.imshow("boss", forged_image)
			key = cv2.waitKey(0)

			# if the 'r' key is pressed, reset the image:
			# if key == ord("r"):
				# I = Original.copy()

			# if the 'q' key is pressed, quit:
			if key == ord("q"):
				break
		
	def signature(self, image):
		# Create a grayscale mask for the signature. 
		grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		grayScaleMask = cv2.adaptiveThreshold(grayScale, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 11,C = 15)
		
		# The next six lines of code are from reference Number 1.
		# Crop the area where the signature is located. 
		points = np.argwhere(grayScaleMask==0)
		points = np.fliplr(points)
		x, y, width, height = cv2.boundingRect(points)
		x, y, width, height = x-50, y-50, width+100, height+70
		croppedColorImage = image[y:y+height,x:x+width]
		croppedGrayScaleImage = grayScaleMask[y:y+height,x:x+width]
		
		# Extracted signature.
		reverseSignature = cv2.bitwise_not(croppedGrayScaleImage)
		regionOfInterestOne = cv2.bitwise_and(croppedColorImage,croppedColorImage,mask=reverseSignature)
		
		# Line 101 and 102 are referenced by reference Number 2.
		# Apply the extracted Signature to the background.
		reverseBackground = cv2.bitwise_not(reverseSignature)
		height, width = croppedGrayScaleImage.shape
		background = np.zeros((height, width, 3), np.uint8)
		background[:] = (255,255,255)
		regionOfInterestTwo = cv2.bitwise_and(background,background,mask=reverseBackground)
		forged_signature = regionOfInterestOne + regionOfInterestTwo
		
		# Create an image of the signature.
		cv2.imwrite('forgedSignature.jpg', forged_signature)
		return forged_signature

if __name__ == "__main__":
	myBool = True
	forged_signature = forgery()
	forged_signature.getImage()
	