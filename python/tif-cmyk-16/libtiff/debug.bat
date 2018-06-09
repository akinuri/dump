@echo off

C:\Users\%username%\AppData\Local\Programs\Python\Python36\python.exe "%~dp0\test.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE