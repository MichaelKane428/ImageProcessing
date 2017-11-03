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
	
	
	References: 
	https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
	https://docs.opencv.org/3.2.0/d1/d79/group__photo__denoise.html#ga76abf348c234cecd0faf3c42ef3dc715
	https://docs.opencv.org/3.2.0/d5/d69/tutorial_py_non_local_means.html
	
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
				#grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				#cleanedFrame = self.cleanFrame(grayScale)
				cleanedVideo.write(frame)
				cv2.imshow('frame',frame)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break

			video.release()
			cleanedVideo.release()
			cv2.destroyAllWindows()
		
	def cleanFrame(self, frame):
		reduceNoise = cv2.fastNlMeansDenoising(frame, None) 
		return reduceNoise

if __name__ == "__main__":
	cleaned_video = zorro()
	cleaned_video.getVideo()
	