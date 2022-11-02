import numpy as np
import serial
import time
import sys
import cv2
#Create an Arduino communications link by replacing "COM5" with the port to which your Arduino is attached.
ard = serial.Serial('COM5', 9600) 
time.sleep(2)
print("Arduino Connected ...")
#Bringing in the Haarcascade for facial recognition
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#to record the webcam's video stream.
capture = cv2.VideoCapture(0)
#Find faces by reading the collected image, turning it into a grayscale image.
while 1:
    ret, img = capture.read()
    cv2.resizeWindow('img', 500,500)
    cv2.line(img,(500,250),(0,250),(0,255,0),1)
    cv2.line(img,(250,0),(250,500),(0,255,0),1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    grayInCol  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detectFaces = cascade_face.detectMultiScale(grayInCol, 1.3)
#Rectangle-enclose the face by locating it.
    for (x,y,w,h) in detectFaces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        gray_roi  = grayInCol[y:y+h, x:x+w]
        color_roi = img[y:y+h, x:x+w]
        myArr = {y:y+h, x:x+w}
        print (myArr)
        
        print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))
# Center of roi (Rectangle)
        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2
        print (xx)
        print (yy)
        center = (xx,yy)
# data transfer to the Arduino
        print("Center of Rectangle is :", center)
        data = "X{0:d}Y{1:d}Z".format(xx, yy)
        print ("output = '" +data+ "'")
        ard.write(data)
#Show the stream.
    cv2.imshow('img',img)
#Hit 'Esc' to terminate execution 
    p = cv2.waitKey(30) & 0xff
    if p == 27:
       break