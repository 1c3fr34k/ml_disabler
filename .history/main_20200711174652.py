import PySimpleGUI as sg
import os
import win32serviceutil
import time

def stop_ml():
    win32serviceutil.StopService("MysticLight2_Service")
    time.sleep(1)
    os.system("taskkill /f /im LEDKeeper.exe")

