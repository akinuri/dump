import sys
from pathlib import Path
import cv2
import numpy
from helpers_cv2 import *

img_path = Path(sys.argv[1])

img      = cmyk_to_bgr(str(img_path))
threshed = threshold(img, 240, type=cv2.THRESH_BINARY_INV)
contours = find_contours(threshed)

dilation_length = 51
blur_length     = 51

mask         = mask_from_contours(img, contours)
mask_dilated = dilate_mask(mask, dilation_length)
mask_smooth  = smooth_mask(mask_dilated, odd(dilation_length * 1.5))
mask_blurred = cv2.GaussianBlur(mask_smooth, (blur_length, blur_length), 0)
mask_blurred = cv2.cvtColor(mask_blurred, cv2.COLOR_GRAY2BGR)

mask_threshed = threshold(mask_blurred, 1)
mask_contours = find_contours(mask_threshed)
mask_contour  = max_contour(mask_contours)

x, y, w, h = cv2.boundingRect(mask_contour)

img_cropped  = img[y:y+h, x:x+w]
mask_cropped = mask_blurred[y:y+h, x:x+w]
background   = numpy.full(img_cropped.shape, (200,240,200), dtype=numpy.uint8)
output       = alpha_blend(background, img_cropped, mask_cropped)

# cv2.imwrite(str(img_path.parent) + "/" + img_path.stem + "_feathered2"   + img_path.suffix, output)

cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()