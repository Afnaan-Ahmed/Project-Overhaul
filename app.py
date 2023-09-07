import subprocess

# Welcome to Project Overhaul.

'''                         This tool is intended to integrate various penetration testing tools into a single command line script              '''

'''                         If you forgot what this tool does, just execute it and look at the output, it will guide you   '''

##############################################################################################################################################################

banner = '''
   ___             _         __    ____               __             __
  / _ \_______    (_)__ ____/ /_  / __ \_  _____ ____/ /  ___ ___ __/ /
 / ___/ __/ _ \  / / -_) __/ __/ / /_/ / |/ / -_) __/ _ \/ _ `/ // / / 
/_/  /_/  \___/_/ /\__/\__/\__/  \____/|___/\__/_/ /_//_/\_,_/\_,_/_/  
             |___/                                                     

                                                ~ Created by Afnaan'''

##############################################################################################################################################################

#                         Text Styles

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
brown = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
light_gray = "\033[0;37m"
dark_gray = "\033[1;30m"
light_red = "\033[1;31m"
light_green = "\033[1;32m"
yellow = "\033[1;33m"
light_blue = "\033[1;34m"
light_purple = "\033[1;35m"
light_cyan = "\033[1;36m"
light_white = "\033[1;37m"
bold = "\033[1m"
faint = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
blink = "\033[5m"
negative = "\033[7m"
crossed = "\033[9m"
reset = "\033[0m"




#                         Main menu

def main_menu():
    subprocess.run("clear")
    print(light_cyan + banner + reset)
    print()
    print(light_blue + "               MENU              ")
    print("              ------                " + reset)
    print()
    print(light_green + "[1]" + reset +" - Reconnaissance")
    print(light_red + "[2]" + reset + " - Exploitation")
    print(light_purple + "[3]" + reset + " - Miscellaneous")
    print(light_cyan + "[4]" + reset + " - Exit")
    print()
    response = input(" >    ")
    
    if response == '1':
        subprocess.run("clear", shell=True)
        reconnaissance_menu()

    elif response == '2':
        subprocess.run("clear", shell=True)
        exploitation_menu()
    
    elif response == '3':
        subprocess.run("clear", shell=True)
        miscellaneous_menu()
    
    elif response == '4':
        print(light_cyan + "\nGoodbye!\n" + reset)
    
    else:
        subprocess.run("clear", shell=True)
        print("")
        print(light_red + "Enter a valid option" + reset)
        main_menu()


#                             Reconnaissance menu

def reconnaissance_menu():
    print()
    print(light_blue + "               RECONNAISSANCE               ")
    print("              ----------------                    " + reset)
    print()
    print(light_green + "[1]" + reset + " - Nmap")
    print(light_cyan + "[2]" + reset + " - Back to main menu")
    print()

    response = input(" >    ")

    if response == '1':
        print()
        print(light_green + "Launching nmap..." + reset)
        print()
        result = subprocess.run("nmap",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: nmap is not installed" + reset)

    elif response == '2':
        main_menu()
    
    else:
        print("")
        print(light_red + "Enter a valid option" + reset)
        reconnaissance_menu()

#                             Exploitation menu

def exploitation_menu():
    print("")
    print(light_blue + "               EXPLOITATION                   ")
    print("              --------------                   " + reset)
    print("")
    print(light_green + "[1]" + reset + " - Metasploit")
    print(light_green + "[2]" + reset + " - SQLmap")
    print(light_green + "[3]" + reset + " - amass")
    print(light_cyan + "[4]" + reset + " - Back to main menu")
    print("")

    response = input(" >    ")

    if response == '1':
        print()
        print(light_green + "Launching Metasploit Framework..." + reset)
        print()
        result = subprocess.run("msfconsole",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: metasploit framework is not installed" + reset)

    elif response == '2':
        print()
        print(light_green + "Launching SQLmap..." + reset)
        print()
        result = subprocess.run("sqlmap",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: sqlmap is not installed" + reset)

    elif response == '3':
        print()
        print(light_green + "Launching amass..." + reset)
        print()
        result = subprocess.run("amass",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: amass is not installed" + reset)

    elif response == '4':
        main_menu()
    
    else:
        print()
        print(light_red + "Enter a valid option" + reset)
        exploitation_menu()

#                             Miscellaneous menu

def miscellaneous_menu():
    print()
    print(light_blue + "               MISCELLANEOUS               ")
    print("              ---------------                    " + reset)
    print()
    print(light_green + "[1]" + reset + " - Display Banner")
    print(light_cyan + "[2]" + reset + " - Back to main menu")
    print()

    response = input(" >    ")

    if response == '1':
        print(light_cyan + banner + reset)
        miscellaneous_menu()
    elif response == '2':
        main_menu()
    
    else:
        print("")
        print(light_red + "Enter a valid option" + reset)
        miscellaneous_menu()





#                           Running code
main_menu() 