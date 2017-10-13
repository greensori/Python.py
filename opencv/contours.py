import cv2
import numpy as np
import matplotlib.pyplot as plt

def approxpoly():
    img = cv2.imread('testsample\pp1.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[1511]
    epsilon = 0.095 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(img, approx, -1, (0,255,0), 3)
    cv2.imwrite('testsample\pp_polyDPthres.png',thresh)
    cv2.imwrite('testsample\pp_polyDP.png',img)
    print ('complete')  

def boundaryrec():
    img = cv2.imread('testsample\pp1.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
    #ret, thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imwrite('testsample\pp_bdThres.png',thresh)
    cv2.imwrite('testsample\pp_boundary.png',img)
    print ('complete')
