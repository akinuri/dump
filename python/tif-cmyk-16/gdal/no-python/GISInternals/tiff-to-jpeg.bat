@echo off

"C:\Program Files\GDAL\gdal_translate.exe" -scale -ot byte -of GTIFF -co PHOTOMETRIC=CMYK "C:\Users\%username%\Documents\GitHub\dump\python\tif-cmyk-16\images\cmyk-16.tif" "cmyk-16.jpg"

pause