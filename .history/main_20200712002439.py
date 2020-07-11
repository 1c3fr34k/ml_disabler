import PySimpleGUI as sg
import os
import win32serviceutil
import time
import subprocess


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



sg.theme("Black")

layout = [  [sg.Text('Process Status:'), sg.Text(Process_Query())],
            [sg.Text('Service Status:'), sg.Text(Service_Query())],
            [sg.Button('Start'), sg.Button('Stop'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Mystic Light Disabler', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == 'Start':
        start_ml()
    elif event == 'Stop':
        stop_ml()

window.close()