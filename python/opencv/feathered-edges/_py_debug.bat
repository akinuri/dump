@echo off

REM python %1

REM python "%~dp0\draw_states.py" %*
REM python "%~dp0\show_contours.py" %*
REM python "%~dp0\output_crop.py" %*
REM python "%~dp0\show_cropped.py" %*
REM python "%~dp0\show_dilated_contours.py" %*
REM python "%~dp0\output_mask_dilated.py" %*
python "%~dp0\show_mask_applied.py" %*
REM python "%~dp0\remove_bg.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE