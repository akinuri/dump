@echo off

"C:\\Program Files\\ImageMagick-7.0.7-Q16\\magick.exe" convert "images\\azra-cmyk-8-input.jpg" "images\\azra-rgb-8-output.jpg"
"C:\\Program Files\\ImageMagick-7.0.7-Q16\\magick.exe" convert "images\\delta-cmyk-16-input.tif" "images\\delta-rgb-8-output.jpg"

echo done

pause