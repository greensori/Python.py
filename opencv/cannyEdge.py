#example of canny edge scripts
#screen size is 1250x905
#target img is PC screen

import cv2
import numpy as np
from PIL import ImageGrab

xsize = (0, 1250)
ysize = (150, 1055)


def canny(screen):
    img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
    canny_edge = cv2.Canny(img_gray, 10, 70)
    ret, mask = cv2.threshold(canny_edge, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


while True:
    screen = np.array(ImageGrab.grab(bbox=(xsize[0], ysize[0], xsize[1], ysize[1])))
    cv2.imshow('PC canny screen', canny(screen))
    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
    break
