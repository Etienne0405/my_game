# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Collect all music files
music_files = []
import os

music_dirs = [
    'music/draw_card',
    'music/ghost_encounter',
    'music/health',
    'music/music',
    'music/overall',
    'music/voices'
]

for music_dir in music_dirs:
    if os.path.exists(music_dir):
        for file in os.listdir(music_dir):
            if file.endswith(('.mp3', '.wav')):
                music_files.append((os.path.join(music_dir, file), music_dir))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=music_files,
    hiddenimports=['pygame', 'chess', 'curses', '_curses', 'msvcrt'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='my_game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Disable UPX to avoid potential issues
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Keep console for terminal-based game
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # You can add an icon file here if you have one
)
