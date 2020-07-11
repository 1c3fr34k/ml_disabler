import PySimpleGUI as sg
import os
import win32serviceutil

def stop_ml():
    win32serviceutil.StopService("MysticLight2_Service")

