@ECHO OFF

title Compile Filer
echo Compiling Filer.

pyinstaller.exe --icon=Logo.ico --onefile main.py
move dist\main.exe .\Filer.exe

rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__

del main.spec

cls
if EXIST .\Filer.exe goto Compiled
if NOT EXIST .\Filer.exe goto NotCompiled

:Compiled
echo Filer Compiled Successfully!
echo Get ready to Encrypt all your Files!
echo|set /p="Continue."
pause >nul
exit

:NotCompiled
echo Can't Compile Filer!
echo|set /p="Continue."
pause >nul
exit
