from PyInstaller.utils.hooks import collect_data_files, copy_metadata

datas = collect_data_files('squidpy', include_py_files=True)
datas += copy_metadata('squidpy')