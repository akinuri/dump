@echo off

cd "C:\ProgramData\Miniconda3\Library\bin"

gdal_translate -of PNG "C:\Users\%username%\Documents\GitHub\dump\tif-2-jpg\images\cmyk-8.tif" "C:\Users\%username%\Documents\GitHub\dump\tif-2-jpg\gdal\miniconda3\output\cmyk-8.png"

pause