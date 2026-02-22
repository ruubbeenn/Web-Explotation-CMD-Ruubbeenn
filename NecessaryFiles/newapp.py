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
import bcrypt
import readline
import getpass
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import shutil

comando = input("Que quieres hacer: ")
separacion = comando.split()
lon = len(separacion)
badusageofwebhunter = False

if separacion[0].lower() == "webhunter":
    ## WHAT WEB INSTALLED ON TERMINAL
    if shutil.which("whatweb") is not None:
        if lon == 2:
            ## NO PARAMETER
            web = separacion[1].lower()
            if not web.startswith(("https://", "http://")):
                if not "www" in web:
                        web = f"https://www.{web}"
                else:
                    web = f"https://{web}"
                commandwebhunter = f"whatweb {web}"

            try:
                print(f"""{Fore.LIGHTBLUE_EX}
============================
     LOADING WEBHUNTER
============================
\n{Fore.WHITE}""")
                try:
                    output = subprocess.check_output(commandwebhunter, shell=True,text=True)
                    outputprinted = output.split(",")
                    print(f"{Fore.LIGHTGREEN_EX}[✓] Webhunter scan to {Fore.LIGHTCYAN_EX}{web} {Fore.WHITE}finished!{Fore.WHITE}\n")
                
                    for i in outputprinted:
                        print(f"{Fore.LIGHTYELLOW_EX}[?]{Fore.WHITE} {i}")

                    print("\n")

                except Exception as err:
                    print(f"{Fore.LIGHTRED_EX}An error has ocurred:\n{Fore.WHITE}{err}\n")
            
            except Exception as err:
                print(f"{Fore.LIGHTRED_EX}An error has ocurred:\n{Fore.WHITE}{err}\n")


        else:
            print(f"Command {Fore.LIGHTRED_EX}webhunter {Fore.WHITE}bad usage. Use {Fore.LIGHTGREEN_EX}webhunter --help {Fore.WHITE}for more info!\n")
