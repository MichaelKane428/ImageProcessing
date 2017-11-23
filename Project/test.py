import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui
import imutils

class peakFlow():
	def start(self):
		image = cv2.imread("ROI.jpg")
		for angle in np.arange(0, 100, 15):
			rotated = imutils.rotate(image, angle)
		cv2.imshow("NEW", rotated)
		key = cv2.waitKey(0)
	
if __name__ =="__main__":
	instance = peakFlow()
	instance.start()