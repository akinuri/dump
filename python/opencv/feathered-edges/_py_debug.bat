@echo off

REM python %1

REM python "%~dp0\debug_alpha_blend.py" %*


REM python "%~dp0\output_crop.py" %*
REM python "%~dp0\output_mask_dilated.py" %*

REM python "%~dp0\show_contours.py" %*
REM python "%~dp0\show_cropped.py" %*
REM python "%~dp0\show_contours_dilated.py" %*
REM python "%~dp0\show_mask_applied.py" %*
python "%~dp0\show_mask_feathered.py" %*
REM python "%~dp0\show_states.py" %*

IF %ERRORLEVEL% NEQ 0 PAUSE