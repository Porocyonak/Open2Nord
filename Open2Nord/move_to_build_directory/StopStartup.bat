@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

schtasks /delete /tn "Open2Nord" /F

echo Done!

pause