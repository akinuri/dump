@echo off

REM "C:\\Program Files\\GDAL\\gdal_translate.exe" -ot byte -of GTIFF -scale -co PHOTOMETRIC=CMYK input_cmyk-16.tif output_cmyk-8.tif
"C:\\Program Files\\GDAL\\gdal_translate.exe" -ot byte -of GTIFF -scale -co SOURCE_ICC_PROFILE=Color_Profiles\\USWebCoatedSWOP.icc input_cmyk-16.tif output_cmyk-8.tif

pause