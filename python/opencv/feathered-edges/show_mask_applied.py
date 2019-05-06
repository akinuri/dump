import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

img_path = Path(sys.argv[1])

img      = cmyk_to_bgr(str(img_path))
threshed = threshold(img, 240, type=cv2.THRESH_BINARY_INV)
contours = find_contours(threshed)
mask     = mask_from_contours(img, contours)
mask     = dilate_mask(mask, 50)
# mask     = cv2.GaussianBlur(mask, (51,51), 0)
crop     = cv2.bitwise_or(img, img, mask=mask)

bg      = cv2.imread("bg.jpg")
bg_mask = cv2.bitwise_not(mask)
bg_crop = cv2.bitwise_or(bg, bg, mask=bg_mask)

final   = cv2.bitwise_or(crop, bg_crop)

cv2.imshow("debug", final)

cv2.waitKey(0)
cv2.destroyAllWindows()