## IMPORTS
from tqdm import tqdm
import time
import os
import sys
import requests
import subprocess
from colorama import init, Fore, Style
from datetime import datetime
import hashlib


# Paths
UsersPath = r"./DataInfo/Datos"
userfile = r"./DataInfo/user.txt"


## =============================
##          S T A R T
## =============================

# check status
def loading():
    os.system("clear")
    
    print(Fore.WHITE + """
   __                ___                   
  / /  ___  ___ ____/ (_)__  ___ _         
 / /__/ _ \/ _ `/ _  / / _ \/ _ `/   _   _ 
/____/\___/\_,_/\_,_/_/_//_/\_, (_) (_) (_)
                           /___/           
          """)
    
    print("[!] Loading console.py\n")
    time.sleep(0.5)
    print(Fore.LIGHTGREEN_EX + "[✓] Loaded console.\n")
    
    ## LOAD VERSION
    version = r"./DataInfo/version.txt"
    with open(version, "r") as f:
        linea = f.read()
        linea = linea.strip()
        
    texto = linea.split(":", 1)
    version = texto[1].strip()
    
    print(Fore.LIGHTYELLOW_EX + f"[!] Version: {version}\n")
    input(Fore.WHITE + f"Press any button to start console.")
    startconsole()
    
    

def startconsole():
    creatinguser = True
    while creatinguser:
    # CREATE USER
        os.system("clear")
        print("""
      _____             __        __  __           
     / ___/______ ___ _/ /____   / / / /__ ___ ____
    / /__/ __/ -_) _ `/ __/ -_) / /_/ (_-</ -_) __/
    \___/_/  \__/\_,_/\__/\__/  \____/___/\__/_/   
                                                
        """)
        print(Fore.CYAN + "Max Length: 15" + Fore.WHITE + "\n")
        usernameinput = input("-> Create your unique username: ")
        userlen = len(usernameinput)
        if userlen < 15 and userlen > 0:
            ## CREATE PASS
            os.system("clear")
            print("""
    _____             __        ___  ___   ________
    / ___/______ ___ _/ /____   / _ \/ _ | / __/ __/
    / /__/ __/ -_) _ `/ __/ -_) / ___/ __ |_\ \_\ \  
    \___/_/  \__/\_,_/\__/\__/ /_/  /_/ |_/___/___/  
                                                                                    
                """)
            
            print("- User: " + Fore.LIGHTGREEN_EX + usernameinput)
            print(Fore.CYAN + "Max pass lenght: 20" + Fore.WHITE + "\n")
            
            ## PASS
            creatingpass = True
            while creatingpass: 
                passinput = input("-> Create your unique password: ")
                
                if len(passinput) < 20 and len(passinput) > 0:
                    # GOOD PASS
                    os.system("clear")
                    print("""
                                                                                        
,--. ,--. ,---.  ,------.,------.      ,-----. ,-----. ,--.  ,--.,------.,--. ,----.    
|  | |  |'   .-' |  .---'|  .--. '    '  .--./'  .-.  '|  ,'.|  ||  .---'|  |'  .-./    
|  | |  |`.  `-. |  `--, |  '--'.'    |  |    |  | |  ||  |' '  ||  `--, |  ||  | .---. 
'  '-'  '.-'    ||  `---.|  |\  \     '  '--'\'  '-'  '|  | `   ||  |`   |  |'  '--'  | 
 `-----' `-----' `------'`--' '--'     `-----' `-----' `--'  `--'`--'    `--' `------'  
                                                                                        
                          """)
                    
                    ## ENCRIPTYING PASS AND USER
                    saved_user = hashlib.sha256(usernameinput())
                    saved_password = hashlib.sha256(passinput())
                    
                    with open(userfile, "w") as f:
                        f.write(f"{saved_user}:{saved_password}")
                    
                    print(Fore.LIGHTGREEN_EX + "[+] Encrypting and saving user and pass.")
                    time.sleep(1)
                    
                else:
                    
                    # BAD PASS
                    print(Fore.LIGHTRED_EX + f"[!] The pass is {len(usernameinput)} length, max is 20. Try again.\n")
                    input(Fore.WHITE + "Press any button to continue.")
                    
        
        else:
            print(Fore.LIGHTRED_EX + f"[!] The username is {len(usernameinput)} length, max is 15. Try again.\n")
            input(Fore.WHITE + "Press any button to continue.")

if os.path.exists(UsersPath):
    if os.path.exists(userfile):
        ## LOGIN
        print("login")

else:
    loading()
