@echo off
echo Starting game...
echo.
dist\my_game.exe
if errorlevel 1 (
    echo.
    echo Game exited with an error.
    pause
)
