@echo off
echo Building Windows executable...
echo.

REM Check if PyInstaller is installed
python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing dependencies...
    python -m pip install -r requirements.txt
) else (
    echo PyInstaller found. Installing/updating dependencies...
    python -m pip install -r requirements.txt
)

echo.
echo Creating executable...
python -m PyInstaller build_exe.spec --clean

echo.
echo Build complete! The executable should be in the 'dist' folder.
echo You can run it by double-clicking 'dist\my_game.exe'
pause
