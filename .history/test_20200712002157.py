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


print((process_exists("LEDKeeper.exe"))

def Process_Query():
    ml_process_query = process_exists("LEDKeeper.exe")

    if ml_process_query == True:
        return("Running")
    else:
        return("Stopped")