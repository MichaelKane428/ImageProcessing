#!python2
"""
	(C) Michael Kane 2017

	Student No: C14402048
	Course: DT211C
	Date: 02/11/2017

	Title: 

	Introduction:
	
	Step-by-step:
	
	Give an overview:
	
	Comment on experiments:
	1. I attempted to use the following code to clean up the image.
	CleanedFrame = cv2.fastNlMeansDenoising(frame,None,10,7,21)
	The issues I was having was with the final argument(21). The higher this was the longer it took to process a single frame.
	It was taking upwards of ten minutes to generate anything. The final product of waiting 30 minutes was a video file that didnt work.
	//Remove this comment when I have tried it on the college pcs. 
	
	2. 	Tried all these different types of kernals to removce noise. After working with them for a while. I belive I have,
		a complete misunderstanding about how they work. 
		They just blurred the image and didint reduce the noise, It made the frames alot worse.
		1.frameKernel = np.array([[1,4,1], [4,7,4], [1,4,1]],dtype=float)
		  CleanedFrame = cv2.filter2D(frame,ddepth=-1,kernel=frameKernel)
		
		2.CleanedFrame = cv2.bilateralFilter(frame,9,75,75)
		
		3.CleanedFrame = cv2.GaussianBlur(frame,(5,5),0)
		
		4.kernel = np.ones((10,10),np.float32)/100
		
		5.CleanedFrame = cv2.filter2D(frame,-1,kernel)
		  CleanedFrame = cv2.blur(frame,(2,2))
	
	3.  Eroding the image was interesting..........
		grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		grayScaleMask = cv2.adaptiveThreshold(grayScale, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 5,C = 10)
		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,50))
		erosion = cv2.erode(grayScaleMask,shape)
		regionOfInterestOne = cv2.bitwise_and(frame,frame,mask=erosion)
	
	References: 
	//Displaying the video.
	https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
	https://docs.opencv.org/3.2.0/d1/d79/group__photo__denoise.html#ga76abf348c234cecd0faf3c42ef3dc715
	https://docs.opencv.org/3.2.0/d5/d69/tutorial_py_non_local_means.html
	
	//Noise reduction/bluring
	https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
	http://answers.opencv.org/question/1451/smoothing-image-better-way-of-doing-that/
	
	//These two go together
	https://stackoverflow.com/questions/32468371/video-capture-propid-parameters-in-opencv
	https://docs.opencv.org/3.3.0/dd/d43/tutorial_py_video_display.html
	
	
"""


# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

class zorro():
	"""
	Purpose of function:
	Allow portablity of the zoro code
	
	Example Function:
	instance = zoro()
	
	Args:
		None
	return:
		None
	"""
	
	def getVideo(self):
		"""
		Purpose of function:
		Allow a user to select an video.
		
		Example Function:
		instance.getVideo()
		
		Args:
			None
		return:
			None
		"""
		
		video = cv2.VideoCapture('Zorro.mp4')
		if(video.isOpened() == False):
			print("There was an error trying to open your file.")
			print("Please check that the file name is correct, and that the file is in the correct directory.")
		else:
			fourcc = cv2.VideoWriter_fourcc(*'XVID')
			height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
			width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
			cleanedVideo = cv2.VideoWriter('CleanedZorro.avi',fourcc, 20.0, (width,height))
			while(video.isOpened()):
				ret, frame = video.read()
				cleanedFrame = self.cleanFrame(frame)
				cleanedVideo.write(cleanedFrame)
				cv2.imshow('frame',cleanedFrame)
				if cv2.waitKey(25) & 0xFF == ord('q'):
					break
			video.release()
			cleanedVideo.release()
			cv2.destroyAllWindows()
		
	def cleanFrame(self, frame):
		grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		grayScaleMask = cv2.adaptiveThreshold(grayScale, maxValue = 255,
		adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
		thresholdType = cv2.THRESH_BINARY,
		blockSize = 5,C = 10)
		shape = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(40,50))
		erosion = cv2.erode(grayScaleMask,shape)
		regionOfInterestOne = cv2.bitwise_and(frame,frame,mask=erosion)
		return regionOfInterestOne

if __name__ == "__main__":
	cleaned_video = zorro()
	cleaned_video.getVideo()
	