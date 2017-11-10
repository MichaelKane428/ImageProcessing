#!python2
"""
	(C) Michael Kane 2017

	Student No: C14402048
	Course: DT211C
	Date: 02/11/2017
	GitHub: https://github.com/MichaelKane428/ImageProcessing/tree/master/Assignment2
	Title: Assignment 2 Zorro

	Introduction:
	The goal of this application is to clean the zorro video, by removing the white noise and
	the distorted background
	
	Step-by-step:
	1. set the frames you wish to clean using:
	firstFrame = 300
	lastFrame = 309
	
	2. capture the video using video = cv2.VideoCapture('Zorro.mp4').
	
	3. Prepare a new video to write your frames to. Fourcc defines the codec to use for windows I used XVID, but mac would need MP4
	The new video needs to have the same width and height as the original so we grab them using video.get. 
	Finally the videowriter object is created.
	
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
	width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
	cleanedVideo = cv2.VideoWriter('CleanedZorro.avi',fourcc, 20.0, (width,height))
	
	4. Loop through and wait for the frames to show up using a counter with the frames selected.
	if counter >= firstFrame and counter < lastFrame:
	
	In this codintional statment call the cleanFrame function then write the returned frame to the new video object.
	
	5. Inside the cleanFrame function use fastnldenoise and medianblur to clean up the image.
	Once the image is cleaned write the frame to an image file.
	
	fastDenoise = cv2.fastNlMeansDenoising(frame,None,10,7,21)
	medianBlurFrame = cv2.medianBlur(frame, 11)
	cv2.imwrite('frame_' + str(counter) + '.jpg', medianBlurFrame)
	
	6. Release both videos e.g. video.release(), and destroy all windows once the application has finished.
	
	Give an overview:
	My first attempt at this application involved the entire video. I found it difficult to get results as
	the algorithms would take up to an our to run. Example the fastNlMeansDenoising algorithm.
	Github version for this attempt below.
	https://github.com/MichaelKane428/ImageProcessing/commit/dbb58b21f6d95cbc3852840a83af63bcf40e7108#diff-f36d187bd5953849a16b16b5401342a8
	
	The second attempt which can be seen below uses the fastNlMeansDenoising algorithm, 
	and it takes about 3 minutes for the application to run on ten frames.
	The output is no where near what was desired.
	I did try alot of experiments for both attempts, but I felt I lacked an understanding of the algorithms
	even with the documentation to help me.
	
	Comment on experiments:
	1.  I attempted to use the following code to clean up the image.
		CleanedFrame = cv2.fastNlMeansDenoising(frame,None,10,7,21)
		The issues I was having was with the final argument(21). The higher this was the longer it took to process a single frame.
		It was taking upwards of one hour to generate anything.
		
	2. The purpose of attempts 2-4 was to blur the image and reduce the noise. (unsuccessful)
	frameKernel = np.array([[1,4,1], [4,7,4], [1,4,1]],dtype=float)
	CleanedFrame = cv2.filter2D(frame,ddepth=-1,kernel=frameKernel)
	
	3.CleanedFrame = cv2.bilateralFilter(frame,9,75,75)
	
	4.CleanedFrame = cv2.GaussianBlur(frame,(5,5),0)
	
	5.kernel = np.ones((10,10),np.float32)/100
	
	6.CleanedFrame = cv2.filter2D(frame,-1,kernel)
	  CleanedFrame = cv2.blur(frame,(2,2))
	
	7.kernel = np.ones((10,10),np.float32)/25
	  cleanedFrame = cv2.blur(frame,(10,10))
	
	8. This code produced Black frames with sme detail in grey. 
	denoisedFrame = cv2.fastNlMeansDenoising(frame,None,10,7,21)
	cleanedFrame = cv2.subtract(denoisedFrame ,frame)
	cleanedFrame2 = cv2.add(cleanedFrame, frame)

		
	9.  This code produced black holes in the image:
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
	1. Docs OpenCV, DO. (2017)Getting Started with Videos.
	Available at: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html (10/11/2017)
	
	//fastdenoise
	2. Docs OpenCV, DO. (2017)Denoising Computational Photography.
	Available at: https://docs.opencv.org/3.2.0/d1/d79/group__photo__denoise.html#ga76abf348c234cecd0faf3c42ef3dc715 (10/11/2017)
	
	3. Docs OpenCV, DO. (2017)Image Denoising.
	Available at: https://docs.opencv.org/3.2.0/d5/d69/tutorial_py_non_local_means.html (10/11/2017)
	
	//bilateralFilter, gausianblur, 2dfilter
	4. Docs OpenCV, DO. (2017)Smoothing Images.
	Available at: https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html (10/11/2017)
	
	5. Answers OpenCV, AO. (2017)Smoothing image-better way of doing that.
	Available at: http://answers.opencv.org/question/1451/smoothing-image-better-way-of-doing-that/ (10/11/2017)
	
	//median blur
	6. Docs OpenCV, DO. (2017) Image Filtering.
	Available at: https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html?highlight=median#cv2.medianBlur (10/11/2017)
	
	7. Stack Overflow, SO. (2017) Median Filter with Python and OpenCV.
	Available at: https://stackoverflow.com/questions/18427031/median-filter-with-python-and-opencv (10/11/2017)
	
	//Writing a video
	8. Stack Overflow, SO. (2017) Video capture PROPID parameters in openCV.
	Available at: https://stackoverflow.com/questions/32468371/video-capture-propid-parameters-in-opencv (10/11/2017)
	
	9. Docs OpenCV, DO. (2017) Getting Started with Videos.
	Available at: https://docs.opencv.org/3.3.0/dd/d43/tutorial_py_video_display.html (10/11/2017)
	
	
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
		#Saw Jane do this in class great idea for getting the frames.
		firstFrame = 300
		lastFrame = 309
		counter = 0
		video = cv2.VideoCapture('Zorro.mp4')
		
		if(video.isOpened() == False):
			print("There was an error trying to open your file.")
			print("Please check that the file name is correct, and that the file is in the correct directory.")
		else:
			print("Please wait for the Program to finish.")
			print("You will find your ten images, and a video of the cleaned frames\nin the folder with this file.")
			print("NOTE: The average time to run this file is 3 minutes.")
			# Prepare the extension for the cleaned video.
			fourcc = cv2.VideoWriter_fourcc(*'XVID')
			height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
			width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
			cleanedVideo = cv2.VideoWriter('CleanedZorro.avi',fourcc, 20.0, (width,height))
			
			# Clean the frame and write to a video.
			while(video.isOpened()):
				ret, frame = video.read()
				if counter >= firstFrame and counter < lastFrame: 
					cleanedFrames = self.cleanFrame(frame, counter)
					cleanedVideo.write(cleanedFrames)
				elif counter == lastFrame:
					cleanedFrames = self.cleanFrame(frame, counter)
					cleanedVideo.write(cleanedFrames)
					video.release()
				counter += 1	
			video.release()
			cleanedVideo.release()
			cv2.destroyAllWindows()
	
	# Please check the experiments section. It shows the different algorithms I tried.
	def cleanFrame(self, frame, counter):
		"""
		Purpose of function:
		Clean the frame and write it as a new image.
		
		Example Function:
		self.cleanFrame(arg1, arg2)
		
		Args:
			frame: image from the video.
			counter: an integer value denoting the current frame.
		return:
			cleanedFrame: Cleaned image.
		"""
		fastDenoise = cv2.fastNlMeansDenoising(frame,None,10,7,21)
		cleanedFrame = cv2.medianBlur(frame, 11) 
		cv2.imwrite('frame_' + str(counter) + '.jpg', cleanedFrame)
		return cleanedFrame

if __name__ == "__main__":
	cleaned_video = zorro()
	cleaned_video.getVideo()
	