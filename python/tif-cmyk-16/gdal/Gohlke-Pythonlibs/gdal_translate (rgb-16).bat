@echo off

cd "C:\Users\%username%\AppData\Local\Programs\Python\Python36\Lib\site-packages\osgeo"

gdal_translate -of JPEG "C:\Users\%username%\Documents\GitHub\dump\tif-2-jpg\images\rgb-16.tif" "C:\Users\%username%\Documents\GitHub\dump\tif-2-jpg\gdal\Gohlke-Pythonlibs\output\rgb-16.jpg"

pause