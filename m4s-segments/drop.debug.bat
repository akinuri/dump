@echo off

REM Allows to keep the console window open after an error

python "%1"

IF %ERRORLEVEL% NEQ 0 PAUSE