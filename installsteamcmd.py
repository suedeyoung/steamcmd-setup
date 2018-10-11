#!/usr/bin/python
import subprocess

print("Greetings! This script is still in beta so please let me know if there is any issues with the script itself.\nSo far, it seems that things are just barely getting started and this is my first full blown python script so I'm sorry if it looks bad")

subprocess.call(["ls", "-lah"])
print("Completed ls -lah subprocess call")