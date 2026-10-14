@echo off
REM Start AgriVoice Project on Windows
title AgriVoice AI Launcher

echo.
echo =========================================================
echo   AgriVoice AI - Smart Voice Assistant for Farmers
echo =========================================================
echo.

set "SCRIPT_DIR=%~dp0"

echo [1/2] Starting Django Backend on http://localhost:8000...
cd /d "%SCRIPT_DIR%backend"
start "AgriVoice Backend" cmd /k "python manage.py runserver 0.0.0.0:8000"

echo [2/2] Starting Frontend on http://localhost:3000...
cd /d "%SCRIPT_DIR%agrivoice-ui"
start "AgriVoice Frontend" cmd /k "npm start"

echo.
echo Application is starting...
echo Frontend UI: http://localhost:3000
echo Backend API: http://localhost:8000
echo.
echo Keep this or the launched command windows open.