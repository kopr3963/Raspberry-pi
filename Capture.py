# Capture.py
#_*_coding: utf-8-*-
import cv2
import numpy as numpy

def settings():
	try:
		print '카메라 구동';
		cap = cv2.VideoCapture(0);
	except:
		print '카메라 구동 실패';
		return;

	cap.set(3, 480);
	cap.set(4, 320);

	while True:
		ret,frame = cap.read();

		if not ret:
			print('ret is error');
			break;

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
		cv2.imshow('video',gray);

		k = cv2.waitKey(1) & 0xFF;
		if k == 27:
			break;
		cap.release();
		cv2.destroyAllWindows();
settings();
