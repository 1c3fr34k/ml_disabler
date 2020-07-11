import PySimpleGUI as sg
import os
import win32serviceutil
import time
import subprocess
import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():

    def process_exists(process_name):
        try:
            call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
            # use buildin check_output right away
            output = subprocess.check_output(call).decode()
            # check in last line for process name
            last_line = output.strip().split('\r\n')[-1]
            # because Fail message could be translated
            return last_line.lower().startswith(process_name.lower())
        except:
            return(False)


    def stop_ml():
        win32serviceutil.StopService("MysticLight2_Service")
        time.sleep(1)
        os.system("taskkill /f /im LEDKeeper.exe")

    def start_ml():
        win32serviceutil.StartService("MysticLight2_Service")


    def Service_Query():
        ml_service_query = win32serviceutil.QueryServiceStatus('MysticLight2_Service')
        print(ml_service_query)
        if ml_service_query[2] == 0:
            return("Stopped")
        else:
            return("Running")


    def Process_Query():
        ml_process_query = process_exists("LEDKeeper.exe")
        if ml_process_query == True:
            return("Running")
        else:
            return("Stopped")


    def Update_Query():
        if Process_Query() and Service_Query() == "Running":
            while Process_Query() and Service_Query() == "Running":
                window["TPQ"].update(Process_Query())
                window["TSQ"].update(Service_Query())

        elif Process_Query() and Service_Query() == "Stopped":
            while Process_Query() and Service_Query() == "Stopped":
                window["TPQ"].update(Process_Query())
                window["TSQ"].update(Service_Query())



    sg.theme("Black")

    layout = [  [sg.Text('Process Status:'), sg.Text(Process_Query(), key="TPQ")],
                [sg.Text('Service Status:'), sg.Text(Service_Query(), key="TSQ")],
                [sg.Button('Start'), sg.Button('Stop'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Mystic Light Disabler', layout, size=(240,100))
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'Cancel': # if user closes window or clicks cancel
            break
        elif event == 'Start':
            start_ml()
            Update_Query()
        elif event == 'Stop':
            stop_ml()
            Update_Query()

    window.close()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)