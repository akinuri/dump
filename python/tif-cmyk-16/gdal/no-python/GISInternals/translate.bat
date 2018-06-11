@echo off

"C:\\Program Files\\GDAL\\gdal_translate.exe" -ot byte -of GTIFF -scale -co PHOTOMETRIC=CMYK input_delta-cmyk-16.tif "output_delta-cmyk-8 (translate).tif"

pause