@echo off

REM python %1

REM python "%~dp0\draw_states.py" %*
python "%~dp0\show_contours.py" %*
REM python "%~dp0\remove_bg.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE