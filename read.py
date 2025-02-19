import cv2 
import numpy as np

img=cv2.imread('group.jpg')
kernel=np.ones((5,5),np.uint8)
#to read image
# cv2.imshow('group', img)
# cv2.waitKey(0)

# greyimage
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image',imgray)
# cv2.waitKey(0)

# blur image
imgblur=cv2.GaussianBlur(imgray,(7,7),0)
cv2.imshow('blur image',imgblur)
# cv2.waitKey(0)

# edge dectector
imgcannay=cv2.Canny(img,150,200)
cv2.imshow('edge detect image',imgcannay)
#cv2.waitKey(0)

#image dilation mean thicker
imagedilation=cv2.dilate(imgcannay,kernel,iterations=1)
cv2.imshow(' image dilation',imagedilation)
# cv2.waitKey(0)

#imgae corrossion make it thinner
imageerro=cv2.erode(imagedilation,kernel,iterations=1)
cv2.imshow(' image erod',imageerro)
cv2.waitKey(0)