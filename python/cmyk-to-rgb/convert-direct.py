from PIL import Image
from PIL import ImageCms

img_original = "input_azra.jpg"

img = Image.open(img_original);

print("image : " + img_original)
print("image mode: " + img.mode)
print("converting to RGB")

img = img.convert("RGB")

img.save("output_rgb_direct.jpg", quality=95)

print("done")

input()
