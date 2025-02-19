import cv2 
import numpy as np

img=np.zeros((512,512,3),np.uint8)
print(img)
#colour the image
# img[:]=255,0,0 #blue
# img=cv2.imread('group.jpg')
#cv2.line(img,(0,0),(300,300),(0,255,0),3)# first param-start co-ordinates,then end co-ordinated,then the color of the line,and then thikness of line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow('group', img)
cv2.waitKey(0)