import PySimpleGUI as sg
import os
import win32serviceutil
import time

def stop_ml():
    win32serviceutil.StopService("MysticLight2_Service")
    time.sleep(1)
    os.system("taskkill /f /im LEDKeeper.exe")

def start_ml():
    win32serviceutil.StartService("MysticLight2_Service")


sg.theme("Black")

layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Mystic Light Disabler', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()