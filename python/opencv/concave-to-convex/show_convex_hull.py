import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

from pprint import pprint

img_path = Path(sys.argv[1])

img = cmyk_to_bgr(str(img_path))

threshed = threshold(img, 240, type=cv2.THRESH_BINARY_INV)
contours = find_contours(threshed)

mask        = mask_from_contours(img, contours)
mask_smooth = smooth_mask(mask, 51)
mask_dilate = dilate_mask(mask_smooth, 51)
mask_smooth = smooth_mask(mask_dilate, 51)

# convex hull ops
contours = find_contours(mask_smooth)
hull = []
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))
hull = mask_from_contours(img, hull)

cv2.imshow("hull", hull)

# cv2.imwrite(str(Path(img_path).parent) + "\\" + img_path.stem + "_mask_hull" + img_path.suffix, hull)

cv2.waitKey(0)
cv2.destroyAllWindows()