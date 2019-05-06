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

crop = cv2.bitwise_or(img, img, mask=mask)

bg      = cv2.imread("bg.jpg")
bg_mask = cv2.bitwise_not(mask)
bg_crop = cv2.bitwise_or(bg, bg, mask=bg_mask)

final = cv2.bitwise_or(crop, bg_crop)




thumb_w = 200
thumb_h = 213

debug = numpy.full((530, 930, 3), 200, dtype=numpy.uint8)

thumb_img  = cv2.resize(img.copy(), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_mask = cv2.resize(gray_to_bgr(mask.copy()), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_crop = cv2.resize(crop.copy(), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)

thumb_bg      = cv2.resize(bg.copy(), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_bg_mask = cv2.resize(gray_to_bgr(bg_mask.copy()), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)
thumb_bg_crop = cv2.resize(bg_crop.copy(), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)

thumb_final   = cv2.resize(final.copy(), (thumb_w, thumb_h), interpolation = cv2.INTER_AREA)

x_text = 20
x_off = 20
y_off = 20
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_img
cv2.putText(debug, "image", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + 20
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_mask
cv2.putText(debug, "mask", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + 20
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_crop
cv2.putText(debug, "crop", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))


x_off = 20
y_off = 20 + thumb_h + 40
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_bg
cv2.putText(debug, "bg", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + 20
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_bg_mask
cv2.putText(debug, "bg_mask", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))

x_off = x_off + thumb_w + 20
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_bg_crop
cv2.putText(debug, "bg_crop", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))


# y_off = y_off - 20 - int(thumb_h/2)
x_off = x_off + thumb_w + 50
debug[y_off : y_off + thumb_h, x_off : x_off + thumb_w] = thumb_final
cv2.putText(debug, "crop + bg_crop", (x_off + x_text, y_off + thumb_h + x_text), cv2.FONT_HERSHEY_PLAIN , 1, (0,0,0))


# cv2.imwrite(str(img_path.parent) + "/" + img_path.stem + "_mask_debug"   + img_path.suffix, debug)
# cv2.imwrite(str(img_path.parent) + "/" + img_path.stem + "_mask_final"   + img_path.suffix, final)

cv2.imshow("debug", debug)

cv2.waitKey(0)
cv2.destroyAllWindows()