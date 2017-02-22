import numpy as np
import time
import cv2
import os

camera = cv2.VideoCapture(0)
camera.set(cv2.cv.CV_CAP_PROP_FPS, 1)
time.sleep(1.0)
background = None
frameNumber = 0
frameCount = 0
imgDir = "img"
start = time.time()
thresholdLimit = 20

while(True):
	#capture frame by frame
	ret, frame = camera.read()

	#operations on the frame
	currentFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	if background is None:
		background = currentFrame
		continue

	currentFrame = cv2.GaussianBlur(currentFrame, (31, 31), 0)

	#compare frames
	frameDelta = cv2.absdiff(background, currentFrame)
	thresh = cv2.threshold(frameDelta, thresholdLimit, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=30)
	(contours, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #find contours

	#fps
	end = time.time()
	seconds = end - start
	fps = round((1 / seconds), 1)
	start = time.time()
	cv2.putText(frame, "fps: {}".format(fps), (400, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 140, 255), 1)

	for contour in contours:
		if cv2.contourArea(contour) < 250:
			continue

		(x, y, w, h) = cv2.boundingRect(contour)

		#show movement
		color = (0, 255, 0)
		cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
		frameCount += 1

		if frameCount == 24:
			#save images when movement is detected
			cv2.imwrite(os.path.join(imgDir, str(frameNumber))+".png", frame)
			frameNumber += 1
			frameCount = 0

	#display result
	cv2.imshow("Feed",frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

#release capture
camera.release()
cv2.destroyAllWindows()
