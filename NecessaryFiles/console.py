from tqdm import tqdm
import time
import os
import sys
import requests
import subprocess
from colorama import init, Fore, Style
from datetime import datetime


## FILES
checkfiles = {
    "datainfo": r"./DataInfo",
    "setup": r"./DataInfo/setup.txt",
    "webpaths": r"./DataInfo/WebPaths",
    "status": r"./DataInfo/status.txt",
    "version": r"./DataInfo/version.txt",
    "username": r"./DataInfo/Users"
}


datainfo = r"./DataInfo"
setup = r"./DataInfo/setup.txt"
setupPY = r"./setup.py"
webpaths = r"./DataInfo/WebPaths"
status = r"./DataInfo/status.txt"
MainpyPath = r"./main.py"

## FUNCTIONS
def setup_function():
    try:
        os.system("python3 setup.py")
    except Exception as err:
        print(f"An internal error has occurred.")
        print("Exiting. . .")
        sys.exit()
        
        
## CHECK SETUP.PY
if not os.path.exists(setupPY):
    url = r"https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/setup.py"
    response = requests.get(url)
    
    if response.status_code == 200:
        contenido = response.text
        
        ## CREATE FILE
        with open(setupPY, "w") as f:
            f.write(contenido)
            
## CHECK FINAL A ARCHIVOS
if os.path.exists(webpaths):
    comando_previo = f"ls -1 ./DataInfo/WebPaths | wc -l"
    comando_final = subprocess.check_output(comando_previo, shell=True, text=True)
    comando_final = comando_final.strip()
    comando_final = comando_final.splitlines()
    if "0" in comando_final:
        setup_function()
    else:
        comando = f"wc -w ./DataInfo/WebPaths/*"
        RespuestaServer = subprocess.check_output(comando, shell=True, text=True)
        resultado = RespuestaServer.strip()
        resultado = resultado.splitlines()
        ultima_linea = RespuestaServer.splitlines()[-1]
 
    ## START SETUP BC OF AN ERROR
    if not ultima_linea == " 190729 total":
        comando = f"rm -r ./DataInfo/WebPaths/*"
        os.system("clear")
        print("=" * 60)
        print(Fore.RED + "\n[!] PROBLEM DETECTED!" + Fore.WHITE + "\n")
        print(f"There was a", Fore.GREEN + "required", Fore.WHITE + "file that had an" + Fore.LIGHTRED_EX + " internal error" + Fore.WHITE + " on webpaths files.\n")
        print("=" * 60)
        setupaccion = input(Fore.LIGHTYELLOW_EX + "\n-> Do you want to solve it? (y/n): ")
        setup_function()
    

## NECESSARY CHECK.
CantidadCheckFiles = len(checkfiles) - 1
linkscorrectos = 0

for i in checkfiles:
    link = checkfiles[i]
    if not os.path.exists(link):
        os.system("clear")
        print("=" * 60)
        print(Fore.RED + "\n[!] PROBLEM DETECTED!" + Fore.WHITE + "\n")
        print(f"There was a", Fore.GREEN + "required", Fore.WHITE + "file that was" + Fore.LIGHTRED_EX + " removed" + Fore.WHITE + ".\n")
        print("In order to continue, you must solve it, or the program could fail.\n")
        print("If you press \"no\" on repairing, the program will be stopped.\n")
        print("=" * 60)
        setupaccion = input(Fore.LIGHTYELLOW_EX + "\n-> Do you want to solve it? (y/n): ")
        
        if setupaccion.lower() == "y" or setupaccion.lower() == "yes":
            try:
                
                
                os.system("python3 setup.py")
                break
            except Exception as err:
                print(f"An error has occured: {err}")
                sys.exit()

        else:
            os.system("clear")
            print("Exiting.")
            sys.exit()
    else:
        linkscorrectos += 1
        
## START MAIN.PY
if linkscorrectos == len(checkfiles):
    with open(status, "r") as f:
        lecturastatus = f.read()
        
        os.system("clear")
        
    if lecturastatus == "Ok" and os.path.exists(MainpyPath):
        
        url = "https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/main.py"
        preguntaservidor = requests.get(url)
        RespuestaservidorMainpy = preguntaservidor.text
        with open(MainpyPath, "w") as f:
            f.write(RespuestaservidorMainpy)
            
        os.system("python3 main.py")
        
    else:
        os.system("clear")
        print("=" * 60)
        print(Fore.RED + "\n[!] PROBLEM DETECTED!" + Fore.WHITE + "\n")
        print(f"There was a", Fore.GREEN + "required", Fore.WHITE + "file that was" + Fore.LIGHTRED_EX + " removed" + Fore.WHITE + ".\n")
        print("In order to continue, you must solve it, or the program could fail.\n")
        print("If you press \"no\" on repairing, the program will be stopped.\n")
        print("=" * 60)
        setupaccion = input(Fore.LIGHTYELLOW_EX + "\n-> Do you want to solve it? (y/n): ")
        
        if setupaccion.lower() == "y" or setupaccion.lower() == "yes":
            try:
                os.system("python3 setup.py")
            except Exception as err:
                print(f"An error has occured: {err}")
                sys.exit()

        else:
            os.system("clear")
            print("Exiting.")
            sys.exit()
