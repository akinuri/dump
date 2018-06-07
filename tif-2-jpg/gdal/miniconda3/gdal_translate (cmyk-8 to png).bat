@echo off

cd "C:\ProgramData\Miniconda3\Library\bin"

gdal_translate -of PNG "C:\Users\%username%\Documents\GitHub\dump\gdal\images\cmyk-8.tif" "C:\Users\%username%\Documents\GitHub\dump\gdal\miniconda3\gdal_translate\output\cmyk-8.png"

pause