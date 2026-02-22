import os
import time
from tqdm import tqdm
import requests
from colorama import init, Fore, Style
import sys
import readline


## IMPORTANT
init(autoreset=True)

## PATHS
DataInfoFolder = r"./DataInfo"
setup = r"./DataInfo/setup.txt"
webpaths = r"./DataInfo/WebPaths/"
status = r"./DataInfo/status.txt"
version = r"./DataInfo/version.txt"
userfolder = r"./DataInfo/Users"

## FUNCTIONS
# ghost
def ghost():
    print("""\n

  .-')      ('-.   .-') _                 _ (`-.  
 ( OO ).  _(  OO) (  OO) )               ( (OO  ) 
(_)---\_)(,------./     '._ ,--. ,--.   _.`     \ 
/    _ |  |  .---'|'--...__)|  | |  |  (__...--'' 
\  :` `.  |  |    '--.  .--'|  | | .-') |  /  | | 
 '..`''.)(|  '--.    |  |   |  |_|( OO )|  |_.' | 
.-._)   \ |  .--'    |  |   |  | | `-' /|  .___.' 
\       / |  `---.   |  |  ('  '-'(_.-' |  |      
 `-----'  `------'   `--'    `-----'    `--'      """)
    
## START
def startup():
    ## INICIO
    os.system("clear")
    print(Fore.CYAN + f"Starting. . .\n")
    ghost()
    os.system("clear")
    ghost()
    print("\n\n")
    
    ## INFO
    print(Fore.MAGENTA + "[INFO] If there is an error while downloading file, press " + Fore.LIGHTCYAN_EX + "CTRL + C " + Fore.MAGENTA + " to continue.\n")
    
    ## data info
    createfile_datainfo()
        
    ## CHECK webpaths folder
    create_webpathsfolder()
        
    status_file()
    
    ## version
    version_file()
    
    ## users
    users_files()
    

# status.txt
def status_file():
    if not os.path.exists(status):
        
        print(Fore.LIGHTRED_EX + "[!] status.txt doesn't exist!\n")
        
        try:
            with open(status, "w") as f:
                f.write("Not status found.")
            
            print(Fore.CYAN + "- status.txt file created!\n\n")
            time.sleep(0.2)
        
        except Exception as err:
            os.system("clear")
            print(Fore.LIGHTRED_EX + f"An critical internal error has ocurred: {err}")
            print("\nExiting. . .")
            sys.exit()
        
        except KeyboardInterrupt as err:
            playerinput = input("Do you want to cancel the download? (y/n): ")
            
            if playerinput.lower() == "y" or playerinput.lower() == "yes":
                print(f"Download canceled")
            
            else:
                os.system("cls")
                createfile_datainfo()
                
    else:
        print(Fore.LIGHTGREEN_EX + "[+] status.txt already exists.\n\n")
                
    
            
# users.txt
def users_files():
    print("\n")
    if os.path.exists(userfolder):
        print(Fore.LIGHTGREEN_EX + "[+] Users path exists!\n")
        
    else:
        print(Fore.LIGHTRED_EX + "[-] Users folder doesn't exist!\n")
        try:
            os.mkdir(userfolder)
            print(Fore.CYAN + "- Created Users folder!\n\n")
            
            
        except Exception as err:
            os.system("clear")
            print(Fore.LIGHTRED_EX + f"[-] A fatal error has ocurred: {err}\n")
            print("a")
            print(Fore.YELLOW + "Exiting. . .")
            time.sleep(0.2)
            sys.exit()
    
            
# version.txt
def version_file():
    
    # NO EXISTE
    if not os.path.exists(version):
        print(Fore.LIGHTRED_EX + "[!] version.txt doesn't exist.\n")
        
        ## SERVER REQUEST
        version_url = f"https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/version_file.txt"
        server_response = requests.get(version_url)
        
        ## SERVER RESPONSE
        if server_response.status_code == 200:
            response = server_response.text
            response = response.strip()
            response_final = response.split(":", 1)
            Version_Name = response_final[0].strip()
            Version_Text = response_final[1].strip()
            
            ## CREATE FILE
            with open(version, "w") as f:
                f.write(response)
            
            print(Fore.CYAN + f"- Created version file!\n")
            print(Fore.LIGHTYELLOW_EX + f"= {Version_Name}: {Version_Text}")
    
    ## SI EXISTE
    else:
        print(Fore.LIGHTGREEN_EX + "[+] version.txt file exists!\n" + Fore.WHITE)
        
        ## SERVER REQUEST
        version_url = f"https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/version_file.txt"
        server_response = requests.get(version_url)
        
        ## SERVER RESPONSE
        if server_response.status_code == 200:
            response = server_response.text
            response = response.strip()
            response = response.split(":", 1)
            Version_Name = response[0]
            Version_Text = response[1]
            print(Fore.LIGHTYELLOW_EX + f"- {Version_Name}: {Version_Text}")
            
            ## CHECK
            with open(version, "r") as f:
                lineas = f.read()
                if not response == lineas:
                    wrongversion = True
                    
            if wrongversion:
                with open(version, "w") as f:
                    f.write(f"{Version_Name}: {Version_Text}")
    

# data info
def createfile_datainfo():
    if not os.path.exists(DataInfoFolder):
    
        try:
            print(Fore.LIGHTRED_EX + "[!] DataInfo folder doesn't exist!\n")
            os.mkdir(DataInfoFolder)
            
            print(Fore.CYAN + "- Datainfo Folder created!\n")
            time.sleep(0.2)
        
        except Exception as err:
            os.system("clear")
            print(Fore.LIGHTRED_EX + f"An critical internal error has ocurred: {err}")
            print("\nExiting. . .")
            sys.exit()
        
        except KeyboardInterrupt as err:
            playerinput = input("Do you want to cancel the download? (y/n): ")
            
            if playerinput.lower() == "y" or playerinput.lower() == "yes":
                print(f"Download canceled")
            
            else:
                os.system("clear")
                createfile_datainfo()
                
    else:
        print(Fore.LIGHTGREEN_EX + "[+] DataInfo Folder exists!\n\n")
            
# data setup.txt       
def createfile_setup():
    try:
        with open(setup, "w") as f:
            f.write("yes")
    
    except Exception as err:
        os.system("clear")
        print(Fore.LIGHTRED_EX + f"An critical internal error has ocurred: {err}")
        print("\nExiting. . .")
        sys.exit()
    
    except KeyboardInterrupt as err:
        playerinput = input("Do you want to cancel the download? (y/n): ")
        
        if playerinput.lower() == "y" or playerinput.lower() == "yes":
            print(f"Download canceled")
        
        else:
            os.system("cls")
            createfile_setup()
        
def create_webpathsfolder():
    if not os.path.exists(webpaths):
        print("\n" + Fore.LIGHTRED_EX + "[!] Webpaths folder doesn't exist.\n")
        
        try:
            os.mkdir(webpaths)
            
            print(Fore.CYAN + "- webpaths Folder created!\n\n")
            time.sleep(0.2)
        
        except Exception as err:
            os.system("clear")
            print(Fore.LIGHTRED_EX + f"An critical internal error has ocurred: {err}")
            print("\nExiting. . .")
            sys.exit()
        
        except KeyboardInterrupt as err:
            playerinput = input("Do you want to cancel the download? (y/n): ")
            
            if playerinput.lower() == "y" or playerinput.lower() == "yes":
                print(f"Download canceled")
            
            else:
                os.system("cls")
                createfile_datainfo()
                
    else:
        print(Fore.LIGHTGREEN_EX + "[+] Webpaths folder exists!\n\n")
            
            
def CreateFilesTXT():
        
    try:
        # downloads
        for i in tqdm(range(1), desc=f"🚀 Downloading File"):
            os.system(comando)
        time.sleep(0.25)
        print("\n" + Fore.CYAN + f"{namearchivo}.txt Downloaded succesfully!")
        print("=" * 50 + "\n\n")

    # excepts ERROR CRITICO    
    except Exception as err:
        os.system("clear")
        print(Fore.LIGHTRED_EX + f"An critical internal error has ocurred: {err}")
        print("\nExiting. . .")
        sys.exit()

    # excepts Keyboard interrupt
    except KeyboardInterrupt as err:
        playerinput = input("Do you want to cancel the download? (y/n): ")
        
        if playerinput.lower() == "y" or playerinput.lower() == "yes":
            print(f"Download canceled")

## START
startup()
    
## CREATE .TXT
if not os.path.exists(setup):
    # create it and write "yes" inside
    createfile_setup()
    
if not os.path.exists(version):
    version_file()

else:
    with open(setup, "r") as f:
        line = f.read()
        
        if not "yes" in line:
            # modify .txt and write "yes"
            createfile_setup()
            
    

# VARIABLES
links = {
    "common_paths": {
        "url": "https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/Common_Paths.txt"
    },

    "medium_common_paths": {
        "url": "https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/Medium-Common_Paths.txt"
    },

    "large_common_paths": {
        "url": "https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/Large-Common_Paths.txt"
    } ,

    "all_paths": {
        "url": "https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/All_Paths.txt"
    }
}

## GET FILES
for i in links:
    for clave, valor in links[i].items():
        pathdef = webpaths + i + ".txt"
        comando = f"wget -q -O{pathdef} {valor}"
        namearchivo = i
        
        print("\n" + "=" * 50)
        print(Fore.GREEN + f"DOWNLOADING {i}.txt\n")
        CreateFilesTXT()
        
## CHECK AND SET STATUS
allpaths = {
    "DataInfoFolder": r"./DataInfo",
    "setup": r"./DataInfo/setup.txt",
    "webpaths": r"./DataInfo/WebPaths/",
    "status": r"./DataInfo/status.txt",
    "version": r"./DataInfo/version.txt",
    "userfolder": r"./DataInfo/Users"
}

correctlinks = 0
for i in allpaths:
    if os.path.exists(allpaths[i]):
        correctlinks += 1
        
if len(allpaths) == correctlinks:
    with open(status, "w") as f:
        f.write("Ok")
        
        
print(Fore.YELLOW + f"All files downloaded succesfully!")
input(Fore.WHITE + f">> Press any button to continue with the program.")
os.system("clear")

## EMPEZAR CONSOLA
with open(status, "r") as f:
    lecturastatus = f.read()
    
if lecturastatus == "Ok":
    ## MAIN.PY PATH
    MainpyPath = r"./main.py"
    
    url = "https://raw.githubusercontent.com/ruubbeenn/Web-Explotation-CMD-Ruubbeenn/refs/heads/main/NecessaryFiles/main.py"
    preguntaservidor = requests.get(url)
    respuestaservidor = preguntaservidor.text
    with open(MainpyPath, "w") as f:
        f.write(respuestaservidor)
        
    os.system("python3 main.py")
else:
    print(Fore.LIGHTRED_EX + f"[!] A fatal error has ocurred checking status of setup." + Fore.WHITE + "\n")
    print(Fore.LIGHTYELLOW_EX + f"[NOTE] Please, launch again console.py!\n")
    input(Fore.WHITE + f"-> Press anywhere to continue.")
    os.system("clear")
