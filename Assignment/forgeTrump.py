#!python2
"""
	(C) Michael Kane 2017

	Student No: C14402048
	Course: DT211C
	Date: 29/09/2017

	Title: Master Forgery Assignment.

	Introduction:
	Challenge : Find, isolate and clean the signature pictured in 'Trump.jpg'

	Step-by-step:
	1. Open a signature of your choice.
	2. Convert the image to its grayscale version.
	3. Equalise the histogram.
	4. Apply the open and close functions to the image.
	5. Call the cropImage function.
	6. Find the area where the signature is located using np.argwhere(grayScaleMask==0). This selects the black pixels in the image. 
	7. Plot the points of the returned value of np.argwhere using points = np.fliplr(points) then x, y, width, height = cv2.boundingRect(points)
	8. Crop both the grayscale and original image.
	9. Get the ROI of the original image by getting the reverse mask of it then anding itwith itself.
	10. Create a grayScale mask of the new cropped grayscale image.
	11. Try to isolate the signature further using:
		shape = cv2.getStructuringElement(cv2.MORPH_RECT,(80,80))
		openMask = cv2.morphologyEx(grayScaleMask,cv2.MORPH_OPEN,shape)
		closedMask = cv2.morphologyEx(openMask,cv2.MORPH_CLOSE,shape)
		closedMask = cv2.bitwise_not(closedMask)
		regionOfInterestOne = cv2.bitwise_and(croppedColorImage,croppedColorImage,mask=closedMask)
	12. Create a blank background image by getting to shape of the original image, then use np.zeros((height, width, 3), np.uint8) to create the image
	13. Change the background to full white then add the background and ROI together.
	14. Write the image to an image file, return the image and display it.
	
	Give an overview:
	The purpose of this application is to allow a user to isolate Donald Trumps signature, 
	then use it in what ever way the like.
	
	Comment on experiments:
	1. Tried to isolate the signature through cropping and morphology, but the result of this application is all I could manage.
	
	2. Tried taking the result of the program and applying an adaptive threshold. 
	My idea was to isolate the pixels further but it didnt really have any effect on the image.
	
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
		try:
			#Opening an image from a file:
			print("Please Select a Signature you wish to forge:")
			file = easygui.fileopenbox()
			image = cv2.imread(file)
			forged_image = self.forgeSignature(image)
		except:
			print("User failed to select an image.")
		while True:
			# Showing an image on the screen (OpenCV):
			cv2.imshow("Trump Signature", forged_image)
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
		
		# Create a grayscale mask for the signature, then use morphology to isolate part of the signature. 
		grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		grayScaleHistogram = cv2.equalizeHist(grayScale)
		threshold = cv2.threshold(grayScaleHistogram, 218, 255, cv2.THRESH_BINARY)[1]
		threshold = cv2.bitwise_not(threshold)
		
		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,50))
		openMask = cv2.morphologyEx(threshold,cv2.MORPH_OPEN,shape)
		closedMask = cv2.morphologyEx(openMask,cv2.MORPH_CLOSE,shape)
		
		# Call the cropImage function.
		croppedColorImage, croppedGrayScaleImage = self.cropImage(closedMask, image)
		
		# Retrieve a coloured image of the newly cropped area.
		reverseSignature = cv2.bitwise_not(croppedGrayScaleImage)
		regionOfInterestOne = cv2.bitwise_and(croppedColorImage,croppedColorImage,mask=reverseSignature)
		
		# Retrieve a grayScaleMask of the newly cropped area.
		grayScale = cv2.cvtColor(regionOfInterestOne, cv2.COLOR_BGR2GRAY)
		grayScaleMask = cv2.adaptiveThreshold(grayScale, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 11,C = 20)
		
		# Attempting to isolate the signature further.
		shape = cv2.getStructuringElement(cv2.MORPH_RECT,(80,80))
		openMask = cv2.morphologyEx(grayScaleMask,cv2.MORPH_OPEN,shape)
		closedMask = cv2.morphologyEx(openMask,cv2.MORPH_CLOSE,shape)
		closedMask = cv2.bitwise_not(closedMask)
		regionOfInterestOne = cv2.bitwise_and(croppedColorImage,croppedColorImage,mask=closedMask)
		
		# Line 101 and 102 are referenced by reference Number 2.
		# Apply the extracted Signature to the background.
		reverseBackground = cv2.bitwise_not(closedMask)
		height, width = croppedGrayScaleImage.shape
		background = np.zeros((height, width, 3), np.uint8)
		background[:] = (255,255,255)
		regionOfInterestTwo = cv2.bitwise_and(background,background,mask=reverseBackground)
		forged_signature = regionOfInterestOne + regionOfInterestTwo
		
		# Create an image of the signature.
		cv2.imwrite('forgedSignature.jpg', forged_signature)
		return forged_signature
		
	def cropImage(self, mask, colorImage):
		"""
		Purpose of function:
		The purpose of this function is to crop the grayscale and colored images which have been passed into the function.
		
		Example Function:
		variable = self.cropImage(param1, param2)
		
		Args:
			param1 (numpy.ndarray): This is the first paramter. Which is a gryscale mask for the colored Image.
			param2 (numpy.ndarray): This is the first paramter. Which is the original colored Image.
		return:
			param1 (numpy.ndarray): This will return a cropped version of the grayscale mask.
			param2 (numpy.ndarray): This will return a cropped version of the original colored image.
		"""
		# The next six lines of code are from reference Number 1.
		# Crop the area where the signature is located. 
		points = np.argwhere(mask==0)
		points = np.fliplr(points)
		x, y, width, height = cv2.boundingRect(points)
		x, y, width, height = x, y, width, height
		croppedColorImage = colorImage[y:y+height,x:x+width]
		croppedGrayScaleImage = mask[y:y+height,x:x+width]
		return croppedColorImage, croppedGrayScaleImage
		
if __name__ == "__main__":
	forged_signature = forgery()
	forged_signature.getImage()
	