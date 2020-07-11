import win32serviceutil




def Process_Query():
    ml_process_query = win32serviceutil.QueryProcessStatus('LEDKeeper.exe')

    print(ml_process_query)

    """
    if ml_service_query[2] == 0:
        print("stopped")
        return("stopped")
    else:
        print("running")
        return("running")
    """

Process_Query()