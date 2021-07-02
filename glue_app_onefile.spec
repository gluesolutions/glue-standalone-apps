# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import glob

if os.name == 'nt':
    icon = os.path.abspath('icon.ico')
elif sys.platform == 'darwin':
    icon = os.path.abspath('icon.icns')
else:
    icon = None

block_cipher = None

#notebooks = [(x, 'app_notebooks') for x in glob.glob(os.path.join('app_notebooks', '*.ipynb'))]

a = Analysis(['start_glue.py'],
             pathex=['glue'],
             binaries=[],
             #datas=notebooks,
             hiddenimports=['voila',
                            'ipykernel',
                            'ipykernel.datapub',
                            'IPython.extensions.storemagic',
                            'ipywidgets',
                            'jupyterlab_pygments',
                            'ipyvuetify',
                            'bqplot',
                            'nbformat',
                            'nbconvert',
                            'numpy',
                            'scipy',
                            'astropy',
                            'voila-vuetify'],
             hookspath=['hooks'],
             runtime_hooks=[],
             excludes=['tkinter'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='glue',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True,
          icon=icon)

app = BUNDLE(exe,
             name='glue.app',
             icon=icon,
             info_plist={
             'NSHighResolutionCapable': 'True'
             },
             bundle_identifier='org.qt-project.Qt.QtWebEngineCore')
