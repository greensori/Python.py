from msvcrt import getch 

#when press 'esc' key then print 'esc press'
#scripts only works at cmd screen
while True:
    key = ord(getch())
    if key == 27:
        print 'esc press'
