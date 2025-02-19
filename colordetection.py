import cv2 
import numpy as np

img=cv2.imread('group.jpg')

imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV',imghsv)
cv2.waitKey(0)