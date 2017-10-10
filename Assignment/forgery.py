#!python2
"""
	(C) Michael Kane 2017

	Student No: C14402048
	Course: DT211C
	Date: 29/09/2017

	Title: Master Forgery Assignment.

	Introduction:
	1. Open image Wartime.jpg;
	2. View its histogram alongside the image;
	3. Use histogram equalisation to improve its contrast;
	4. View the new histogram alongside the new image.
	Advanced Task:
	Try this on a poor quality colour image.

	Step-by-step:
	1. Open an image of your choice.
	2. Convert the image to its grayscale version.
	3. Unravel the image from its matrix and get the pixel values using G.ravel() where G is the grayscale image.
	4. Plot the Histogram using plot.hist(Values,bins=256,range=[0,256]).
	5. Equalise the Histogram using H = cv2.equalizeHist(G) where G is the grayscale image.
	6. Show the Hisograms and the images.
	
	Give an overview:
	
	Comment on experiments:
	For colour images there seems to be some trouble equalizing the Histograms, will do more research into this.
	
	Use References: 
	
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
		#print("Please Select a Signature you wish to forge:")
		#file = easygui.fileopenbox()
		#image = cv2.imread(file)
		#image = cv2.imread("Boss.bmp")
		image = cv2.imread("redSignature.png")
		#image = cv2.imread("Trump.jpg")
		form = cv2.imread("form.png")
		
		#print("Please Select an image to place the signature on:")
		#file2 = easygui.fileopenbox()
		#form = cv2.imread(file2)
		forged_image = self.signature(image, form)
		

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
		
	def signature(self, image, form):
		grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		grayScaleMask = cv2.adaptiveThreshold(grayScale, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 5,C = 10)
		
		# https://stackoverflow.com/questions/44383209/how-to-detect-edge-and-crop-an-image-in-python
		# Reference this correctly at top of page.
		points = np.argwhere(grayScaleMask==0)
		points = np.fliplr(points)
		x, y, width, height = cv2.boundingRect(points)
		x, y, width, height = x-50, y-50, width+100, height+70
		croppedColorImage = image[y:y+height,x:x+width]
		croppedGrayScaleImage = grayScaleMask[y:y+height,x:x+width]
		
		
		reverseMask = cv2.bitwise_not(croppedGrayScaleImage)
		ROI1 = cv2.bitwise_and(croppedColorImage,croppedColorImage,mask=reverseMask)
		
		reverseMask2 = cv2.bitwise_not(reverseMask)
		
		height, width = croppedGrayScaleImage.shape
		form = cv2.resize(form,(width,height))
		ROI2 = cv2.bitwise_and(form,form,mask=reverseMask2)
		
		forged_signature = ROI1 + ROI2
		
		
		cv2.imwrite('forgedSignature.jpg', forged_signature)
		return forged_signature

if __name__ == "__main__":
	myBool = True
	forged_signature = forgery()
	forged_signature.getImage()
	