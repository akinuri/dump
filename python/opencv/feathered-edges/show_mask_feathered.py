import os
import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

from pprint import pprint

img_path = Path(sys.argv[1])

orig_img          = cmyk_to_bgr(str(img_path))
orig_threshed     = threshold(orig_img, 240, type=cv2.THRESH_BINARY_INV)
orig_contours     = find_contours(orig_threshed)
orig_mask         = mask_from_contours(orig_img, orig_contours)
orig_mask_dilated = dilate_mask(orig_mask, 41)

orig_out_contours = draw_contours(orig_img, orig_contours)

dilated_blurred  = cv2.GaussianBlur(orig_mask_dilated, (41,41), 0)
dilated_threshed = threshold(dilated_blurred, 1)
dilated_contours = find_contours(dilated_threshed)
dilated_contour  = sorted(dilated_contours, key=cv2.contourArea)[-1]

x, y, w, h = cv2.boundingRect(dilated_contour)
img_cropped     = orig_img[y:y+h, x:x+w]
dilated_cropped = dilated_blurred[y:y+h, x:x+w]

dilated_out_contours = draw_contours(orig_img, dilated_contours)



bg = numpy.full(img_cropped.shape, (0,0,255), dtype=numpy.uint8)

mask_blurred_3chan = cv2.cvtColor(dilated_cropped, cv2.COLOR_GRAY2BGR).astype("float") / 255.
img = img_cropped.astype("float") / 255.
bg  = bg.astype("float") / 255.
out = bg * (1 - mask_blurred_3chan) + img * mask_blurred_3chan

pprint(out.shape)
pprint(out)

# cv2.imshow("orig_img", orig_img)
# cv2.imshow("orig_mask_dilated", orig_mask_dilated)
# cv2.imshow("orig_out_contours", orig_out_contours)

# cv2.imshow("dilated_blurred", dilated_blurred)
# cv2.imshow("dilated_threshed", dilated_threshed)
# cv2.imshow("dilated_out_contours", dilated_out_contours)

# cv2.imshow("img_cropped", img_cropped)
# cv2.imshow("dilated_cropped", dilated_cropped)
# cv2.imshow("background", background)


cv2.imwrite(str(img_path.parent) + "/" + img_path.stem + "_feathered"   + img_path.suffix, out)
cv2.imwrite(str(img_path.parent) + "/" + img_path.stem + "_feathered"   + img_path.suffix, out)
cv2.imshow("out", out)


cv2.waitKey(0)
cv2.destroyAllWindows()