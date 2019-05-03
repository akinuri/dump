import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

img_path = Path(sys.argv[1])

orig_img      = cmyk_to_bgr(str(img_path))
orig_threshed = cv_threshold(orig_img, 240, type=cv2.THRESH_BINARY_INV)
orig_contours = find_contours(orig_threshed)
orig_mask     = mask_from_contours(orig_img, orig_contours)
orig_output   = draw_contours(orig_img, orig_contours)

dilated_mask     = dilate_mask(orig_mask, 50)
dilated_contours = find_contours(dilated_mask)
dilated_output   = draw_contours(orig_img, dilated_contours)

cv2.imshow("orig_output", orig_output)
cv2.imshow("dilated_output", dilated_output)

cv2.waitKey(0)
cv2.destroyAllWindows()
