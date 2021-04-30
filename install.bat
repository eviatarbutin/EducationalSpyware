pyinstaller --onefile client.py
del client.spec
rmdir build /s /q
rmdir __pycache__ /s /q