import sys
from pathlib import Path

from PIL import Image
from PIL import ImageCms
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# https://docs.opencv.org/master/index.html
import cv2
import numpy

# drop an image on this script file
img_path = Path(sys.argv[1])

# open image with Pillow and convert it to RGB if the image is CMYK
img = Image.open(str(img_path))
if img.mode == "CMYK":
    img = ImageCms.profileToProfile(img, "Color Profiles\\USWebCoatedSWOP.icc", "Color Profiles\\sRGB_Color_Space_Profile.icm", outputMode="RGB")

img      = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
gray     = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)[1]
kernel   = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
morphed  = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)
contours = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
contour  = sorted(contours, key=cv2.contourArea)[-1]

x, y, w, h = cv2.boundingRect(contour)

final = cv2.drawContours(img, contours, -1, (0,255,0), 2)
cv2.rectangle(final, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow("final", final)
cv2.waitKey(0)
cv2.destroyAllWindows()