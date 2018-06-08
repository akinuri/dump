@echo off

"C:\OSGeo4W64\bin\gdal_translate.exe" -scale -ot byte -of PNG "C:\Users\%username%\Documents\GitHub\dump\tif-2-jpg\images\cmyk-16.tif" "cmyk-16.png"

pause