@echo off
title OpenCats V2
cd src
python check.py
start python init.py
echo Web面板已经在 http://127.0.0.1:9000/ 启动。
python -m http.server 9000 --directory ./web/
echo 程序已退出。
pause