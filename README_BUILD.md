# Building Windows Executable

This guide explains how to build a standalone Windows executable from your Python game.

## Prerequisites

- Python 3.x installed
- All game dependencies installed

## Quick Build

Simply run the `build.bat` file:

```batch
build.bat
```

This will:
1. Install/update PyInstaller and dependencies
2. Create a standalone executable in the `dist` folder
3. The executable will be named `my_game.exe`

## Manual Build

If you prefer to build manually:

1. Install dependencies:
   ```batch
   pip install -r requirements.txt
   ```

2. Build the executable:
   ```batch
   pyinstaller build_exe.spec --clean
   ```

3. Find your executable in the `dist` folder

## What Gets Included

The build process automatically includes:
- All Python source files
- All music and sound files from the `music/` directory
- Required Python libraries (pygame, chess, etc.)
- Python runtime

## Running the Executable

After building, you can run the game by:
- Double-clicking `dist\my_game.exe`
- Or running it from the command line: `dist\my_game.exe`

The executable is completely standalone - no Python installation needed on the target machine!

## Troubleshooting

If you encounter issues:
- Make sure all music files are in their correct directories
- Check that all dependencies are listed in `requirements.txt`
- Try building with `--clean` flag to remove cached files
- Check the console output for any error messages
