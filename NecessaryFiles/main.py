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


## DICIONARIES
LoginOptions = {
    "1": "Login in a user.",
    "2": "Register a new user.",
    "3": "Exit."
}

# commands
commands = ["help", "pathmapper", "exit", "clear"]



helpcommand = {
    "help": {
        "PathMapper": "Searchs hidden paths on a web, such as /index.html, /admin.html.",
        "exit": "Exits the program. (Easy no?)",
        "webstatus": "Show's the status of a web [200, 403. . .]",
        "clear": "Clear's completely the screen."
    }

}


## Paths
UsersPath = r"./DataInfo/Users"
userfile = r"./DataInfo/user.txt"
setuppyfolder = r"./setup.py"
MainDirectory = r"./"


## BOOLEANS
creatinguser = False
creatingpass = False
onconsole = False
LoginIn = False
readbeforebool = False
loggedinauser = False
savepaths = False
onlyopenpaths = False
badusagepathmapper = False
finishedpathmapper = False
errorinwebstatus = False


## =============================
##        INFO OF USAGE
## =============================
def webstatushelp():
    os.system("clear")
    print(f"""
{Fore.YELLOW}==============================
         WEB STATUS
=============================={Fore.WHITE}

Webstatus is a tool that checks the current status of a {Fore.LIGHTGREEN_EX}website{Fore.WHITE}. It sends a request and displays what it receives on screen {Fore.YELLOW}[200, 403, etc.]{Fore.WHITE}.

{Fore.LIGHTYELLOW_EX}[?] INFO{Fore.WHITE}

You can enter {Fore.LIGHTBLUE_EX}https://{Fore.WHITE} or {Fore.LIGHTBLUE_EX}http://{Fore.WHITE} if you want, but keep in mind that you will then have to add {Fore.LIGHTRED_EX}www{Fore.WHITE}.


{Fore.YELLOW}[?] EXAMPLE OF USE{Fore.WHITE}

- {Fore.LIGHTBLUE_EX}webstatus exampleweb.com{Fore.WHITE}
- {Fore.LIGHTBLUE_EX}webstatus www.exampleweb.com{Fore.WHITE}
- {Fore.LIGHTBLUE_EX}webstatus exampleweb{Fore.WHITE}
""")
    
    input("\nPress Enter to Continue. ")
    os.system("clear")

def pathmapperinfo(): 
    os.system("clear")
    print(f"""
{Fore.YELLOW}================================
         PATH MAPPER
================================{Fore.WHITE}

Pathmapper is a web page port {Fore.LIGHTCYAN_EX}scanning tool{Fore.WHITE} that searches through a list of thousands of different combinations on a website. After scanning, it lists each and every port that exists, both blocked and accessible.

It is {Fore.LIGHTRED_EX}IMPORTANT{Fore.WHITE} to include both the www. format at the beginning and the {Fore.LIGHTRED_EX}attack level{Fore.WHITE} at the end!


{Fore.LIGHTYELLOW_EX}[?] FORMAT{Fore.WHITE}
      
You {Fore.LIGHTRED_EX}MUST{Fore.WHITE} use the following format:  

- {Fore.LIGHTBLUE_EX}https://www.<web>.<domain> |{Fore.WHITE}
- {Fore.LIGHTBLUE_EX}www.<web>.<com>{Fore.WHITE}


{Fore.LIGHTYELLOW_EX}[?] FLAGS{Fore.WHITE}

There are currently two flags in path mapper, which are as follows:

{Fore.LIGHTBLUE_EX}[-S]{Fore.WHITE} = Saves the attack in a .txt file that you can then view using {Fore.LIGHTGREEN_EX}openfile <file>{Fore.WHITE}.

{Fore.LIGHTBLUE_EX}[-O]{Fore.WHITE} = Only shows ports that are OPEN, i.e., hidden and blocked ports will not be shown.


{Fore.LIGHTYELLOW_EX}[?] ATTACK LEVELS{Fore.WHITE}

There are several types of attack levels, which vary according to the number of ports that will be tested in the scan. It is {Fore.LIGHTRED_EX}IMPORTANT{Fore.WHITE} to set the scan level at the end.

{Fore.LIGHTBLUE_EX}[1]{Fore.WHITE} = 4754 Combinations
{Fore.LIGHTBLUE_EX}[2]{Fore.WHITE} = 20496 Combinations
{Fore.LIGHTBLUE_EX}[3]{Fore.WHITE} = 37094 Combinations
{Fore.LIGHTBLUE_EX}[4]{Fore.WHITE} = 128385 Combinations


{Fore.LIGHTYELLOW_EX}[?] EXAMPLE OF USE{Fore.WHITE}

There are several ways to use pathmapper. You must enter a minimum of 2 words and a maximum of 5 words.

-> {Fore.LIGHTBLUE_EX}pathmapper www.exampleweb.com 1{Fore.WHITE} = (Basic attack)
-> {Fore.LIGHTBLUE_EX}pathmapper -S www.exampleweb.com 1{Fore.WHITE} = (Basic attack and save to txt.)
-> {Fore.LIGHTBLUE_EX}pathmapper -O www.exampleweb.com 2{Fore.WHITE} = (Medium attack and only open ports)
-> {Fore.LIGHTBLUE_EX}pathmapper -O -S www.exampleweb.com 1{Fore.WHITE} = (Basic attack and both parameters)
-> {Fore.LIGHTBLUE_EX}pathmapper -O -S www.exampleweb.com 4{Fore.WHITE} = (Maximum level attack, with both parameters)

""")
    
    input("Press Enter to continue")
    os.system("clear")


## =============================
##          S T A R T
## =============================


## START CONSOLE IF THERE ARE USERS
def startconsole():
    onconsole = True
    while onconsole:
        os.system("clear")
        print("""
  (`\ .-') /`   ('-. .-. .-')           ('-.  ) (`-.       _ (`-.                                  .-') _    
   `.( OO ),' _(  OO)\  ( OO )        _(  OO)  ( OO ).    ( (OO  )                                (  OO) )   
,--./  .--.  (,------.;-----.\       (,------.(_/.  \_)-._.`     \ ,--.      .-'),-----.   ,-.-') /     '._  
|      |  |   |  .---'| .-.  |        |  .---' \  `.'  /(__...--'' |  |.-') ( OO'  .-.  '  |  |OO)|'--...__) 
|  |   |  |,  |  |    | '-' /_)       |  |      \     /\ |  /  | | |  | OO )/   |  | |  |  |  |  \'--.  .--' 
|  |.'.|  |_)(|  '--. | .-. `.       (|  '--.    \   \ | |  |_.' | |  |`-' |\_) |  |\|  |  |  |(_/   |  |    
|         |   |  .--' | |  \  |       |  .--'   .'    \_)|  .___.'(|  '---.'  \ |  | |  | ,|  |_.'   |  |    
|   ,'.   |   |  `---.| '--'  /       |  `---. /  .'.  \ |  |      |      |    `'  '-'  '(_|  |      |  |    
'--'   '--'   `------'`------'        `------''--'   '--'`--'      `------'      `-----'   `--'      `--'    
\n""")
    
        print(Fore.LIGHTYELLOW_EX + f"\t  ACTIONS:\n" + Fore.WHITE)

        numcolors = 1
        # Options
        print("=" * 30)
        for i in LoginOptions:
            if numcolors == 1:
                print("[" + str(i) + "] " + Fore.LIGHTGREEN_EX + LoginOptions[i] + "\n")

            elif numcolors == 2:
                print("[" + str(i) + "] " + Fore.LIGHTBLUE_EX + LoginOptions[i] + "\n")
                
            elif numcolors == 3:
                print("[" + str(i) + "] " + Fore.LIGHTRED_EX + LoginOptions[i])

            print(Fore.WHITE, end=(""))
            numcolors += 1

        print("=" * 30)
            
        UserLoginAction = input("\nWhat do you want to do: ")

        # Check if parameter is valid
        if UserLoginAction.isdigit():
            # VALID!
            print("ES VALIDO!")

            ## Check if parameter in diccionary
            if UserLoginAction in LoginOptions:
                ## IT IS ON DICIONARY

                # LOGIN IN A USER
                if LoginOptions[UserLoginAction] == "Login in a user.":
                    onconsole = True
                    login()

                if LoginOptions[UserLoginAction] == "Register a new user.":
                    CreateNewUser()

                if LoginOptions[UserLoginAction] == "Exit.":
                    os.system("clear")
                    print(Fore.LIGHTGREEN_EX + "[+] Data Saved.\n")
                    print(Fore.LIGHTYELLOW_EX + "[?] Thanks for using Web Explotation by Rubennn. See you soon!\n")
                    input(Fore.WHITE + "Press Enter to exit.")
                    os.system("clear")
                    sys.exit()

            else:
                ## IT IS NOT IN DICIONARY
                os.system("clear")
                print(Fore.LIGHTRED_EX + f"[!] You have entered a wrong parameter.\n")
                print(Fore.LIGHTYELLOW_EX + f"[?] Your parameter: {UserLoginAction}\n")
                input(Fore.WHITE + f"Press enter to continue.")




        else:
            # NO VALID!
            os.system("clear")
            print(Fore.LIGHTRED_EX + f"[!] You must enter a valid parameter.\n")
            print(Fore.LIGHTYELLOW_EX + f"[?] Your parameter: {UserLoginAction}\n")
            input(Fore.WHITE + f"Press enter to continue.")

     
## LOGIN IN A USER
def login():
    LoginIn = True
    
    ## LOGIN
    while LoginIn:
        os.system("clear")
        print("""
  (`\ .-') /`   ('-. .-. .-')           ('-.  ) (`-.       _ (`-.                                  .-') _    
   `.( OO ),' _(  OO)\  ( OO )        _(  OO)  ( OO ).    ( (OO  )                                (  OO) )   
,--./  .--.  (,------.;-----.\       (,------.(_/.  \_)-._.`     \ ,--.      .-'),-----.   ,-.-') /     '._  
|      |  |   |  .---'| .-.  |        |  .---' \  `.'  /(__...--'' |  |.-') ( OO'  .-.  '  |  |OO)|'--...__) 
|  |   |  |,  |  |    | '-' /_)       |  |      \     /\ |  /  | | |  | OO )/   |  | |  |  |  |  \'--.  .--' 
|  |.'.|  |_)(|  '--. | .-. `.       (|  '--.    \   \ | |  |_.' | |  |`-' |\_) |  |\|  |  |  |(_/   |  |    
|         |   |  .--' | |  \  |       |  .--'   .'    \_)|  .___.'(|  '---.'  \ |  | |  | ,|  |_.'   |  |    
|   ,'.   |   |  `---.| '--'  /       |  `---. /  .'.  \ |  |      |      |    `'  '-'  '(_|  |      |  |    
'--'   '--'   `------'`------'        `------''--'   '--'`--'      `------'      `-----'   `--'      `--'    
\n""")
        ## SELECT USER
        userselected = input("> User: " + Fore.LIGHTGREEN_EX)
        seepath = r"./DataInfo/Users/" + userselected

        # CHECK IF USERSELECTED IS NOT EMPTY.
        if not userselected == "":
            
            if os.path.exists(seepath):
                ## PASS
                passSelected = getpass.getpass(Fore.WHITE + "> Password: " + Fore.LIGHTGREEN_EX)

                PassPathCheck = seepath + f"/pass.txt"
                if os.path.exists(PassPathCheck):

                    ## READ HASHED PASS
                    with open(PassPathCheck, "r") as f:
                        hashedpass = f.read().strip()

                    ## CHECK PASS
                    if bcrypt.checkpw(passSelected.encode("utf-8"), hashedpass.encode("utf-8")):
                        
                        # RIGHT PASS
                        os.system("clear")
                        print(Fore.LIGHTGREEN_EX + f"[+] Logged in on {userselected}!\n" + Fore.WHITE)
                        input("Press Enter to begin.")
                        LoginIn = False
                        readbefore(userselected)
                   
                    else:
                        # WRONG PASS
                        os.system("clear")
                        print(Fore.LIGHTRED_EX + """
  (`\ .-') /`   ('-. .-. .-')           ('-.  ) (`-.       _ (`-.                                  .-') _    
   `.( OO ),' _(  OO)\  ( OO )        _(  OO)  ( OO ).    ( (OO  )                                (  OO) )   
,--./  .--.  (,------.;-----.\       (,------.(_/.  \_)-._.`     \ ,--.      .-'),-----.   ,-.-') /     '._  
|      |  |   |  .---'| .-.  |        |  .---' \  `.'  /(__...--'' |  |.-') ( OO'  .-.  '  |  |OO)|'--...__) 
|  |   |  |,  |  |    | '-' /_)       |  |      \     /\ |  /  | | |  | OO )/   |  | |  |  |  |  \'--.  .--' 
|  |.'.|  |_)(|  '--. | .-. `.       (|  '--.    \   \ | |  |_.' | |  |`-' |\_) |  |\|  |  |  |(_/   |  |    
|         |   |  .--' | |  \  |       |  .--'   .'    \_)|  .___.'(|  '---.'  \ |  | |  | ,|  |_.'   |  |    
|   ,'.   |   |  `---.| '--'  /       |  `---. /  .'.  \ |  |      |      |    `'  '-'  '(_|  |      |  |    
'--'   '--'   `------'`------'        `------''--'   '--'`--'      `------'      `-----'   `--'      `--'    
\n""")
                        print(Fore.RED + "[!] Wrong password.\n")
                        input(Fore.WHITE + f"Press Enter to return.")

                            
                else:
                    # FILE DISSAPEARED & REMOVED
                    os.system("clear")
                    print(Fore.LIGHTRED_EX + f"[!] Internal error has occurred.\n")
                    print(f"[?] You " + Fore.LIGHTYELLOW_EX + " must " + Fore.WHITE + "solve it to continue.\n")
                    SolveAction = input(Fore.WHITE + f"Do you want to solve it? (y/n): ")

                    if SolveAction.lower() == "y" or SolveAction.lower() == "yes":
                        os.system("clear")
                        os.system("python3 setup.py")
                    
                    else:
                        os.system("clear")
                        print(Fore.LIGHTRED_EX + "[!] Exiting.\n")
                        time.sleep(1)
                        os.system("clear")
                        sys.exit()

            
            else:
                # NO VALID! | DOESN'T EXIST
                os.system("clear")
                print(Fore.LIGHTRED_EX + f"[!] You have entered a wrong username.\n")
                print(Fore.LIGHTYELLOW_EX + f"[?] Your parameter: {userselected}\n")
                input(Fore.WHITE + f"Press enter to continue.")
        
        else:
            ## EMPTY PARAMETER
            os.system("clear")
            print(Fore.LIGHTRED_EX + f"[!] You haven't entered a parameter.\n")
            print(Fore.LIGHTYELLOW_EX + f"[?] Returning.\n")
            input(Fore.WHITE + f"Press enter to continue.")
                

        
        
## SUCCESFULLY LOGGED IN
def readbefore(user):
    readbeforebool = True
    while readbeforebool:
        os.system("clear")
        print(Fore.LIGHTYELLOW_EX + f"[INFO]:" + Fore.WHITE + " Welcome " + Fore.GREEN + f"{user}" + Fore.WHITE + ", you've successfully logged in our service. Before continuing, we " + Fore.LIGHTGREEN_EX + "recommend reading " + Fore.WHITE + "this to clarify any questions you may have. With our " + Fore.LIGHTRED_EX + "exploit" + Fore.WHITE + ", you can use various functions, such as scanning hidden web paths, checking the status of websites, and many more!")

        print(f"\n- To get started, we " + Fore.LIGHTGREEN_EX + "recommend " + Fore.WHITE + "using the " + Fore.LIGHTCYAN_EX + "<help> " + Fore.WHITE + "command to " + Fore.LIGHTGREEN_EX + "learn " + Fore.WHITE + "about the commands.")

        print(f"\n- If you don't know how a command works, use " + Fore.LIGHTCYAN_EX + "<command> “--help”" + Fore.WHITE + ", which will show you more detailed information about the command.\n\n")

        readed = input(Fore.LIGHTYELLOW_EX + f"Have you read everything? (y/n): " + Fore.WHITE)


        if readed.lower() == "y" or readed.lower() == "yes":
            ## START CONSOLE
            LoggedIn(user)
            time.sleep(10)

        else:
            os.system("clear")
            print(Fore.LIGHTRED_EX + f"[!] Please read everything before starting the console.\n")

            input(Fore.WHITE + f"Press Enter to return.")


## =============================================
##                C O N S O L E
## =============================================

def LoggedIn(user):
    global finishedpathmapper
    global badusagepathmapper
    global savepaths
    global onlyopenpaths
    global errorinwebstatus

    loggedinauser = True
    
    ## CONSOLE LOOP
    os.system("clear")

    ## PRINT USER AND TIME
    while loggedinauser:
        action = input(Fore.LIGHTCYAN_EX + "[" + datetime.now().strftime("%H:%M") + "] " + Fore.WHITE + "|" + Fore.LIGHTGREEN_EX + f" {user}" + Fore.WHITE + "> ")
        separacion = action.split()

        ## ES COMANDO
        if action.lower() != "":

            ## HELP COMMAND
            if separacion[0].lower() == "help":
                lon = len(separacion)
                if lon == 1:
                    lastone = len(commands)
                    lastoneminus = lastone - 1
                    print("\nIf you want to know more about a command, use --help at the end of a command. \n- Example: " + Fore.LIGHTBLUE_EX + "pathmapper --help\n")
                    print(Fore.WHITE + "\nList of commands " + Fore.LIGHTCYAN_EX + "available" + Fore.WHITE + ":\n")
                    
                    ## LISTA PEQUEÑA
                    for i in range(lastone):
                        if not i == lastoneminus:
                            ## NOT THE LAST ONE
                            print(commands[i] + ",", end=(" "))

                        else:
                            ## THE LAST ONE
                            print(commands[i] + ".\n")

                    print(f"""{Fore.YELLOW}
=========================
      Advanced Info             
========================={Fore.WHITE}
""")
                    ## LISTA ENORME
                    for command, usage in helpcommand["help"].items():
                        print(f"{Fore.LIGHTYELLOW_EX}[{command}]{Fore.WHITE} = {usage}")

                    print("\n")

                else:
                    print(f"{Fore.LIGHTGREEN_EX}Help {Fore.WHITE}bad usage. {Fore.LIGHTGREEN_EX}Help {Fore.WHITE}command only takes 1 parameter [help].") 


            ## EXIT COMMAND
            elif separacion[0].lower() == "exit":
                lon = len(separacion)
                if lon == 1:
                    os.system("clear")
                    print(Fore.LIGHTGREEN_EX + "[+] Data Saved.\n")
                    input(Fore.WHITE + f"Press Enter to exit " + Fore.LIGHTYELLOW_EX + f"{user} " + Fore.WHITE + "account.")
                    os.system("clear")
                    startconsole()
                else:
                    print(f"{Fore.LIGHTRED_EX}Exit {Fore.WHITE}command bad usage. {Fore.LIGHTRED_EX}Only takes 1 parameter [exit].")


                                    ## CHECK WEB STATUS
            elif separacion[0].lower() == "webstatus":
                lon = len(separacion)
                
                if lon == 2:
                    
                    if separacion[1] == "--help":
                        webstatushelp()
                        continue
                    webacheckear = separacion[1]
                    
                    # confirmate website
                    if not webacheckear.startswith(("https://", "http://")):
                        if not webacheckear.endswith(".com"):
                            if not "www." in webacheckear:
                                # NO HTTPS \ NO .COM \ NO WWW.
                                webacheckear = f"https://www.{webacheckear}.com"

                            else:
                                errorinwebstatus = True


                        ## NO HTTPS pero si .com
                        else:
                            ## NO HTTPS \ SI.COM
                            if not "www." in webacheckear:

                                # NO HTTPS \ SI .COM \ NO WWW.
                                webacheckear = f"https://www.{webacheckear}"

                            else:
                                ## NO HTTPS \ SI .COM \ SI WWW.
                                webacheckear = f"https://{webacheckear}"



                    ## si tiene https://
                    else:

                        # SI HTTPS \ NO .COM \ NO WWW.
                        if not webacheckear.endswith(".com"):
                            if not "www." in webacheckear:

                                errorinwebstatus = True
                            
                            else:
                                # SI HTTPS \ SI WWW. \ SI COM
                                webacheckear = f"{webacheckear}.com"
                            
                        else:
                            if not "www." in webacheckear:
                            # SI HTTPS \ NO WWW. \ SI COM
                                errorinwebstatus = True

                    if not errorinwebstatus:
                        print(f"""{Fore.LIGHTCYAN_EX}
==========================
        WEB STATUS                         
==========================
{Fore.WHITE}""")

                        print(Fore.LIGHTYELLOW_EX + f"\n[?] Checking web status of " + Fore.LIGHTGREEN_EX + f"{webacheckear}\n" + Fore.WHITE)

                        ## TRY REQUEST
                        try:
                            serverrequest = requests.get(webacheckear)
                            statuscode = serverrequest.status_code

                            
                            ## OK REQUEST
                            if statuscode >= 200 and statuscode < 300:
                                print(f"{Fore.LIGHTGREEN_EX}-> [✓] {webacheckear}{Fore.WHITE} | {Fore.YELLOW}[{statuscode}] {Fore.WHITE}\n\n")

                            ## REDIRECT REQUESTS
                            elif statuscode >= 300 and statuscode < 400:
                                print(f"{Fore.LIGHTCYAN_EX}-> [→] {webacheckear}{Fore.WHITE} | {Fore.YELLOW}[{statuscode}] {Fore.WHITE}\n\n")

                            ## FORBIDEN
                            elif statuscode >= 400 and statuscode < 500:
                                print(f"{Fore.LIGHTRED_EX}-> [✗] {webacheckear}{Fore.WHITE} | {Fore.YELLOW}[{statuscode}] {Fore.WHITE}\n\n")
                            
                        
                        except Exception as err:
                            print(Fore.RED + f"[!] An error has occurred: \n{Fore.WHITE}{err}\n")

                    else:
                        print(f"Command {separacion[0]} bad usage. Use {Fore.LIGHTCYAN_EX}webstatus --help {Fore.WHITE}for more info!")


            ## COMMANDO CLEAR
            elif separacion[0] == "clear":
                lon = len(separacion)
                if lon == 1:
                    os.system("clear")
                
                else:
                    print(f"\nClear {Fore.LIGHTRED_EX}bad usage{Fore.WHITE}, clear tool only {Fore.LIGHTCYAN_EX}requires{Fore.WHITE} 1 parameter -> [clear]\n ")


            ## ===========================
            ##        PATH MAPP3R
            ## ===========================
            ## INICIO DEL PATHMAPPER

            elif separacion[0] == "pathmapper":
                try:
                    lon = len(comando)
                    comando = action.split()

                    if lon <= 5:
                            ## ES EL COMANDO PATHMAPPER
                            ## LEN DE 1 Y 2 | UNVALID
                            if lon == 1:
                                badusagepathmapper = True
                            
                            elif lon == 2:
                                if comando[1] == "--help":
                                    pathmapperinfo()
                                    continue
                                else:
                                    badusagepathmapper = True


                            ## LEN DE 3
                            elif lon == 3:
                                ## SAVE WEB
                                savedweb = comando[1]

                                ## LEVEL OF ATTACK
                                levelofattack = 1

                                if comando[2] == "1":
                                    levelofattack = 1
                                    finishedpathmapper = True
                                    FileToUseMapper = f"common_paths.txt"

                                elif comando[2] == "2":
                                    levelofattack = 2
                                    finishedpathmapper = True
                                    FileToUseMapper = f"medium_common_paths.txt"

                                elif comando[2] == "3":
                                    levelofattack = 3
                                    finishedpathmapper = True
                                    FileToUseMapper = f"large_common_paths.txt"


                                elif comando[2] == "4":
                                    levelofattack = 4
                                    finishedpathmapper = True
                                    FileToUseMapper = f"all_paths.txt"

                                else:
                                    badusagepathmapper = True

                            ## LEN DE 4
                            elif lon == 4:
                                if comando[1] == "-O":
                                    onlyopenpaths = True
                                elif comando[1] == "-S":
                                    savepaths = True
                                else:
                                    badusagepathmapper = True

                                ## SAVE WEB
                                savedweb = comando[2]

                                ## LEVEL OF ATTACK
                                levelofattack = 1

                                if comando[3] == "1":
                                    levelofattack = 1
                                    finishedpathmapper = True
                                    FileToUseMapper = f"common_paths.txt"

                                elif comando[3] == "2":
                                    levelofattack = 2
                                    finishedpathmapper = True
                                    FileToUseMapper = f"medium_common_paths.txt"

                                elif comando[3] == "3":
                                    levelofattack = 3
                                    finishedpathmapper = True
                                    FileToUseMapper = f"large_common_paths.txt"


                                elif comando[3] == "4":
                                    levelofattack = 4
                                    finishedpathmapper = True
                                    FileToUseMapper = f"all_paths.txt"

                                else:
                                    badusagepathmapper = True
                                    
                            ## LEN DE 5
                            elif lon == 5:
                                if comando[1] == "-S" and comando[2] == "-O" or comando[1] == "-O" and comando[2] == "-S":
                                    savepaths = True
                                    onlyopenpaths = True
                                else:
                                    badusagepathmapper = True

                                ## SAVE WEB
                                savedweb = comando[3]

                                ## LEVEL OF ATTACK
                                levelofattack = 1

                                if savepaths or onlyopenpaths:
                                    if comando[4] == "1":
                                        levelofattack = 1
                                        finishedpathmapper = True
                                        FileToUseMapper = f"common_paths.txt"
                                        
                                    elif comando[4] == "2":
                                        levelofattack = 2
                                        finishedpathmapper = True
                                        FileToUseMapper = f"medium_common_paths.txt"

                                    elif comando[4] == "3":
                                        levelofattack = 3
                                        finishedpathmapper = True
                                        FileToUseMapper = f"large_common_paths.txt"


                                    elif comando[4] == "4":
                                        levelofattack = 4
                                        finishedpathmapper = True
                                        FileToUseMapper = f"all_paths.txt"

                                    else:
                                        badusagepathmapper = True


                    else:
                        badusagepathmapper = True

                except IndexError:
                    badusagepathmapper = True
                    

                if not finishedpathmapper and badusagepathmapper == True:
                    ## BAD USAGE
                    print(f"pathmapper bad usage. Use " + Fore.LIGHTCYAN_EX + f"pathmapper --help " + Fore.WHITE + "for more info!")
                    finishedpathmapper = False
                    onlyopenpaths = False
                    savepaths = False

                    ## GOOD USAGE
                elif finishedpathmapper:
                    print(f"""
    {Fore.WHITE}===============================
    {Fore.LIGHTCYAN_EX}         PATH MAPPER
    {Fore.WHITE}===============================
                """)
                    
                    ## PRINT VARIABLES
                    # SAVE AS TXT PRINT
                    if savepaths:
                        print(f"Save Paths: " + Fore.LIGHTGREEN_EX + "True" + Fore.WHITE)
                    else:
                        print(f"Save Paths: " + Fore.LIGHTRED_EX + "False" + Fore.WHITE)

                    # ONLY OPEN PATH PRINT
                    if onlyopenpaths:
                        print(f"Only Open Pahts: " + Fore.LIGHTGREEN_EX + "True" + Fore.WHITE)
                    else:
                        print(f"Only Open Pahts: " + Fore.LIGHTRED_EX + "False" + Fore.WHITE)

                    # Web
                    print(f"Website: " + Fore.LIGHTGREEN_EX + f"{savedweb}" + Fore.WHITE)

                    # Number of attack | File to use
                    print(f"Level of attack: " + Fore.LIGHTGREEN_EX + f"{levelofattack} " + Fore.WHITE + "|" + Fore.LIGHTCYAN_EX + f" {FileToUseMapper}" + Fore.WHITE)

                    
                    # CONFIRMATIO
                    confirmation = input("\nAre you sure? (y/n): ")

                    if confirmation.lower() == "y" or confirmation.lower() == "yes":
                        os.system("clear")
                        print(Fore.LIGHTRED_EX + """
    ===============================
        INITIATING ATTACK
    ===============================
                """ + Fore.WHITE)

                        ## PATHS TO OPEN
                        PathMapperPathToOpen = r"./DataInfo/WebPaths/" + FileToUseMapper

                        # CHECK FILE
                        if os.path.exists(PathMapperPathToOpen):

                            ## OPEN FILE
                            with open(PathMapperPathToOpen, "r") as f:
                                lineas = f.read().splitlines()

                            ## CORRECT WEB
                            if not savedweb.startswith(("http://", "https://")):
                                finalweb = "https://" + savedweb
                            else:
                                finalweb = savedweb

                            finalweb = finalweb.rstrip("/")

                            ## SAVED WEBS
                            functionalwebs = []


                            ## CHECK WEBS FUNCTION
                            session = requests.Session()

                            def check_url(url):
                                try:
                                    r = session.get(url, timeout=1.5, allow_redirects=False)

                                    # Solo existe si responde 200
                                    if r.status_code == 200:
                                        return (url, "ok")

                                    # Opcional: si quieres ver paths que existen pero no tienes acceso
                                    elif r.status_code in [401, 403]:
                                        return (url, "forbidden")

                                except:
                                    pass

                                # Todo lo demás: ignorar
                                return None
                            
                            ## SAVED WEBS
                            results = {}

                            ## REVISAR HILOS Y ENVIAR MENSAJES  
                            max_hilos = 175

                            with ThreadPoolExecutor(max_workers=max_hilos) as executor:
                                envios = [
                                    executor.submit(check_url, f"{finalweb}/{i.strip()}")
                                    for i in lineas
                                ]

                                ## PROGRESSION BAR
                                for envio in tqdm(as_completed(envios), total=len(envios)):
                                    resultado = envio.result()

                                    if resultado:
                                        url, status = resultado
                                        results[url] = status

                                ## COMPLETED
                                print(Fore.LIGHTYELLOW_EX + "\n[?] Attack completed\n" + Fore.WHITE)

                                # Si no se encontró nada
                                if not results:
                                    print(Fore.LIGHTRED_EX + "[!] No hidden path has been found!\n" + Fore.WHITE)

                                else:
                                    # Mostrar resultados según onlyopenpaths
                                    ## OK
                                    for url, status in results.items():

                                        if onlyopenpaths and status != "ok":
                                            continue

                                        if status == "ok":
                                            print(Fore.LIGHTGREEN_EX + "[✓] " + url + Fore.WHITE)

                                    ## REDIRECT
                                    for url, status in results.items():
                                        if onlyopenpaths and status != "ok":
                                            continue

                                        if status == "redirect":
                                            print(Fore.LIGHTBLUE_EX + "[→] " + url + Fore.WHITE)

                                    ## FORBIDDEN
                                    for url, status in results.items():
                                        if onlyopenpaths and status != "ok":
                                            continue
                                        
                                        if status == "forbidden":
                                            print(Fore.LIGHTRED_EX + "[403] " + url + Fore.WHITE)

                                    # Guardar ataque si corresponde
                                    if savepaths:
                                        route = r"./DataInfo/Users/rubennn/PathMapperAttacks"
                                        numberofattacks = route + r"/numberofattacks.txt"

                                        # Crear carpeta si no existe
                                        if not os.path.exists(route):
                                            os.makedirs(route)

                                        # Crear o actualizar contador
                                        if not os.path.exists(numberofattacks):
                                            with open(numberofattacks, "w") as f:
                                                f.write("1")
                                            linea = "1"
                                        else:
                                            with open(numberofattacks, "r") as f:
                                                linea = f.read().strip()

                                            linea = int(linea) + 1

                                            with open(numberofattacks, "w") as f:
                                                f.write(str(linea))

                                        # Crear archivo del ataque
                                        attackfilemade = f"attack-{linea}.txt"
                                        attackmade = f"{route}/{attackfilemade}"

                                        # Guardar resultados
                                        with open(attackmade, "w") as f:
                                            for url, status in results.items():
                                                if onlyopenpaths and status != "ok":
                                                    continue
                                                f.write(f"{url} | {status}\n")

                                        print(Fore.LIGHTBLUE_EX + f"\n[?] Attack saved on {attackfilemade}!\n" + Fore.WHITE)
                                        print(Fore.WHITE + "[?] Enter the command " + Fore.LIGHTGREEN_EX + "openfile <file> " + Fore.WHITE + "to see the file.\n")

                                





                            
                    else:
                        print(Fore.LIGHTRED_EX + f"\n[!] Attack canceled\n")

                    print("\n")
                        
            else:
                print(f"Command {Fore.LIGHTRED_EX}{action}{Fore.WHITE} not found.\n")

                        




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
    
    ## CHECK IF THERE IS ANY USER CREATED
    if os.listdir(UsersPath):
        ## USER EXIST
        startconsole()

    else:
        ## NO USER EXIST
        CreateNewUser()



def CreateNewUser():
    creatinguser = True

    while creatinguser:
    # CREATE USER
    
        os.system("clear")
        print("""
           _  .-')     ('-.   ('-.     .-') _     ('-.                       .-')      ('-.  _  .-')   
          ( \( -O )  _(  OO) ( OO ).-.(  OO) )  _(  OO)                     ( OO ).  _(  OO)( \( -O )  
   .-----. ,------. (,------./ . --. //     '._(,------.       ,--. ,--.   (_)---\_)(,------.,------.  
  '  .--./ |   /`. ' |  .---'| \-.  \ |'--...__)|  .---'       |  | |  |   /    _ |  |  .---'|   /`. ' 
  |  |('-. |  /  | | |  |  .-'-'  |  |'--.  .--'|  |           |  | | .-') \  :` `.  |  |    |  /  | | 
 /_) |OO  )|  |_.' |(|  '--.\| |_.'  |   |  |  (|  '--.        |  |_|( OO ) '..`''.)(|  '--. |  |_.' | 
 ||  |`-'| |  .  '.' |  .--' |  .-.  |   |  |   |  .--'        |  | | `-' /.-._)   \ |  .--' |  .  '.' 
(_'  '--'\ |  |\  \  |  `---.|  | |  |   |  |   |  `---.      ('  '-'(_.-' \       / |  `---.|  |\  \  
   `-----' `--' '--' `------'`--' `--'   `--'   `------'        `-----'     `-----'  `------'`--' '--'                                         
        """)
        print(Fore.CYAN + "Max Length: 15" + Fore.WHITE + "\n")
        usernameinput = input("-> Create your unique username: ")
        userlen = len(usernameinput)

        ## CHECK IF ANOTHER USER EXISTS
        checkpath = r"./DataInfo/Users/" + usernameinput
        if os.path.exists(checkpath):
            os.system("clear")
            print(Fore.LIGHTRED_EX + "[!] User already exists.\n")
            print(Fore.LIGHTYELLOW_EX + "[?] Choose another username to continue.\n")
            input(Fore.WHITE + "Press anywhere to continue.")
        
        else:
        
        ## CHECK USER LENGHT
            if userlen < 15 and userlen > 0:
            
                ## CREATE PASS
                # user false
                creatinguser = False

                # pass true
                creatingpass = True

                while creatingpass:
                    os.system("clear")
                    print("""
           _  .-')     ('-.   ('-.     .-') _     ('-.           _ (`-.    ('-.      .-')     .-')    
          ( \( -O )  _(  OO) ( OO ).-.(  OO) )  _(  OO)         ( (OO  )  ( OO ).-. ( OO ).  ( OO ).  
   .-----. ,------. (,------./ . --. //     '._(,------.       _.`     \  / . --. /(_)---\_)(_)---\_) 
  '  .--./ |   /`. ' |  .---'| \-.  \ |'--...__)|  .---'      (__...--''  | \-.  \ /    _ | /    _ |  
  |  |('-. |  /  | | |  |  .-'-'  |  |'--.  .--'|  |           |  /  | |.-'-'  |  |\  :` `. \  :` `.  
 /_) |OO  )|  |_.' |(|  '--.\| |_.'  |   |  |  (|  '--.        |  |_.' | \| |_.'  | '..`''.) '..`''.) 
 ||  |`-'| |  .  '.' |  .--' |  .-.  |   |  |   |  .--'        |  .___.'  |  .-.  |.-._)   \.-._)   \ 
(_'  '--'\ |  |\  \  |  `---.|  | |  |   |  |   |  `---.       |  |       |  | |  |\       /\       / 
   `-----' `--' '--' `------'`--' `--'   `--'   `------'       `--'       `--' `--' `-----'  `-----'                                                                   
                """)
            
                    print("- User: " + Fore.LIGHTGREEN_EX + usernameinput)
                    print(Fore.CYAN + "Max pass lenght: 20" + Fore.WHITE + "\n")
                
                    ## INPUT PASS
                    passinput = getpass.getpass("-> Create your unique password: ")
                
                    ## CHECK PASS LENGHT
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
                        hashedpass = bcrypt.hashpw(passinput.encode("utf-8"), bcrypt.gensalt())

                        ## SAVE PASS
                        route = r"./DataInfo/Users/" + usernameinput
                        os.makedirs(route)

                        passwordtxtpath = route + "/pass.txt"

                        ## CREATE password.txt
                        with open(passwordtxtpath, "w") as f:
                            f.write(hashedpass.decode())

                        ## FINISH
                        os.system("clear")
                        print("""
               .-')      ('-.  _  .-')                                     .-') _                                
              ( OO ).  _(  OO)( \( -O )                                   ( OO ) )                               
 ,--. ,--.   (_)---\_)(,------.,------.          .-----.  .-'),-----. ,--./ ,--,'    ,------.,-.-')   ,----.     
 |  | |  |   /    _ |  |  .---'|   /`. '        '  .--./ ( OO'  .-.  '|   \ |  |\ ('-| _.---'|  |OO) '  .-./-')  
 |  | | .-') \  :` `.  |  |    |  /  | |        |  |('-. /   |  | |  ||    \|  | )(OO|(_\    |  |  \ |  |_( O- ) 
 |  |_|( OO ) '..`''.)(|  '--. |  |_.' |       /_) |OO  )\_) |  |\|  ||  .     |/ /  |  '--. |  |(_/ |  | .--, \ 
 |  | | `-' /.-._)   \ |  .--' |  .  '.'       ||  |`-'|   \ |  | |  ||  |\    |  \_)|  .--',|  |_.'(|  | '. (_/ 
('  '-'(_.-' \       / |  `---.|  |\  \       (_'  '--'\    `'  '-'  '|  | \   |    \|  |_)(_|  |    |  '--'  |  
  `-----'     `-----'  `------'`--' '--'         `-----'      `-----' `--'  `--'     `--'    `--'     `------'                                                                 
                          """)
                        print(Fore.LIGHTGREEN_EX + f"[+] User created succesfully!\n" + Fore.WHITE)
                        input("Press any button to continue.")
                        creatingpass = False
                        startconsole()
                    
                    
                  
                    
                    else: 
                        # BAD PASS
                        print(Fore.LIGHTRED_EX + f"[!] The pass is {len(usernameinput)} length, max is 20. Try again.\n")
                        input(Fore.WHITE + "Press any button to continue.")
                    
        
            else:
                print(Fore.LIGHTRED_EX + f"[!] The username is {len(usernameinput)} length, max is 15. Try again.\n")
                input(Fore.WHITE + "Press any button to continue.")


## START CHECK
if os.path.exists(UsersPath):
    
    ## load loading.
    loading()

else:
    os.system("clear")
    print(Fore.RED + f"[!] A fatal error has ocurred!\n")
    print(Fore.WHITE + f"In order to continue you" + Fore.LIGHTYELLOW_EX + " MUST SOLVE IT" + "." + Fore.WHITE)
    choice = input("\nDo you want to solve it (y/n): ")
    if choice.lower() == "y" or choice.lower() == "yes":
        if os.path.exists(setuppyfolder):
            os.system("clear")
            os.system("python3 setup.py")
            
            
        else:
            os.system("clear")
            print(Fore.RED + f"[!] We can't solve it automatically.\n" + Fore.WHITE)
            print(Fore.WHITE + f"[?] Relaunch console.py to solve it.\n")
            sys.exit()
