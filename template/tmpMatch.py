##template matching with drawing rectangle

from PIL import ImageGrab
import numpy as np
import cv2

#result of template match
match_list = []
file_no = 0
#set screen size
xsize = (0, 1250)
ysize = (150, 1055)

#set image file
file_name += ('img_title6.png',....)
imread_file = imgfile_read(file_name)

#to find image from background image and drawing rectangle
#information about template matching is storaged in match_list
#match_list = [(filenum, (position),...), ()]

def imgfile_read(filelist):
    imglist = []
    for i in range(len(filelist)):
        imread_temp = cv2.imread(filelist[i], 0)
        imglist += [imread_temp,]
    return imglist

def matched_img(img_rgb, matched_gray, file_num):
    count = 0
    # temp_list = [file num + [position]]
    temp_list = [file_num]
    global match_list
    h, w = img_rgb.shape[::1]
    res = cv2.matchTemplate(matched_gray, img_rgb, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(matched_gray, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        count += 1
        temp_list += [pt]
        if len(zip(*loc[::-1])) == count:
            print ("complete", count, pt, "file_num", file_num)
            match_list += [temp_list]
    return matched_gray

def match_img():
    global match_list
    global file_no
    global prevent_act
    count = 0
    file_no = 0
    while True:
        # make a background
        screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # find image
        for i in range(len(file_name):
          screen_gray = matched_img(imread_file[i], screen_gray, file_no)
          file_no += 1
        match_list = []
        file_no = 0
        count = 0
        #resize screen
        screen_gray = cv2.resize(screen_gray, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('screen_gray: test', screen_gray)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
            
