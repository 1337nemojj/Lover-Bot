from os import path, system
import time
from datetime import datetime



def cur_time():
    t = datetime.now()
    return t.strftime("%m/%d/%Y, %H:%M:%S")

def name_pid(file_path):
    with open(file_path + "PID.txt", "r", encoding='utf-16-le') as file:
        for lines in file:
            if "bot.py" in lines:
                proc = lines.split()
                name = proc[2]
                PID = proc[3]
                return(name,PID)

while True:
    file_path = path.abspath(__file__)[:-len(path.basename(__file__))]
    time.sleep(1)
    system("wmic process get Caption, ProcessId, CommandLine >" + file_path + "PID.txt")
    time.sleep(1)
    if name_pid(file_path) == None:
        print("[!] STOP - ",cur_time())
        system("start python bot.py")
        print("launched")
    else:
        print("[+] OK   - ",cur_time())
    time.sleep(1)