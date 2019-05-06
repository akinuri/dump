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

cropped = img[y:y+h, x:x+w]

cv2.imwrite(str(img_path.parent) + "/" + img_path.stem + "_cropped"   + img_path.suffix, cropped)

