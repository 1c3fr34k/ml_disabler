import win32serviceutil



ml_service_query = win32serviceutil.QueryServiceStatus('MysticLight2_Service')

print(ml_service_query)


if ml_service_query[2] == 0:
    print("service not running")
else:
    print("service running")
