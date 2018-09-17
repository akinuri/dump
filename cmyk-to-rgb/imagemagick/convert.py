from __future__ import print_function
from wand.image import Image

with Image(filename="images\\delta-cmyk-16-input.tif") as img:
    img.format = "jpeg"
    img.save(filename="new.jpg")

input("Done")