@echo off
title OpenCats V2
python check.py
cd src
start python init.py
echo HTTP Server run on http://127.0.0.1:9000/.
python -m http.server 9000 --directory ./web/
echo 程序已退出。
pause