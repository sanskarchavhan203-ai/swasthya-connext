@echo off
echo ========================================================
echo   Launching Swasthya Connect Public Tunnel
echo ========================================================
echo.
echo 1. Starting Local Server...
start "" python server.py
timeout /t 2 >nul
echo 2. Opening Secure Public Tunnel...
echo.
ssh -o StrictHostKeyChecking=no -R 80:127.0.0.1:3000 nokey@localhost.run
pause
