import sys
from pathlib import Path
from helpers_cv2 import *
import cv2
import numpy

from pprint import pprint

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
mask_draw_con = draw_contours(img, mask_contours)

x, y, w, h    = cv2.boundingRect(mask_contour)
img_cropped   = img[y:y+h, x:x+w]
mask_cropped  = mask_blurred[y:y+h, x:x+w]

background = numpy.full(img_cropped.shape, (200,240,200), dtype=numpy.uint8)

output = alpha_blend(background, img_cropped, mask_cropped)

thumb_margin = 20
thumb_w = 200
thumb_h = 213

thumb_w2 = math.floor((img_cropped.shape[1] / img.shape[1]) * thumb_w)
thumb_h2 = math.floor((img_cropped.shape[0] / img.shape[0]) * thumb_h)
thumb_margin2 = thumb_w - thumb_w2

debug = numpy.full((530, (thumb_w + thumb_margin)*7 + 20, 3), 200, dtype=numpy.uint8)

thumb_img           = cv2.resize(img.copy(), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_mask          = cv2.resize(gray_to_bgr(mask.copy()), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_mask_dilated  = cv2.resize(gray_to_bgr(mask_dilated.copy()), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_mask_smooth   = cv2.resize(gray_to_bgr(mask_smooth.copy()), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_mask_blurred  = cv2.resize(gray_to_bgr(mask_blurred.copy()), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_mask_threshed = cv2.resize(gray_to_bgr(mask_threshed.copy()), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_mask_contours = cv2.resize(gray_to_bgr(mask_draw_con.copy()), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_img_cropped   = cv2.resize(img_cropped.copy(), (thumb_w2, thumb_h2), interpolation = cv2.INTER_AREA)
thumb_mask_cropped  = cv2.resize(mask_cropped.copy(), (thumb_w2, thumb_h2), interpolation = cv2.INTER_AREA)
thumb_background    = cv2.resize(background.copy(), (thumb_w2, thumb_h2), interpolation = cv2.INTER_AREA)
thumb_blended       = cv2.resize(output.copy(), (thumb_w2, thumb_h2), interpolation = cv2.INTER_AREA)

x_text = 20
x_off = thumb_margin
y_off = 20
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_img
cv2.putText(debug, "image", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + thumb_margin
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_mask
cv2.putText(debug, "mask", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + thumb_margin
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_mask_dilated
cv2.putText(debug, "dilated", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + thumb_margin
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_mask_smooth
cv2.putText(debug, "smooth", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + thumb_margin
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_mask_blurred
cv2.putText(debug, "blurred", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + thumb_margin
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_mask_threshed
cv2.putText(debug, "threshed", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + thumb_margin
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_mask_contours
cv2.putText(debug, "threshed contours", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = thumb_margin
y_off = y_off + thumb_h + thumb_margin*2
debug[y_off : y_off + thumb_h2, x_off : x_off + thumb_w2] = thumb_img_cropped
cv2.putText(debug, "img_cropped", (x_off + x_text, y_off + thumb_h), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w2 + thumb_margin
debug[y_off : y_off + thumb_h2, x_off : x_off + thumb_w2] = thumb_mask_cropped
cv2.putText(debug, "mask_cropped", (x_off + x_text, y_off + thumb_h), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w2 + thumb_margin
debug[y_off : y_off + thumb_h2, x_off : x_off + thumb_w2] = thumb_background
cv2.putText(debug, "background", (x_off + x_text, y_off + thumb_h), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w2 + thumb_margin
debug[y_off : y_off + thumb_h2, x_off : x_off + thumb_w2] = thumb_blended
cv2.putText(debug, "alpha blend", (x_off + x_text, y_off + thumb_h), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

cv2.imwrite(str(img_path.parent) + "/" + img_path.stem + "_mask_debug2"   + img_path.suffix, debug)
cv2.imwrite(str(img_path.parent) + "/" + img_path.stem + "_mask_feathered"   + img_path.suffix, output)

cv2.imshow("debug", debug)
cv2.imshow("output", output)

cv2.waitKey(0)
cv2.destroyAllWindows()