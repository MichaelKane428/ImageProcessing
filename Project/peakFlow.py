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
	[1]The code below for OCR would work on the sample OCR images, 
	   but would not work on our cropped peakFlow images
	
		gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray,(5,5),0)
		thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

		#################      Now finding Contours         ###################

		_, contours, _hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

		samples =  np.empty((0,100))
		responses = []
		keys = [i for i in range(48,58)]

		for cnt in contours:
			if cv2.contourArea(cnt)>50:
				[x,y,w,h] = cv2.boundingRect(cnt)

				if  h>28:
					cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
					roi = thresh[y:y+h,x:x+w]
					roismall = cv2.resize(roi,(10,10))
					cv2.imshow('norm',im)
					key = cv2.waitKey(0)

					if key == 27:  # (escape to quit)
						sys.exit()
					elif key in keys:
						responses.append(int(chr(key)))
						sample = roismall.reshape((1,100))
						samples = np.append(samples,sample,0)

		responses = np.array(responses,np.float32)
		responses = responses.reshape((responses.size,1))
		print "training complete"

		np.savetxt('generalsamples.data',samples)
		np.savetxt('generalresponses.data',responses)
	
	[2] Attempt at rotating the test images to have the same orientation. This will allow us to use OCR to check the upright Characters. 
		image = cv2.imread("ROI.jpg")
		for angle in np.arange(0, 100, 15):
			rotated = imutils.rotate(image, angle)
		cv2.imshow("NEW", rotated)
		key = cv2.waitKey(0)
	
	[3] Attempting tring to find the center of the point to underline/hightligh the result.
		# new code 
		# tring to find the center of the point to underline/hightligh the result 
		# https://stackoverflow.com/questions/4002796/python-find-the-min-max-value-in-a-list-of-tuples
		rb = self.find_red(ROI)
		points = np.argwhere(croppedRed==255)
		points = np.fliplr(points)
		zip(*points)
		maxV = map(max, zip(*points))
		minV = map(min, zip(*points))
		meanMax = (maxV[0]+ minV[0])/2
		meanMin = (maxV[1]+ minV[1])/2
		print(meanMax)
		print(meanMin)
		cv2.line(img = ROI, pt1 = (meanMax,meanMin), 
		pt2 =(meanMax+20,meanMin+20), color = (255,255,255), thickness = 3)
	
	References:
	[1]. docs opencv, DO. (2017) Contours: Getting Started.
	Available at: https://docs.opencv.org/3.2.0/d4/d73/tutorial_py_contours_begin.html (24/11/2017)
	
	[2]. docs opencv, DO. (2017) Contour Features.
	Available at: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#contour-features (2017)
    
	[3]. stackoverflow, SO. (2017) Find and draw the largest contour in opencv on a specific color (Python).
	Available at: https://stackoverflow.com/questions/44588279/find-and-draw-the-largest-contour-in-opencv-on-a-specific-color-python (24/11/2017)
	
	[4]. rroji, RR. (2017) Number Plate Recognition Using an Improved Segmentation.
	Available at: http://www.rroij.com/open-access/number-plate-recognition-using-an-improvedsegmentation-.php?aid=47317 (24/11/2017)
	
	[5]. pyimagesearch, PIS. (2017) Credit card OCR with OpenCV and Python.
	Available at: https://www.pyimagesearch.com/2017/07/17/credit-card-ocr-with-opencv-and-python/ (24/11/2017)
	
	[6]. pyimagesearch, PIS. (2017) Using Tesseract OCR with Python.
	Available at: https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/ (24/11/2017)
	
	[7]. stackoverflow, SO. (2017) Preprocessing image for Tesseract OCR with OpenCV
	Available at: https://stackoverflow.com/questions/28935983/preprocessing-image-for-tesseract-ocr-with-opencv (24/11/2017)
	
	[8]. stackoverflow, SO. (2017) How to use Opencv for Document Recognition with OCR?
	Available at: https://stackoverflow.com/questions/7542194/how-to-use-opencv-for-document-recognition-with-ocr (24/11/2017)
	
	[9]. scholarcommons, SC. (2017) Image processing for the extraction of nutritional information from food labels.
	Available at: https://scholarcommons.scu.edu/cgi/viewcontent.cgi?referer=https://www.google.ie/&httpsredir=1&article=1041&context=cseng_senior (24/11/2017)

	[10]. docs opencv, DO. (2017) Canny Edge Detection.
	Available at: https://docs.opencv.org/3.3.1/da/d22/tutorial_py_canny.html (24/11/2017)
	
	[11]. docs opencv, DO. (2017) Changing Colorspaces.
	Available at: https://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html (24/11/2017)
	
	[12]. stackoverflow, SO. (2017) Simple Digit Recognition OCR in OpenCCV-Python.
	Available at: https://stackoverflow.com/questions/9413216/simple-digit-recognition-ocr-in-opencv-python (24/11/2017)
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
		
		cv2.imshow("ROI", ROI)
		cv2.imwrite("ROI.jpg", ROI)
		key = cv2.waitKey(0)
		print("Your region of interest is now in an image called ROI.jpg")

	def cropROI(self, croppedImage, croppedRed):
		points = np.argwhere(croppedRed==255)
		points = np.fliplr(points)
		x, y, width, height = cv2.boundingRect(points)
		x, y, width, height = x, y, width+50, height+100
		croppedColorImage = croppedImage[y:y+height,x:x+width]
		return croppedColorImage
	
	def cropLargestContour(self, alteredImage, contours):
		#Code Taken from Source Number [3]
		#Crop the largestContour. Integration of the code with cropping to find the Largest contour.
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