@echo off

cd "C:\Users\%username%\AppData\Local\Programs\Python\Python36\Lib\site-packages\osgeo"

gdal_translate -of JPEG "C:\Users\%username%\Documents\GitHub\dump\tif-2-jpg\images\cmyk-8.tif" "C:\Users\%username%\Documents\GitHub\dump\tif-2-jpg\gdal\Gohlke-Pythonlibs\output\cmyk-8.jpg"

pause