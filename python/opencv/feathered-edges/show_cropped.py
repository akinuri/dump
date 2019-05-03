import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy
import math

img_path = Path(sys.argv[1])

img      = cmyk_to_bgr(str(img_path))
threshed = cv_threshold(img, 240, type=cv2.THRESH_BINARY_INV)
contours = find_contours(threshed)
contour  = sorted(contours, key=cv2.contourArea)[-1]

x, y, w, h = cv2.boundingRect(contour)

cropped = img[y:y+h, x:x+w]

cropped_h, cropped_w, cropped_ch = cropped.shape
new_w  = int(round(cropped_w * 1.1))
new_h  = int(round(cropped_h * 1.1))

canvas = numpy.zeros((new_h, new_w, 3), numpy.uint8)
canvas.fill(255)

offs_x = int(math.floor((new_w - cropped_w) /2))
offs_y = int(math.floor((new_h - cropped_h) /2))

canvas[offs_y:offs_y+cropped_h, offs_x:offs_x+cropped_w] = cropped

cv2.imshow("img", img)
cv2.imshow("cropped", cropped)
cv2.imshow("canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
