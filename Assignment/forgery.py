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
	3. Find the area where the signature is located using np.argwhere(grayScaleMask==0). 
	4. Plot the points of the returned value of np.argwhere using points = np.fliplr(points) then x, y, width, height = cv2.boundingRect(points)
	5. Crop both the grayscale and original image.
	6. Get the ROI of the original image by getting the reverse mask of it then anding itwith itself.
	7. Create a blank background image by getting to shape of the original image, then use np.zeros((height, width, 3), np.uint8) to create the image
	8. Change the background to full white then add the background and ROI together.
	9. Write the image to an image file, return the image and display it.
	
	Give an overview:
	The purpose of this application is to allow a user to input an image of a signature, 
	and recieve an image back with the signature isolated and background completely white.
	
	Comment on experiments:
	1. Tried to get blue signatures to appear clearer, but it seems any blue signature I pass in, unless it has been created in paint appears gray.
	Green signatures dont seem to work very well.
	
	Any signatures I try off the interent dont work as well as they should, I get a 50/50 working ration on the ones I picked.
	
	2. Sucessfully implemented a version which placed the image onto a signed form, the issue was that it was not to scale and would appear squashed.
	This was done by cropping the signature which can be found below, rezising the form and combinging the ROI for the signature and the form.
	
	After completing this however it was revealed that it is not the objective of the assignment so I reverted to a simpler version.
	Link to the git version with the code.
	https://github.com/MichaelKane428/ImageProcessing/commit/736ac1edc6fc626ce3d79d24015580cb994fc487#diff-be144f71162553069eb09260442b8921
	
	
	References: 
	Convert References to harvard style.
	1. Stack Overflow, SO. (2017)How to detect edge and crop an image in Python. 
	Available at: https://stackoverflow.com/questions/44383209/how-to-detect-edge-and-crop-an-image-in-python(12/10/2017)
	2. Stack Overflow, SO. (2017)How to fill OpenCV image with one solid color?.
	Available at: https://stackoverflow.com/questions/4337902/how-to-fill-opencv-image-with-one-solid-color(12/10/2017)
	
"""


# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class forgery():
	"""
	Purpose of function:
	Allow portablity of the forge signature code
	
	Example Function:
	instance = forgery()
	
	Args:
		None
	return:
		None
	"""
	
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
		
		#Opening an image from a file:
		print("Please Select a Signature you wish to forge:")
		file = easygui.fileopenbox()
		image = cv2.imread(file)
		forged_image = self.forgeSignature(image)

		while True:
			# Showing an image on the screen (OpenCV):
			cv2.imshow("boss", forged_image)
			key = cv2.waitKey(0)

			# if the 'q' key is pressed, quit:
			if key == ord("q"):
				break
		
	def forgeSignature(self, image):
		"""
		Purpose of function:
		The purpose of this function is to isolate a signature and place it on a fully white background, 
		then return it to the getImage function to be displayed.
		
		Example Function:
		variable = self.forgeSignature(param1)
		
		Args:
			param1 (numpy.ndarray): This is the first paramter. Which will be an image a user has selected.
		return:
			The return value (numpy.ndarray): This will return a forged version of the original signature.
		"""
		
		# Create a grayscale mask for the signature. 
		grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		grayScaleHistogram = cv2.equalizeHist(grayScale)
		grayScaleMask = cv2.adaptiveThreshold(grayScaleHistogram, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 11,C = 30)
		
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
		return grayScaleMask

if __name__ == "__main__":
	forged_signature = forgery()
	forged_signature.getImage()
	