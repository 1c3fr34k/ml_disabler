import win32serviceutil



ml_service_query = win32serviceutil.QueryServiceStatus('MysticLight2_Service')

#print(query)

if ml_service_query[1] != 1:
    print("service not running")
else:
    print("service running")
