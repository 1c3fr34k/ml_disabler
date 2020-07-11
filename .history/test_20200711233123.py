import win32serviceutil



query = win32serviceutil.QueryServiceStatus('MysticLight2_Service')

print(query)
