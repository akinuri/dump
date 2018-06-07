@echo off

C:\ProgramData\Miniconda3\python.exe "%~dp0\open_tiff.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE