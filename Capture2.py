#Capture2.py

import numpy as np
import cv2

cap = cv2.VideoCapture(0);

while(True):
	ret,frame = cap.read();
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

	cv2.imshow('frame',gray);
 	edges = cv2.Canny(gray, 50,150,apertureSize =3)

  	lines = cv2.HoughLines(edges, 1, np.pi/180,140);

  	for line  in lines:
    	r, theta = line[0]
    	a = np.cos(theta)
    	b = np.sin(theta)
	    x0 = a*r
	    y0 = b*r
	    x1 = int(x0 + 1000*(-b))
	    y1 = int(y0 + 1000*a)
	    x2 = int(x0 - 1000*(-b))
	    y2 = int(y0 - 1000*a)

	    cv2.line(ret, (x1, y1), (x2, y2), (0,255,0),1)


	if cv2.waitKey(1) & 0xFF == ord('q'):
	 break;

cv2.imshow('frame',gray)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
