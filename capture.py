import numpy as np
import time
import cv2
import os
import datetime

camera = cv2.VideoCapture(0)
time.sleep(1.0)
background = None
frameNumber = 0
frameCount = 0
imgDir = "/home/arctic/img"
start = time.time()
minArea = 50*50
thresholdLimit = 80
dilationPixels = 10
gaussianPixels = 31
wroteImg = 0
writeTime = 0


while(True):
	#capture frame by frame
	ret, frame = camera.read()

	#operations on the frame
	currentFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	currentFrame = cv2.GaussianBlur(currentFrame, (gaussianPixels, gaussianPixels), 0)

	if background is None:
		background = currentFrame
		continue

	#reset background frame, y u no work??
	"""if cv2.waitKey(1) & 0xFF == ord("r"):
		time.sleep(1.0)
		background = None
		ret, frame = camera.read()
		currentFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		currentFrame = cv2.GaussianBlur(currentFrame, (gaussianPixels, gaussianPixels), 0)
		background = currentFrame
		continue"""

	#compare frames
	frameDelta = cv2.absdiff(background, currentFrame)
	thresh = cv2.threshold(frameDelta, thresholdLimit, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=dilationPixels)
	(contours, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #find contours

	#fps
	end = time.time()
	seconds = end - start
	fps = round((1 / seconds), 1)
	start = time.time()

	today_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

	secondInt = int(time.time())

#	cv2.putText(frame, "fps: {}".format(fps), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1)
	cv2.putText(frame, " {}".format(today_date), (20, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1)

	for contour in contours:
		if cv2.contourArea(contour) < minArea:
			continue

		(x, y, w, h) = cv2.boundingRect(contour)

		#show movement
		color = (0, 255, 0)
		cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
		frameCount += 1

		#save images when movement is detected
		if wroteImg == 0:
			cv2.imwrite(os.path.join(imgDir, str(format(frameNumber, '04')))+".png", frame)
			frameNumber += 1
			frameCount = 0
			wroteImg = 1
			writeTime = secondInt

		if secondInt > writeTime:
			wroteImg = 0
	#display result
	cv2.imshow("feed",frame)
#	cv2.imshow("delta",frameDelta)
#	cv2.imshow("Thresh",thresh)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

#release capture
camera.release()
cv2.destroyAllWindows()
