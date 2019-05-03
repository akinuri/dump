import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

img_path = Path(sys.argv[1])

orig_img      = cmyk_to_rgb(str(img_path))
orig_threshed = cv_threshold(orig_img, 240, type=cv2.THRESH_BINARY_INV)
orig_contours = find_contours(orig_threshed)
orig_mask     = mask_from_contours(orig_img, orig_contours)
orig_output   = draw_contours(orig_img, orig_contours)

dilated_mask     = dilate_mask(orig_mask, 50)
dilated_contours = find_contours(dilated_mask)
dilated_output   = draw_contours(orig_img, dilated_contours)

# pass 1
smooth_mask_blurred   = cv2.GaussianBlur(dilated_mask, (21,21), 0)
smooth_mask_threshed1 = cv_threshold(smooth_mask_blurred)

# pass 2
smooth_mask_blurred   = cv2.GaussianBlur(smooth_mask_threshed1, (21,21), 0)
smooth_mask_threshed2 = cv_threshold(smooth_mask_blurred)

# find contours from smoothened mask
smooth_mask_contours = find_contours(smooth_mask_threshed2)
# draw the contours on the original image
smooth_mask_output   = draw_contours(orig_img, smooth_mask_contours)

cv2.imshow("dilated_output", dilated_output)
cv2.imshow("smooth_mask_output", smooth_mask_output)

cv2.waitKey(0)
cv2.destroyAllWindows()
