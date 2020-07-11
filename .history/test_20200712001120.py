import win32serviceutil




def Service_Query():
    ml_service_query = win32serviceutil.QueryServiceStatus('MysticLight2_Service')

    print(ml_service_query)


    if ml_service_query[2] == 0:
        print("stopped")
        return("stopped")
    else:
        print("running")
        return("running")
