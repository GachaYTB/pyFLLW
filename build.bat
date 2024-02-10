@echo off
REM Don't tell me why its \OneDrive\Bureau\Codes, im french + i stock almost all of my creations in a folder named Codes
cd /d C:\Users\%USERNAME%\OneDrive\Bureau\Codes\pyFLLW
pyinstaller main.py
echo Successfully built pyFLLW.
echo You will find the .exe file in .\dist\main\main.exe
cd /d .\dist\main
start "" "main.exe"