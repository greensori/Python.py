# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from PIL import ImageGrab
from multiprocessing import process
from datetime import datetime
from datetime import date
import datetime as dtime
import numpy as np
import cv2
import time
import os
import psutil
import pyautogui
import Tkinter
import clipboard
import csv

#result of template match
match_list = []

#to save file number
file_no = 0
prevent_action = 0
#this will ussed in class goodForwork
click_raw = 1
autokey = 0
count_cap = 0
macro_key = 0
#set screen size
xsize = (0, 1250)
ysize = (150, 1055)

t1 = ()

file_title = ('img_title1.png', 'img_title2.png', 'img_title3.png', 'img_title4.png', 'img_title5.png')
file_title += ('img_title6.png',)
file_info = ('img_info1.png', 'img_info2.png', 'img_info3.png', 'img_info4.png')
file_menu = ('img_menu1.png', 'img_menu2.png', 'img_menu3.png', 'img_menu4.png', 'img_menu5.png')
file_deleter = ('img_deleter.png', 'img_deleter1.png')
file_macro = ("img_title1.png", "img_main3.png", "img_title6.png", "img_info1.png", "img_info2.png", "img_info4.png")
file_math = ("img_0.png", "img_1.png", "img_2.png", "img_3.png", "img_4.png", "img_5.png", "img_6.png", "img_7.png", "img_8.png", "img_9.png")


class csvcard:
    def __init__(self):
        self.loc = 'D:\print\csv_temp.csv'        
        self.data4 = datetime.today().strftime("%y-%m-%d")
        if rb.get() == 4:
            self.data3 = 'register'
        elif rb.get() == 5:
            self.data3 = 'change'
        else:
            self.data3 = 'notin'
    def firstwrite(self):
        with open(self.loc, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',', quotechar = '|')
            writer.writerow(['obs', 'code', 'hp', 'type', 'date', 'result'])
    # num is target data that will substitute to new data
    def modifydata(self, location, obs, new_data, num):
        obs -= 1
        r = csv.reader(open(location))
        lines = [l for l in r]
        if num == 3:
            lines[obs][3] = new_data
            writer = csv.writer(open(location, 'w'))
            writer.writerows(lines)
        if num == 4:
            lines[obs][4] = new_data
            writer = csv.writer(open(location, 'w'))
            writer.writerows(lines)
        if num == 5:
            lines[obs][5] = new_data
            writer = csv.writer(open(location, 'w'))
            writer.writerows(lines)
    def card(self, name, phone, data5):
    ##if count2  value is '0' then writing new data
    ## if count2 value is '1' and rwcount = write then modify previuous data
        self.data1 = str(name)
        self.data2 = str(phone)
        self.data3 = str(self.data3)
        self.data4 = str(self.data4)
        count = 0
        count2 = 0
        with open(self.loc, 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
            for row in csvreader:
                count += 1
                if row[1] == self.data1:
                    print "read exist data"
                    print row
                    count2 += 1
                    if row[3] <> self.data3:
                        self.modifydata(self.loc, count, self.data3, 3)
                        print "modified type information"
                    if row[4] <> self.data4:
                        self.modifydata(self.loc, count, self.data4, 4)
                        print "modified date information"
                    if data5 == 'renew':
                        self.modifydata(self.loc, count, 'renew', 5)
                        print "modified checking information"
                    elif data5 == 'notrenew':
                        self.modifydata(self.loc, count, 'notrenew', 5)
                        print 'file wasnt renew'
            if count2 == 0:
                print "write new data"
                with open(self.loc, 'a') as csvfile:
                    writer = csv.writer(csvfile, delimiter = ',', quotechar = '|')
                    writer.writerow([count, self.data1, self.data2, self.data3, self.data4, 'notin'])
        return count2

def imgfile_read(filelist):
    imglist = []
    for i in range(len(filelist)):
        imread_temp = cv2.imread(filelist[i], 0)
        imglist += [imread_temp,]
    return imglist

imread_file = imgfile_read(file_title)
imread_info = imgfile_read(file_info)
imread_menu = imgfile_read(file_menu)
imread_deleter = imgfile_read(file_deleter)
imread_macro = imgfile_read(file_macro)
imread_math = imgfile_read(file_math)

count_a = (len(file_title) - 1)
count_b = (count_a + len(file_info))
count_c = (count_b + len(file_menu))


#select menu included click action
def select_menu(pos, id_menu, count):
    for i in pos:
        if i[0] == id_menu and count == 0:
            pyautogui.moveTo(i[1][0] + 1, i[1][1] + 151)
            pyautogui.click(button = 'left')
    return count

class action:
    def __init__(self, num, name):
        self.num = num
        if name:
            self.name = name
        global match_list
        global file_no
        count = 0
        file_no = 0
        last_time = time.time()
        # make a background
        screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
        self.screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    ##goto main manu
    def action0(self):
        #matched_img returns local pt and global match_list
        screen_gray = matched_img(imread_file[self.num], self.screen_gray, self.num)
        screen_gray = matched_img(imread_menu[0], self.screen_gray, 10)
        count = 0
        temp_time = 0
        for i in match_list:
            if i[0] == self.num and count == 0:
                pyautogui.moveTo(450, 265)
                pyautogui.click(button = 'left')
                time.sleep(0.1)
                clipboard.copy('20120101')
                time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)                            
                pyautogui.press('down')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                pyautogui.press('tab')
                time.sleep(0.1)
                if self.name <> '0':
                    clipboard.copy(self.name)
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')
                if self.name == '0':
                    pyautogui.press('enter')
                count += 1
            else:
                select_menu(match_list, 10, count)
                while temp_time < 50 and count == 0:
                    print ("Try %s Times" %temp_time)  
                    temp_screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
                    temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
                    temp_screen = matched_img(imread_file[self.num], temp_screen, self.num)
                    for i in match_list:
                        temp_time += 1
                        if i[0] == self.num and count == 0:
                            count += 1
                            pyautogui.moveTo(450, 265)
                            pyautogui.click(button = 'left')
                            gap = 0.05
                            time.sleep(gap)
                            clipboard.copy('20120101')
                            time.sleep(gap)
                            pyautogui.hotkey('ctrl', 'v')
                            time.sleep(gap)
                            pyautogui.press('tab')
                            time.sleep(gap)
                            pyautogui.press('tab')
                            time.sleep(gap)                            
                            pyautogui.press('down')
                            time.sleep(gap)
                            pyautogui.press('tab')
                            time.sleep(gap)
                            pyautogui.press('tab')
                            time.sleep(gap)
                            if self.name <> '0':
                                clipboard.copy(self.name)
                                pyautogui.hotkey('ctrl', 'v')
                                pyautogui.press('enter')
                            if self.name == '0':
                                pyautogui.press('enter')
                
    #goto 2nd menu
    def action1(self):
        count = 0
        temp_time = 0
        screen_gray = matched_img(imread_file[self.num], self.screen_gray, self.num)
        screen_gray = matched_img(imread_menu[1], self.screen_gray, 11)
        for i in match_list:
            if i[0] == self.num:
                pyautogui.moveTo(410, 245)
                pyautogui.click(button = 'left')
                count += 1
            else:
                select_menu(match_list, 11, count)
                while temp_time < 50 and count == 0:
                    print ("Try %s Times" %temp_time)
                    temp_screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
                    temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
                    temp_screen = matched_img(imread_file[self.num], temp_screen, self.num)
                    for i in match_list:
                        temp_time += 1
                        if i[0] == self.num and self.name <> '1':
                            count += 1
                            pyautogui.moveTo(410, 245)
                            pyautogui.click(button = 'left')
                            clipboard.copy(self.name)
                            pyautogui.hotkey('ctrl', 'v')
                            pyautogui.press('enter')
                        if i[0] == self.num and self.name == '1':
                            count += 1
    def action2(self):
        temp_time = 0
        screen_gray = matched_img(imread_file[self.num], self.screen_gray, self.num)
        screen_gray = matched_img(imread_menu[2], self.screen_gray, 12)
        count = 0
        for i in match_list:
            if i[0] == self.num:
                pyautogui.moveTo(410, 215)
                count += 1
            else:
                select_menu(match_list, 12, count)
                while temp_time < 50 and count == 0:
                    print ("Try %s Times" %temp_time)  
                    temp_screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
                    temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
                    temp_screen = matched_img(imread_file[self.num], temp_screen, self.num)
                    for i in match_list:
                        temp_time += 1
                        if i[0] == self.num and self.name <> '2':
                            count += 1
                            pyautogui.moveTo(410, 215)
                            pyautogui.click(button = 'left')
                            clipboard.copy(self.name)
                            pyautogui.hotkey('ctrl', 'v')
                            pyautogui.press('enter')
                        if i[0] == self.num and self.name == '2':
                            count += 1
    #goto sms page
    def action3(self):
        screen_gray = matched_img(imread_file[self.num], self.screen_gray, self.num)
        screen_gray = matched_img(imread_menu[3], self.screen_gray, 13)
        count = 0
        for i in match_list:
            if i[0] == self.num:
                pyautogui.moveTo(705, 215)
                count += 1
                if self.name:
                    pyautogui.click(button = 'left')
                    pyautogui.hotkey('ctrl', 'v')
            else:
                select_menu(match_list, 13, count)
            return count
        
    def action4(self):
        count = 0
        temp_time = 0
        screen_gray = matched_img(imread_file[self.num], self.screen_gray, self.num)
        screen_gray = matched_img(imread_menu[4], self.screen_gray, 14)
        for i in match_list:
            if i[0] == self.num:
                pyautogui.moveTo(405, 215)
                count += 1
            else:
                select_menu(match_list, 14, count)
                while temp_time < 50 and count == 0:
                    print ("Try %s Times" %temp_time)  
                    temp_screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
                    temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
                    temp_screen = matched_img(imread_file[self.num], temp_screen, self.num)
                    for i in match_list:
                        temp_time += 1
                        if i[0] == self.num:
                            count += 1
                            pyautogui.moveTo(405, 215)
                            clipboard.copy(self.name)
                            pyautogui.hotkey('ctrl', 'v')
                            pyautogui.press('enter')
                            
    def save_ROI(self):
        temp_screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
        temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
        temp_screen = matched_img(imread_file[self.num], temp_screen, self.num)
                    
    def action_deleter(self):
        count = 0
        screen_gray = matched_img(imread_deleter[0], self.screen_gray, 'deleter')
        screen_gray = matched_img(imread_deleter[1], self.screen_gray, 'deleter1')
        for i in match_list:
            if i[0] == 'deleter1' and count == 0:
                count += 1
                pyautogui.moveTo(i[1][0] + 110, i[1][1] + 155)
                pyautogui.click(button = 'left')
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.press('tab')
                pyautogui.hotkey('ctrl','v')
                for i in range(5):
                    pyautogui.press('tab')
                    time.sleep(0.1)
                for i in range(15):
                    clipboard.copy(0)
                    pyautogui.hotkey('ctrl','c')
                    time.sleep(0.1)
                    temp_date = clipboard.paste()
                    print temp_date
                    if temp_date == '':
                        for c in range(4):
                            pyautogui.press('tab')
                            time.sleep(0.1)
                    else:
                        time.sleep(0.1)
                        pyautogui.press('delete')
                        pyautogui.press('tab')
                        time.sleep(0.1)
                        pyautogui.press('delete')
                        pyautogui.press('tab')
                        time.sleep(0.1)
                        pyautogui.press('tab')
                        time.sleep(0.1)
                        pyautogui.press('0')
                        time.sleep(0.1)
                        pyautogui.press('tab')
                temp_date = 0
                pyautogui.hotkey('ctrl','c')
                temp_date = clipboard.paste()
                if temp_date <> 0:
                    pyautogui.press('delete')
                    pyautogui.press('tab')
                    time.sleep(0.1)
                    pyautogui.press('delete')
                    pyautogui.press('tab')
                    time.sleep(0.1)
                    pyautogui.press('tab')
                    time.sleep(0.1)
                    pyautogui.press('0')
                else:
                    time.sleep(0.1)
                    
class autoaction:
    def __init__(self):
        global click_raw
        click_raw = 1
    def work1(self):
        count = 0
        temp_time = 0
        # click raws is start1
        global click_raw
        global match_list
        global prevent_action
        match_list = []
        #this will returns pt
        while temp_time < 20 and count == 0:
            print ("Try %s times" %temp_time)
            temp_time += 1
            match_list = []
            temp_screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
            temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
            temp_screen = matched_img(imread_macro[0], temp_screen, 'checker1')
            temp_screen = matched_img(imread_macro[1], temp_screen, 'checker2')
            for i in match_list:
                if i[0] == 'checker1' and count == 0:
                    for i in match_list:
                        if i[0] == 'checker2' and count == 0:
                            count += 1
                            click_raw += 1
                            max_len = (len(i) - 1)
                            pyautogui.moveTo(i[click_raw][0], i[click_raw][1] + ysize[0])
                            pyautogui.click(button = 'left')
                            if click_raw == max_len:
                                click_raw = 1
                                prevent_action = 1
                                print 'end of action'
        return count
    def work2(self):
        count = 0
        temp_time = 0
        global click_raw
        global match_list
        match_list = []
        while temp_time < 20 and count == 0:
            print ("Try %s times" %temp_time)
            temp_time += 1
            temp_screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
            temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
            temp_screen = matched_img(imread_macro[2], temp_screen, 'title6')
            temp_screen = matched_img(imread_macro[3], temp_screen, 'nameinfo')
            temp_screen = matched_img(imread_macro[4], temp_screen, 'addedfile')
            temp_screen = matched_img(imread_macro[5], temp_screen, 'addedfile2')
            for i in match_list:
                if i[0] == 'title6' and count == 0:
                    for i in match_list:
                        if i[0] == 'addedfile' and count == 0:
                            for i in match_list:
                                if i[0] == 'nameinfo' and count == 0:
                                    count += 1
                                    adjust = [(i[1][0] + 250, i[1][1] + ysize[0] + 1), (i[1][0] + 250, i[1][1] + ysize[0] + 66)]
                                    pyautogui.moveTo(adjust[0][0], adjust[0][1])
                                    pyautogui.click(button = 'left')
                                    pyautogui.hotkey('ctrl', 'c')
                                    name = clipboard.paste()
                                    pyautogui.moveTo(adjust[1][0], adjust[1][1])
                                    pyautogui.click(button = 'left')
                                    pyautogui.hotkey('ctrl', 'a')
                                    pyautogui.hotkey('ctrl', 'c')
                                    phone = clipboard.paste()
                                    pyautogui.press('esc')
                        elif i[0] == 'addedfile2' and count == 0:
                            for i in match_list:
                                if i[0] == 'nameinfo' and count == 0:
                                    count += 1
                                    adjust = [(i[1][0] + 250, i[1][1] + ysize[0] + 1), (i[1][0] + 250, i[1][1] + ysize[0] + 66)]
                                    pyautogui.moveTo(adjust[0][0], adjust[0][1])
                                    pyautogui.click(button = 'left')
                                    pyautogui.hotkey('ctrl', 'c')
                                    name = clipboard.paste()
                                    pyautogui.moveTo(adjust[1][0], adjust[1][1])
                                    pyautogui.click(button = 'left')
                                    pyautogui.hotkey('ctrl', 'a')
                                    pyautogui.hotkey('ctrl', 'c')
                                    phone = clipboard.paste()
                                    pyautogui.press('esc')                                
        #### datacard working##                            
        print name
        print phone
        datacard = csvcard()
        resultcard = datacard.card(name, phone, 'read')
        if resultcard == 0:
            adjust = [(i[1][0] + 460, i[1][1] + ysize[0] + 1), (i[1][0] + 760, i[1][1] + ysize[0] + 50)]
            print adjust
            temp_screen = np.array(ImageGrab.grab(bbox=(adjust[0][0], adjust[0][1], adjust[1][0], adjust[1][1])))
            if np.average(temp_screen) <> 0:                        
                temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
                cv2.imwrite('D:\print\pRoi\%s.png' %name, temp_screen)
                print 'renew ROI saved'
            elif np.average(temp_screen) == 0:
                print 'fail to save ROI'
            temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('D:\print\pRoi\%s.png' %name, temp_screen)
            print 'ROI saved'
        elif resultcard == 1:
            temp_img = cv2.imread('D:\print\pRoi\%s.png' %name, 0)
            temp_screen = matched_img(temp_img, temp_screen, 'record')
            match_count = len(match_list)
            for i in match_list:
                match_count -= 1
                if i[0] == 'record':
                    try:
                        datacard.card(name, phone, 'notrenew')
                    except:
                        pass
                elif match_count == 0:
                    try:
                        datacard.card(name, phone, 'renew')
                    except:
                        pass
                    adjust = [(i[1][0] + 460, i[1][1] + ysize[0] + 1), (i[1][0] + 760, i[1][1] + ysize[0] + 50)]
                    temp_screen = np.array(ImageGrab.grab(bbox=(adjust[0][0], adjust[0][1], adjust[1][0], adjust[1][1])))
                    if np.average(temp_screen) <> 0:                        
                        temp_screen = cv2.cvtColor(temp_screen, cv2.COLOR_BGR2GRAY)
                        cv2.imwrite('D:\print\pRoi\%s.png' %name, temp_screen)
                        print 'renew ROI saved'
                    elif np.average(temp_screen) == 0:
                        print 'fail to save ROI'
                    
def get_position(pos, number):
    count = 0
    for i in pos:
        if i[0] == number:
            count += 1
            find_position = i[1]
            if find_position:
                return find_position

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

def matched_roi():
    return

def match_img():
    global match_list
    global file_no
    global prevent_act
    count = 0
    file_no = 0
    last_time = time.time()
    while True:
        # make a background
        screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # find image
        if count == 0 and file_no <= count_a:
            for i in range(len(file_title)):
                screen_gray = matched_img(imread_file[i], screen_gray, file_no)
                file_no += 1
            count += 1
            print "stage1 end"
        elif count == 0 and file_no > count_a and file_no <= count_b:
            for i in range(len(file_info)):
                screen_gray = matched_img(imread_info[i], screen_gray, file_no)
                file_no += 1
            count += 1
            print "stage2 end"
        elif count == 0 and file_no > count_b and file_no <= count_c:
            for i in range(len(file_menu)):
                screen_gray = matched_img(imread_menu[i], screen_gray, file_no)
                file_no += 1
            count += 1
            print "stage3 end"
            # find image 2
            # display screen
        screen_text = 'complete in {} seconds'.format(time.time() - last_time)
        last_time = time.time()
        print type(match_list)
        if file_no == 15:
            #macro_stage(match_list, screen_gray)
            match_list = []
            file_no = 0
        count = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(screen_gray, screen_text, (10, 850), font, 1, (0, 0, 0), 2)
        cpu_usage = 'cpu: %s' % str(psutil.cpu_percent())
        cv2.putText(screen_gray, cpu_usage, (10, 880), font, 1, (0, 0, 0), 2)
        screen_gray = cv2.resize(screen_gray, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('screen_gray: test', screen_gray)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def capture_img():
    tag_no = Entry1.get()
    tag_no2 = datetime.today().strftime("%Y-%m-%d")
    cap_time = time.time()
    screen_cap = np.array(ImageGrab.grab(bbox=(250, 150, 1250, 1010)))
    screen_cap = cv2.cvtColor(screen_cap, cv2.COLOR_BGR2GRAY)
    img_background = cv2.imread('img_zero.jpg', 0)
    w, h = screen_cap.shape[:2]
    x_offset = 100
    y_offset = 100
    img_background[y_offset:y_offset + w, x_offset:x_offset + h] = screen_cap
    font = cv2.FONT_HERSHEY_SIMPLEX
    if tag_no:
        cv2.putText(img_background, '<%s> printdate: %s' %(tag_no, tag_no2), (800, 1725), font, 0.6, (0, 0, 0), 2)
        cv2.imwrite('D:\print\cv%s.png' %tag_no, img_background)
        print ('cv %s saves complete' %tag_no)
    else:
        cv2.imwrite('D:\print\cv_ran%s.png' %cap_time, img_background)
        print ('cv_ran%s saves complete' %cap_time)

def capture_img2():
#capture top screen
    #to click window menu
    count = 0
    pyautogui.moveTo(1200, 400)
    pyautogui.click(button = 'left')
    #start to capture screen
    tag_no = Entry1.get()
    tag_no2 = datetime.today().strftime("%Y-%m-%d")
    cap_time = time.time()
    screen_cap = np.array(ImageGrab.grab(bbox=(250, 150, 1250, 633)))
    screen_cap = cv2.cvtColor(screen_cap, cv2.COLOR_BGR2GRAY)
    img_background = cv2.imread('img_zero.jpg', 0)
    w, h = screen_cap.shape[:2]
    x_offset = 100
    y_offset = 250
    img_background[y_offset:y_offset + w, x_offset:x_offset + h] = screen_cap
#capture bottom screen
    print "screen1 capture complete"
    pyautogui.press('space')
    time.sleep(0.5)
    screen_cap = np.array(ImageGrab.grab(bbox=(250, 355, 1250, 1050)))
    screen_cap = cv2.cvtColor(screen_cap, cv2.COLOR_BGR2GRAY)
    w, h = screen_cap.shape[:2]
    x_offset = 100
    y_offset = 735
    img_background[y_offset:y_offset + w, x_offset:x_offset + h] = screen_cap
    font = cv2.FONT_HERSHEY_SIMPLEX
    if tag_no:
        cv2.putText(img_background, '<%s> printdate: %s' %(tag_no, tag_no2), (800, 1725), font, 0.6, (0, 0, 0), 2)
    cv2.imwrite('D:\print\cv_ran%s.png' %cap_time, img_background)
    print ('cv_ran%s saves complete' %cap_time)
    pyautogui.press('home')
    ###additional action
    global match_list
    match_list = []
    cv2.line(img_background, (845, 660), (845, 675), (125, 0, 0), 1)
    cv2.line(img_background, (940, 660), (940, 675), (125, 0, 0), 1)
    cv2.line(img_background, (845, 675), (865, 675), (125, 0, 0), 1)
    cv2.line(img_background, (920, 675), (940, 675), (125, 0, 0), 1)
    time.sleep(0.3)
    screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen_gray = matched_img(imread_deleter[0], screen_gray, 'deleter')
    screen_gray = matched_img(imread_deleter[1], screen_gray, 'deleter1')
    for i in match_list:
        if i[0] == 'deleter1':
            pyautogui.moveTo(i[1][0] + 110, i[1][1] + 155)
            pyautogui.click(button = 'left')
            time.sleep(0.05)
            while count == 0:
                pyautogui.hotkey('ctrl', 'c')
                sdate = clipboard.paste()
                print sdate
                if len(sdate) == 10:
                    count = 1
            pyautogui.press('tab')
            count = 0
            time.sleep(0.05)
            while count == 0:
                pyautogui.hotkey('ctrl', 'c')
                edate = clipboard.paste()
                print edate
                if len(edate) == 10 and edate <> sdate:
                    count = 1
    sdate = dtime.date(int(sdate[:4]), int(sdate[5:7]), int(sdate[8:10]))
    edate = dtime.date(int(edate[:4]), int(edate[5:7]), int(edate[8:10]))
    delta = edate - sdate
    delta = delta + dtime.timedelta(1)
    print delta.days
    print 'dtime saves complete'
    cv2.putText(img_background, '%d' %delta.days, (880, 680), font, 0.5, (165, 0, 0), 2)
    if tag_no:
        cv2.putText(img_background, '<%s> printdate: %s' %(tag_no, tag_no2), (800, 1725), font, 0.6, (0, 0, 0), 2)
        cv2.imwrite('D:\print\cv%s_time%s.png' %(tag_no, cap_time), img_background)
        print ('cv %s saves complete' %tag_no)
    else:
        cv2.imwrite('D:\print\cv_ran%s.png' %cap_time, img_background)
        print ('cv_ran%s saves complete' %cap_time)
    ### find images % and there is existing date data on rows then drawlines
    ### screen_row = this is intended to make a 

def capture_img3():
#capture regstration screen
    tag_no = Entry1.get()
    tag_no2 = datetime.today().strftime("%Y-%m-%d")
    cap_time = time.time()
    screen_cap = np.array(ImageGrab.grab(bbox = (250, 150, 1250, 1010)))
    screen_cap = cv2.cvtColor(screen_cap, cv2.COLOR_BGR2GRAY)
    img_background = cv2.imread('img_zero.jpg', 0)
    img_rgb = cv2.imread('src_cap.png', 0)
    w, h = screen_cap.shape[:2]
    res = cv2.matchTemplate(screen_cap, img_rgb, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        temp_offset = pt[1]
    x_offset = 100
    y_offset = 100
    img_background[y_offset:y_offset + w, x_offset:x_offset + h] = screen_cap
    for i in list(range(2)) [::-1]:
        print (i + 1)
        time.sleep(1)
    screen_cap = np.array(ImageGrab.grab(bbox = ( 250, 140, 1250, 1000)))
    screen_cap = cv2.cvtColor(screen_cap, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(screen_cap, img_rgb, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        pty = pt[1]
    img_rgb = cv2.imread('src_cap2.png', 0)
    res = cv2.matchTemplate(screen_cap, img_rgb, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        pty2 = pt[1]
    screen_cap = np.array(ImageGrab.grab(bbox = (250, pty + 11, 1250, pty2 + 195)))
    screen_cap = cv2.cvtColor(screen_cap, cv2.COLOR_BGR2GRAY)
    w, h = screen_cap.shape[:2]
    x_offset = 100
    y_offset = temp_offset - 28
    img_background[y_offset:y_offset + w, x_offset:x_offset + h] = screen_cap
    font = cv2.FONT_HERSHEY_SIMPLEX
    if tag_no:
        cv2.putText(img_background, '<%s> printdate: %s' %(tag_no, tag_no2), (800, 1725), font, 0.6, (0, 0, 0), 2)
    cv2.imwrite('D:\print\irandom%s.png' %cap_time, img_background)
    print ('irandom%s saves complete' %cap_time)
################## additional action
    


def autoMatic_button():
    match_img()

def manual_button():
    global match_list
    match_list = []
    info = Entry2.get()
    name = info[-3:]
    print ("find : %s" %name)
    info = int(info[0])
    aa = action(info, name)
    if info == 0:
        aa.action0()
    if info == 1:
        aa.action1()
    if info == 2:
        aa.action2()
    if info == 3:
        aa.action3()
    if info == 4:
        aa.action4()
    return

def delete_button():
    global match_list
    match_list = []
    aa = action(999, 999)
    aa.action_deleter()
    return

def capture_button():
    i = rb.get()
    if i == 1:
        capture_img()
    if i == 2:
        capture_img2()
    if i == 3:
        capture_img3()
    return

def caldate():
    if len(Entry1.get()) == 8 and len(Entry2.get()) == 8:
        print "cal date module"
        sdate = Entry1.get()
        edate = Entry2.get()
        sdate = dtime.date(int(sdate[:4]), int(sdate[4:6]), int(sdate[6:8]))
        edate = dtime.date(int(edate[:4]), int(edate[4:6]), int(edate[6:8]))
        delta = edate - sdate
        delta = delta + dtime.timedelta(1)
        print delta.days
    if len(Entry1.get()) == 8 and len(Entry2.get()) < 8:
        sdate = Entry1.get()
        sdate = dtime.date(int(sdate[:4]), int(sdate[4:6]), int(sdate[6:8]))
        afterday = sdate + dtime.timedelta(int(Entry2.get()) - 1)
        print afterday
    return

def card_button():
    global prevent_action
    prevent_action = 0
    if rb.get() == 6:
        atext = 'read'
    elif Entry2.get() == 'init':
        abc = csvcard()
        abc.firstwrite()
        print "csv was cleaned"
    else:
        autocheck = autoaction()
        while prevent_action == 0:
            autocheck.work1()
            autocheck.work2()
            pyautogui.press('backspace')        
    return

def test_button():
    test_capture()
    
    return
'''
    clipboard.copy("좋아")
    temp_paste2 = clipboard.paste()
    print temp_paste2
    temp_paste = clipboard.paste()
    print temp_paste
    #manual_match(0, name)
'''

def radio_sel():
    return


App = Tkinter.Tk()
App.title("Testsample")

rb = Tkinter.IntVar()
rb.set(None)

Button1 = Tkinter.Button(App, text = 'capture', width = 10, command = capture_button)
Button1.grid(row=0,column=0)
Button2 = Tkinter.Button(App, text = 'auto', width = 10, command = autoMatic_button)
Button2.grid(row=0,column=1)
Button4 = Tkinter.Button(App, text = 'caldate', width = 10, command = caldate)
Button4.grid(row=1,column=0)
Button3 = Tkinter.Button(App, text = 'delete', width = 10, command = delete_button)
Button3.grid(row=1,column=1)
Button4 = Tkinter.Button(App, text = 'card', width = 10, command = card_button)
Button4.grid(row=2,column=0)
Button3 = Tkinter.Button(App, text = 'test', width = 10, command = test_button)
Button3.grid(row=2,column=1)
Entry1 = Tkinter.Entry(App, width = 22)
Entry1.grid(row = 3, columnspan = 2)
Entry2 = Tkinter.Entry(App, width = 22)
Entry2.grid(row = 4, columnspan = 2)
Button5 = Tkinter.Button(App, text = 'findManual', width = 21, command = manual_button)
Button5.grid(row=5,columnspan=2)
Radio1 = Tkinter.Radiobutton(App, text = 'capture1', variable = rb, value = 1)
Radio1.grid(row=0, column = 3)
Radio2 = Tkinter.Radiobutton(App, text = 'capture2', variable = rb, value = 2)
Radio2.grid(row=1, column = 3)
Radio3 = Tkinter.Radiobutton(App, text = 'capture3', variable = rb, value = 3)
Radio3.grid(row=2, column = 3)
Radio4 = Tkinter.Radiobutton(App, text = 'register  ', variable = rb, value = 4)
Radio4.grid(row=3, column = 3)
Radio4 = Tkinter.Radiobutton(App, text = 'change  ', variable = rb, value = 5)
Radio4.grid(row=4, column = 3)
Radio4 = Tkinter.Radiobutton(App, text = 'read      ', variable = rb, value = 6)
Radio4.grid(row=5, column = 3)

App.mainloop()
