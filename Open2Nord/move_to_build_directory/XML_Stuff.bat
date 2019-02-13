@echo off

set /a c=0

SETLOCAL=ENABLEDELAYEDEXPANSION

set COMM=^<Command^>
set AUT=^<Author^>
set AUTREP=%ComputerName%\%Username%^</Author^>^<URI^>\Open2Nord^</URI^>^</RegistrationInfo^>^<Triggers^>^<LogonTrigger^>^<StartBoundary^>2018-09-06T12:22:00^</StartBoundary^>^<Enabled^>true^</Enabled^>^</LogonTrigger^>^</Triggers^>^<Principals^>^<Principal id="Author"^>^<LogonType^>InteractiveToken^</LogonType^>^<RunLevel^>HighestAvailable^</RunLevel^>^</Principal^>^</Principals^>^<Settings^>^<MultipleInstancesPolicy^>IgnoreNew^</MultipleInstancesPolicy^>^<DisallowStartIfOnBatteries^>false^</DisallowStartIfOnBatteries^>^<StopIfGoingOnBatteries^>false^</StopIfGoingOnBatteries^>^<AllowHardTerminate^>true^</AllowHardTerminate^>^<StartWhenAvailable^>false^</StartWhenAvailable^>^<RunOnlyIfNetworkAvailable^>false^</RunOnlyIfNetworkAvailable^>^<IdleSettings^>^<Duration^>PT10M^</Duration^>^<WaitTimeout^>PT1H^</WaitTimeout^>^<StopOnIdleEnd^>true^</StopOnIdleEnd^>^<RestartOnIdle^>false^</RestartOnIdle^>^</IdleSettings^>^<AllowStartOnDemand^>true^</AllowStartOnDemand^>^<Enabled^>true^</Enabled^>^<Hidden^>false^</Hidden^>^<RunOnlyIfIdle^>false^</RunOnlyIfIdle^>^<WakeToRun^>false^</WakeToRun^>^<ExecutionTimeLimit^>PT72H^</ExecutionTimeLimit^>^<Priority^>7^</Priority^>^</Settings^>^<Actions Context="Author"^>^<Exec^>^<Command^> 

set REP=%~dp0ScheduleFixer_donotrun.bat^</Command^>^</Exec^>^</Actions^>^</Task^>

copy "%~dp0task_info.xml" "%~dp0newtext.xml" /Y

    for /f %%a in (%~dp0newtext.xml) do (
        set foo=%%a
	if !foo!==!AUT! (
		echo author found, editing
		echo !AUTREP! >> %~dp0newtext.xml
		)
	) 
echo !REP! >> %~dp0newtext.xml