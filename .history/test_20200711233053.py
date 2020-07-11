import win32serviceutil


try: 
    win32serviceutil.QueryServiceStatus('MysticLight2_Service')
except:
    print("Windows service NOT installed")
else:
    print("Windows service installed")