import os

def main():
    main_name = 'main'
    icon_name = 'eduspyware.ico'

    #compile service.exe
    os.system(fr'pyinstaller --onefile service.py')

    #compile main.exe
    os.system(fr'pyinstaller --windowed --uac-admin --icon={icon_name} --onefile {main_name}.py')
    os.system(fr'del {main_name}.spec')

    #cleanup directories generated from compilation
    os.system('rmdir build /s /q')
    os.system('rmdir __pycache__ /s /q')

if __name__ == '__main__':
    main()

