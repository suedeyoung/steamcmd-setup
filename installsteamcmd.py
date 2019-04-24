#!/usr/bin/python3
import subprocess
import pwd
import os
from pathlib2 import Path

print("Greetings! This script is still in beta so please let me know if there is any issues with the script itself.\nSo far, it seems that things are just barely getting started and this is my first full blown python script so I'm sorry if it looks bad \n")
subprocess.call(["ls", "-lah"])

print("Completed ls -lah subprocess call \n")


path = os.getcwd()
print("The current path of this system is %s \n" % path)


print("Checking if /home/steamcmd is available... \n")


my_file = Path ("/home/steamcmd")
if my_file.is_dir():
    os.chdir("/home/steamcmd")
    print("/home/steamcmd is already on the server, moving on..")
else:
    print("Not finding /home/steamcmd.. making folder")
    os.mkdir("/home/steamcmd")
    print("Folder should be created, testing it now \n")
    os.chdir("/home/steamcmd")
    print("Successfully create /home/steamcmd")