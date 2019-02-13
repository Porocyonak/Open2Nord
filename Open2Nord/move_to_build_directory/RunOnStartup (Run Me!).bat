@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

call %~dp0XML_Stuff.bat

schtasks /create /tn "Open2Nord" /xml %~dp0newtext.xml /F

echo Done!

pause