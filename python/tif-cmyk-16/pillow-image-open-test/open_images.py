import getpass

from PIL import Image
from PIL import ImageCms

username = getpass.getuser()

img_dir = "C:\\Users\\" + username + "\\Documents\\GitHub\\dump\\python\\tif-cmyk-16\\images"

images = [
    "cmyk-8.tif",
    "cmyk-16.tif",
    "rgb-8.tif",
    "rgb-16.tif",
]

for img_name in images:
    path = img_dir + "\\" + img_name
    try:
        img = Image.open(path)
    except OSError as e:
        print(e)
    else:
        print("success: " + img_name)

input()