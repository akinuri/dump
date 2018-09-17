@echo off

C:\Users\%username%\AppData\Local\Programs\Python\Python36\python.exe "%~dp0\convert.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE