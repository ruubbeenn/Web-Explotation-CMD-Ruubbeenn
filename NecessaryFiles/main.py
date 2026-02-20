## IMPORTS
from tqdm import tqdm
import time
import os
import sys
import requests
import subprocess
from colorama import init, Fore, Style
from datetime import datetime

## =============================
##          S T A R T
## =============================

# check status
def startconsole():
    print("A")
        
    # CREATE USER
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
        
        print(Fore.CYAN + "Max pass lenght: 20" + Fore.WHITE + "\n")
        passinput = input("")


enconsola = True
while enconsola:
    date = datetime.now().strftime("%H:%M:%S")
    userinput = input("")
