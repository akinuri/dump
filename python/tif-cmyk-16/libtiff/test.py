import numpy as np
from PIL import Image
from libtiff import TIFF

input_img = TIFF.open("input_cmyk-16.tif").read_image()

def reduceDepth(image, display_min, display_max):
    image -= display_min
    image = np.floor_divide(image, (display_min - display_max + 1) / 256)
    image = image.astype(np.uint8)
    return image

v8 = reduceDepth(input_img, 0, 65536)

im = Image.fromarray(v8)
im = im.convert("RGB")
im.save("output_rgb-8.jpg")

input("Done")