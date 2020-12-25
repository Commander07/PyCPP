@echo off
echo WARNING: This does currently not work. You need to build it your self.
title build
@echo on
gcc -c -DBUILD_DLL dll\dllmain.cpp -o tmp\dllmain.o
gcc -shared -o ..\dllmain.dll tmp\dllmain.o -Wl,--add-stdcall-alias
@echo off
del /F /Q /S tmp\*
pause