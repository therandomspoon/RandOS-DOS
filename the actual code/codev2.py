import platform
import subprocess
import sys
import time
import socket
import struct
import os
import itertools
import threading


def change_color(color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
    }
    return colors.get(color, "")
    print(change_color("white") + "Hackermode engaged")

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
aaaaaaaaaaaaaa = True
print('What would you like to do?')
comind = input()
if comind == 'ping':
    host = input("Enter the host to ping: ")
    if ping(host):
        print(host, 'is up!')
        print('RandOS-DOS is Shutting down automatically...')
        time.sleep(10)
    else:
        print(host, 'is down!')
        print('RandOS-DOS is Shutting down automatically...')
        time.sleep(10)
elif comind == 'dir':
    def list_directories():
     dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
     print("Directories in the current working directory:")
     for dir in dirs:
        print(dir)
    list_directories()
    print('RandOS-DOS is Shutting down automatically...')
    time.sleep(10)
elif comind == 'echo':
    def ecio():
        def echo(message):
            print(message)
        print('what would you like to print on the screen')
        printmes = input()
        done = False
        print('processing')
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
              if done:
                 break
                 sys.stdout.write('\rloading ' + c)
                 sys.stdout.flush()
                 time.sleep(0.1)
            sys.stdout.write('\rDone!     ')
        t = threading.Thread(target=animate)
        t.start()
        time.sleep(5)
        done = True
        print(printmes)
        print('Would you like to print anything more? yes/no')
        answoo = input()
        if answoo == 'yes':
            ecio()
        else:
            return
    ecio()
elif comind == 'hackermode':
    sys.set_int_max_str_digits(10000000)
    def change_color(color):
     colors = {
           "red": "\033[91m",
            "green": "\033[92m",
           "yellow": "\033[93m",
           "blue": "\033[94m",
           "purple": "\033[95m",
          "cyan": "\033[96m",
       }
     return colors.get(color, "")
    print(change_color("green") + "Hackermode engaged")
    time.sleep(2.5)
    numing = 0
    while aaaaaaaaaaaaaa != False:
        numing = numing + 1
        print(numing)
        numing = numing * numing
        print(numing)
        time.sleep(0.5)


elif comind == 'help':
    print('RandOS - DOS v1.02 Alpha-release Early access')
    print('command list:')
    print('ping - pings a hostname or ip address')
    print('dir - lists all directories on you device (may only work if file is running locally)')
    print('echo - prints text to the screen')
    print('hackermode - hollywood')
    print('Important links')
    print('github - https://github.com/therandomspoon/RandOS-DOS/tree/main')
    print('Documentation - https://randdosdocumentation.randspoon.co.uk/')
    print('RandOS-DOS is Shutting down automatically...')
    time.sleep(10)
