# -*- mode: python ; coding: utf-8 -*-

import os
import sys

if os.name == "nt":
    icon = os.path.abspath("icon.ico")
    onefile = True
elif sys.platform == "darwin":
    icon = os.path.abspath(os.path.join("osx", "icon.icns"))
    onefile = False
else:
    icon = None
    onefile = True

block_cipher = None

a = Analysis(
    ["start_glue.py"],
    pathex=["start-glue"],
    binaries=[],
    hiddenimports=[
        "glue_vispy_viewers",
        "vispy",
        "notebook",
        "freetype",
        "glue_wwt",
        "glue_plotly",
        "glue_statistics",
        "glue_genes",
        "glue_small_multiples",
        "glue_heatmap",
        "pvextractor",
        "anndata",
        "scanpy",
        "pyranges",
        "seaborn",
        "enrichrpy",
        "psutil",

    ],
    hookspath=["hooks"],
    hooksconfig={
        "matplotlib": {"backends": "all"},
    },
    runtime_hooks=[],
    excludes=["tkinter", "PyQt5.QtQml"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

if onefile:

    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        name="glue",
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=False,
        console=True,
        icon=icon,
    )

else:

    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name="start_glue",
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=False,
        console=False,
        icon=icon,
        argv_emulation=True,
    )

    coll = COLLECT(
        exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=False, name="start_glue"
    )

    app = BUNDLE(
        coll,
        name="glue.app",
        icon=icon,
        info_plist={
            "CFBundleName": "glueviz",
            "CFBundleDisplayName": "glueviz",
            "CFBundleVersion": "1.2",
            "CFBundleShortVersionString": "1.2",
            "NSHighResolutionCapable": "True",
            "CFBundleDocumentTypes": [
                {
                    "CFBundleTypeName": "Glue Session Files",
                    "CFBundleTypeExtensions": ["glu"],
                    "CFBundleTypeRole": "Viewer",
                }
            ],
        },
        bundle_identifier="io.gluesolutions.glueviz",
    )
