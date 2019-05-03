import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

img_path = Path(sys.argv[1])

img      = cmyk_to_bgr(str(img_path))
threshed = cv_threshold(img, 240, type=cv2.THRESH_BINARY_INV)
contours = find_contours(threshed)
mask     = mask_from_contours(img, contours)

dilated_mask = dilate_mask(mask, 50)

cv2.imshow("mask", mask)
cv2.imshow("dilated_mask", dilated_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()