echo 'WARNING: This does currently not work. You need to build it your self.'
gcc -c -DBUILD_DLL dll/dllmain.cpp -o tmp/dllmain.o
gcc -shared -o ../dllmain.dll tmp/dllmain.o -Wl,--add-stdcall-alias
rm tmp/*
echo 'Press any key to exit.'
read -n 1 -s