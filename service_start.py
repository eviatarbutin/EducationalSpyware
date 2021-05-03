import os


service_name = '"MySrv3"'
path = '"C:\\Users\\USER\\Desktop\\a.exe"'
os.system(f'cmd /c "sc create {service_name} binpath= {path}"')

# services.msc
