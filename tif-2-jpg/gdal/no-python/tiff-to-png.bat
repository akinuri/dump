@echo off

"C:\Program Files\GDAL\gdal_translate.exe" -scale -ot byte -of PNG "C:\Users\%username%\Documents\GitHub\dump\tif-2-jpg\images\cmyk-16.tif" "cmyk-16.png"

pause