# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['bot.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'pyTelegramBotAPI',
        'altgraph',
        'certifi',
        'charset_normalizer',
        'idna',
        'importlib_metadata',
        'macholib',
        'packaging',
        'pyinstaller_hooks_contrib',
        'requests',
        'urllib3',
        'WMI',
        'zipp',
        'win32com.client',  # Указан полный путь для win32com
    ],
    hookspath=[],  # Добавьте путь к хукам, если это необходимо
    runtime_hooks=[],  # Укажите runtime хуки, если требуется
    excludes=[
        'tkinter',  # Исключим ненужные библиотеки для уменьшения размера
    ],
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='bot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Включена сжатие UPX для уменьшения размера
    console=True,  # Оставим консоль для отладки
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='bot'
)
