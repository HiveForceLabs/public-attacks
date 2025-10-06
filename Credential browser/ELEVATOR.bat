@echo off
setlocal

:: Set the path to ELEVATOR in the current user's Downloads folder
set "ELEVATOR_PATH=%USERPROFILE%\Downloads\broextra.exe"

:: Check if ELEVATOR exists
if not exist "%ELEVATOR_PATH%" (
    echo [ERROR] ELEVATOR executable not found at "%ELEVATOR_PATH%"
    exit /b 1
)

echo [INFO] Running ELEVATOR: "%ELEVATOR_PATH%" -all
echo ----------------------------------------

:: Run ELEVATOR and show its output in the same console
"%ELEVATOR_PATH%" -all
set "EXITCODE=%ERRORLEVEL%"

echo ----------------------------------------

:: Interpret exit codes
if "%EXITCODE%"=="0" (
    echo [INFO] ELEVATOR EXECUTION completed successfully.
    exit /b 0
) else (
    echo [ERROR] ELEVATOR exited with error code %EXITCODE%.
    exit /b 2
)
