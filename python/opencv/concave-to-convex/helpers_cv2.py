import os
from pathlib import Path
import math
import cv2
import numpy
from PIL import Image
from PIL import ImageCms
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

cwd = os.path.dirname(os.path.abspath(__file__))

def cmyk_to_bgr(cmyk_img):
    img = Image.open(cmyk_img)
    if img.mode == "CMYK":
        img = ImageCms.profileToProfile(img, "\\Color Profiles\\USWebCoatedSWOP.icc", cwd + "\\Color Profiles\\sRGB_Color_Space_Profile.icm", outputMode="RGB")
    return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

def gray_to_bgr(img):
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img

def threshold(img, thresh=128, maxval=255, type=cv2.THRESH_BINARY):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshed = cv2.threshold(img, thresh, maxval, type)[1]
    return threshed

def find_contours(img):
    kernel   = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed  = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    contours = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours[-2]

def draw_contours(src_img, contours):
    canvas = cv2.drawContours(src_img.copy(), contours, -1, (0,255,0), 2)
    x, y, w, h = cv2.boundingRect(contours[-1])
    cv2.rectangle(canvas, (x,y), (x+w,y+h), (0,0,255), 2)
    return canvas

def max_contour(contours):
    return sorted(contours, key=cv2.contourArea)[-1]

def mask_from_contours(ref_img, contours):
    mask = numpy.zeros(ref_img.shape, numpy.uint8)
    mask = cv2.drawContours(mask, contours, -1, (255,255,255), -1)
    return cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

def dilate_mask(mask, kernel_size=11):
    kernel  = numpy.ones((kernel_size, kernel_size), numpy.uint8)
    dilated = cv2.dilate(mask, kernel, iterations=1)
    return dilated

def smooth_mask(mask, kernel_size=11):
    blurred  = cv2.GaussianBlur(mask, (kernel_size, kernel_size), 0)
    threshed = threshold(blurred)
    return threshed

def alpha_blend(background, foreground, mask):
    mask       = mask.astype("float") / 255.
    foreground = foreground.astype("float") / 255.
    background = background.astype("float") / 255.
    out        = background * (1 - mask) + foreground * mask
    out        = (out * 255).astype("uint8")
    return out

def odd(num):
    if isinstance(num, float):
        num = math.floor(num)
    if num % 2 == 0:
        num = num - 1
    return num
