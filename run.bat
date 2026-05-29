@echo off
REM Citizen Feedback on Road Maintenance - Run Script for Windows

echo.
echo ========================================
echo Starting Road Maintenance Portal...
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the Flask application
echo Activating virtual environment...
echo.
echo Starting Flask development server...
echo.
echo The application will be available at:
echo   http://localhost:5000
echo.
echo Admin Login:
echo   Email: admin@example.com
echo   Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo.
echo.

python app.py

pause
