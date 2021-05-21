import os

'''
The following piece of code must be in the installation script rather than main.py.
If we would place this piece of code in main.py instead and than compile it, it would require
from the user to have PythonXX in their path variable which loses its portability.
'''
def main():
    file_name = 'main'
    icon_name = 'eduspyware.ico'

    os.system(fr'pyinstaller --windowed --uac-admin --icon={icon_name} --onefile {file_name}.py')
    os.system(fr'del {file_name}.spec')
    os.system('rmdir build /s /q')
    os.system('rmdir __pycache__ /s /q')
    #os.system(fr'move {abs_dir_path}\dist\{file_name}.exe {abs_dir_path}')

if __name__ == '__main__':
    main()

