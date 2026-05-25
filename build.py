import os
import subprocess
import flet

script_name = 'main.py'
app_name = 'Raport_creator'
icon_path = 'icons/icon.ico'

flet_path = os.path.dirname(flet.__file__)
icons_path = os.path.join(flet_path, 'controls', 'material', 'icons.json')

cmd = [
    'pyinstaller',
    '--noconfirm',
    '--onefile',
    '--windowed',
    '--icon', "assets/icon.ico",
    f'--name={app_name}',
    '--version-file=version.txt',

    f'--add-data={icons_path};flet/controls/material',
    f'--add-data={flet_path};flet',


    '--add-data=utils;utils',

    '--hidden-import=flet',
    '--hidden-import=flet.controls.material',
    '--hidden-import=urlextract',
    '--hidden-import=openpyxl',
    '--hidden-import=pandas',

    '--collect-data=urlextract',
]

if os.path.exists(icon_path):
    cmd.append(f'--icon={icon_path}')
else:
    print(f"\n[ВНИМАНИЕ] Иконка '{icon_path}' не найдена! Программа будет собрана со стандартным значком.\n")

cmd.append(script_name)

print(f"Начинаем сборку программы {app_name}...")
subprocess.run(cmd)
print("\nСборка завершена! Готовый файл ищи в папке dist.")