import cv2
import numpy as np

img = cv2.imread('testsample\pp2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[3]
print (cnt)
cv2.drawContours(img, cnt, -1, (0,255,0), 3)

cv2.imwrite('testsample\pr1.png',thresh)
cv2.imwrite('testsample\pr2.png',img)
print ('complete')
