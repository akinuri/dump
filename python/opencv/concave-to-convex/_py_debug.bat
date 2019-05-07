@echo off

REM python %1

REM python "%~dp0\show_mask.py" %*
python "%~dp0\show_convex_hull.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE