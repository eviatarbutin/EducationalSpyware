import os

def main():
    main_name = 'main'
    icon_name = 'eduspyware.ico'

    #compile service.exe
    os.system(fr'pyinstaller --onefile service.py')

    #compile main.exe
    os.system(fr'pyinstaller -c --uac-admin --icon={icon_name} --hidden-import tkinter --onefile {main_name}.py')

    #cleanup files and directories generated from compilation
    os.system(fr'del {main_name}.spec')
    os.system(fr'del service.spec')
    os.system('rmdir build /s /q')
    os.system('rmdir __pycache__ /s /q')

if __name__ == '__main__':
    main()

