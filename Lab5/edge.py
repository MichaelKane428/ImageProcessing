#!python2
"""
	(C) Michael Kane 2017

	Student No: C14402048
	Course: DT211C
	Date: 26/10/2017

	Title: Edge and gradient detection.

	Introduction:

	Step-by-step:

	
	Give an overview:
	
	Comment on experiments:
	
	
	References: 
	
"""


# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class edge():
	
	def getImage(self):
		try:
			#Opening an image from a file:
			print("Please Select an image:")
			file = easygui.fileopenbox()
			image = cv2.imread(file)
			gradients = self.getGradients(image)
			canny = self.getCanny(image)
		except:
			print("User failed to select an image.")
		while True:
			# Showing an image on the screen (OpenCV):
			cv2.imshow("Image", canny)
			key = cv2.waitKey(0)

			# if the 'q' key is pressed, quit:
			if key == ord("q"):
				break

	def getGradients(self, image):
		G = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		gradients = cv2.Sobel(G,ddepth=cv2.CV_64F,dx=1,dy=0)
		return gradients
		
	def getCanny(self, image):
		canny = cv2.Canny(image,threshold1=100,threshold2=200)
		return canny
		
if __name__ == "__main__":
	detect_edge = edge()
	detect_edge.getImage()
	