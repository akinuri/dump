@echo off

C:\Users\%username%\AppData\Local\Programs\Python\Python36\python.exe "%~dp0\image_open.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE