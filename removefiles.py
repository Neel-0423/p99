import os
import shutil
import time

name = input("enter name of the folder: ")
path = input("enter path of the folder: ")
days = input("enter the no of days which the file should be older than for deleating : ")
time_sec=days
time_sec = time.time()

if os.path.exists(path) :
    os.walk(path)
    list_of_files =  os.listdir(os.path.join(path, name))
    print(list_of_files)    
    ctime = os.stat(path).st_ctime
    if ctime>time_sec:
        isDirectory = os.path.isdir(path)
        if isDirectory == "false":
            os.remove(path)
        else :
            shutil.rmtree()
else :
    print("please enter correct path")

