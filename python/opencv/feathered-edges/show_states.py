import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

img_path = Path(sys.argv[1])

img      = cmyk_to_bgr(str(img_path))
threshed = threshold(img, 240, type=cv2.THRESH_BINARY_INV)
contours = find_contours(threshed)
contour  = sorted(contours, key=cv2.contourArea)[-1]

x, y, w, h = cv2.boundingRect(contour)

img_contours = cv2.drawContours(img.copy(), contours, -1, (0,255,0), 2)
cv2.rectangle(img_contours, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow("img", img)
cv2.imshow("threshed", threshed)
cv2.imshow("img_contours", img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
