import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

img_path = Path(sys.argv[1])

orig_img      = cmyk_to_bgr(str(img_path))
orig_threshed = threshold(orig_img, 240, type=cv2.THRESH_BINARY_INV)
orig_contours = find_contours(orig_threshed)
orig_mask     = mask_from_contours(orig_img, orig_contours)
orig_output   = draw_contours(orig_img, orig_contours)

dilated_mask  = dilate_mask(orig_mask, 50)

new_img_path = str(img_path.parent) + "/" + img_path.stem + "_mask_dilated" + img_path.suffix
cv2.imwrite(new_img_path, dilated_mask)
