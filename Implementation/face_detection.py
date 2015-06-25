import numpy as np
import cv2

cascades = ['newcascade0.1BASIC1\\cascade.xml',
'newcascade0.1CORE1\\cascade.xml',
'newcascade0.1ALL1\\cascade.xml',
'newcascade0.1BASIC5\\cascade.xml',
'newcascade0.1CORE5\\cascade.xml',
'newcascade0.1ALL5\\cascade.xml',
'newcascade0.1BASIC10\\cascade.xml',
'newcascade0.1CORE10\\cascade.xml',
'newcascade0.1ALL10\\cascade.xml',
'newcascade0.2BASIC1\\cascade.xml',
'newcascade0.2CORE1\\cascade.xml',
'newcascade0.2ALL1\\cascade.xml',
'newcascade0.2BASIC5\\cascade.xml',
'newcascade0.2CORE5\\cascade.xml',
'newcascade0.2ALL5\\cascade.xml',
'newcascade0.2BASIC10\\cascade.xml',
'newcascade0.2CORE10\\cascade.xml',
'newcascade0.2ALL10\\cascade.xml',
'newcascade0.4BASIC1\\cascade.xml',
'newcascade0.4CORE1\\cascade.xml',
'newcascade0.4ALL1\\cascade.xml',
'newcascade0.4BASIC5\\cascade.xml',
'newcascade0.4CORE5\\cascade.xml',
'newcascade0.4ALL5\\cascade.xml',
'newcascade0.4BASIC510\\cascade.xml',
'newcascade0.4CORE1\\cascade.xml',
'newcascade0.4ALL10\\cascade.xml']

for casc in cascades: 
	face_cascade = cv2.CascadeClassifier(casc)

	img = cv2.imread('02.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray)
	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	cv2.imshow('img',img)
	cv2.imwrite(casc+'1.png',img)
	img = cv2.imread('01.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray)
	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	cv2.imshow('img',img)
	cv2.imwrite(casc+'2.png',img)
	img = cv2.imread('lost.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray)
	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	cv2.imshow('img',img)
	cv2.imwrite(casc+'3.png',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

