import os
cwd = os.path.dirname(os.path.abspath(__file__))

from PIL import Image

img_input  = "input_cmyk-16.tif"
img_output = "output_cmyk-8.tif"

try:
    img = Image.open(img_input)
except OSError as e:
    print(e)
    
    print("\nconverting it to 8-bit\n")
    
    import subprocess
    args = ["C:\\Program Files\\GDAL\\gdal_translate.exe", "-ot", "byte", "-of", "GTIFF", "-scale", "-co", "PHOTOMETRIC=CMYK", img_input, img_output]
    subprocess.call(args)
    
    print("\nopening converted file")
    
    img = Image.open(img_output)
    
    print("success: " + img_output)
    
else:
    print("success: " + img_name)

input()