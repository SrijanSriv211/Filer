@ECHO OFF
title Compiler

echo Compiling FIler
pyinstaller.exe --icon=Icon.ico -F --onefile Filer.py

exit
