from msvcrt import getch 

#when press 'esc' key then print 'esc press'
while True:
    key = ord(getch())
    if key == 27:
        print 'esc press'
