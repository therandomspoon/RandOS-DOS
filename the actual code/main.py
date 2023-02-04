import platform
import subprocess
import sys
import time
import socket
import struct
import os

print("welcome to RandOS")                                                            
print('  DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS')
print('  D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S')
print('  D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S')
print('  DDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS')
print('    D:::::D    D:::::D O::::::O   O::::::OS:::::S')            
print('    D:::::D     D:::::DO:::::O     O:::::OS:::::S')            
print('    D:::::D     D:::::DO:::::O     O:::::O S::::SSSS')         
print('    D:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS')    
print('    D:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS')  
print('    D:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S') 
print('    D:::::D     D:::::DO:::::O     O:::::O            S:::::S')
print('    D:::::D    D:::::D O::::::O   O::::::O            S:::::S')
print('  DDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S')
print('  D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S')
print('  D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS')
print('  DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS')

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    response = os.popen(" ".join(command)).read()
    if 'Destination host unreachable' in response:
        return False
    elif 'Request timed out' in response:
        return False
    else:
        return True

print('What would you like to do?')
comind = input()
if comind == 'ping':
    host = input("Enter the host to ping: ")
    if ping(host):
        print(host, 'is up!')
    else:
        print(host, 'is down!')
elif comind == 'dir':
    def list_directories():
     dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
     print("Directories in the current working directory:")
     for dir in dirs:
        print(dir)
    list_directories()
elif comind == 'help':
    print('RandOS - DOS v1.02 Alpha-release Early access')
    print('command list:')
    print('ping - pings a hostname or ip address')
    print('dir - lists all directories on you device (may only work if file is running locally)')
    print('Important links')
    print('github - ')
