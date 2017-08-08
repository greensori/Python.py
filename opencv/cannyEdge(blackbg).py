import numpy as np
import cv2
from PIL import ImageGrab

xsize = (0, 1250)
ysize = (150, 1055)

def canny(screen):
    img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.Canny(img_gray, threshold1=200, threshold2=300)
    return processed_img
    
while(True):
    screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
    cv2.imshow('PC canny(black) screen', canny(screen))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
        
