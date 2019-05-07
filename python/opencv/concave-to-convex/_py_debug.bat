@echo off

REM python %1

python "%~dp0\show_mask.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE