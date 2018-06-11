import os, sys
cwd = os.path.dirname(os.path.abspath(__file__))

from PIL import Image
from PIL import ImageCms

img_original = "input_azra.jpg"

img = Image.open(img_original);

print("image : " + img_original)
print("image mode: " + img.mode)
print("converting to RGB using profile")

if img.mode == "CMYK":
    img = ImageCms.profileToProfile(img, cwd + "\\Color_Profiles\\USWebCoatedSWOP.icc", cwd + "\\Color_Profiles\\sRGB_Color_Space_Profile.icm", outputMode="RGB")

img.save("output_rgb_profile.jpg", quality=95)

print("done")

input()
