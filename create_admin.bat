@echo off
chcp 65001 >nul
cd /d "%~dp0"
py create_admin.py
pause
