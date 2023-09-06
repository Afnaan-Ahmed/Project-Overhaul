# Welcome to Project Overhaul.

'''                         This tool is intended to integrate various pen testing tools into a single command line script              '''

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


'''                                                         Function Definitions                                                        '''


def main_menu():
    print("")
    print("               MENU              ")
    print("              ------                ")
    print("")
    print("[1] - Reconnaissance")
    print("[2] - Exploitation")
    print("[3] - Miscellaneous")
    print("[4] - Exit")
    print("")
    response = input(" >    ")
    
    if response == '1':
        reconnaissance_menu()

    elif response == '2':
        exploitation_menu()
    
    elif response == '3':
        miscellaneous_menu()
    
    elif response == '4':
        print("\nGoodbye!")
    
    else:
        print("Enter a valid option")
        main_menu()



def reconnaissance_menu():
    print("")
    print("               RECONNAISSANCE               ")
    print("              ----------------                    ")
    print("")
    print("[1] - Nmap")
    print("[2] - Back to main menu")
    print("")

    response = input(" >    ")

    if response == '1':
        print("Starting Nmap...")

    elif response == '2':
        main_menu()
    
    else:
        print("Enter a valid option")
        reconnaissance_menu()


def exploitation_menu():
    print("")
    print("               EXPLOITATION                ")
    print("              --------------                   ")
    print("")
    print("[1] - Metasploit")
    print("[2] - SQLmap")
    print("[3] - amass")
    print("[4] - ffuf")
    print("[5] - Dirbuster")
    print("[6] - Back to main menu")
    print("")

    response = input(" >    ")

    if response == '1':
        print("Launching Metasploit Framework...")

    elif response == '2':
        print("Launching SQLmap...")

    elif response == '3':
        print("Launching Amass...")

    elif response == '4':
        print("Launching FFUF...")

    elif response == '5':
        print("Launching Dirbuster...")

    elif response == '6':
        main_menu()
    
    else:
        print("Enter a valid option")
        exploitation_menu()


def miscellaneous_menu():
    print("")
    print("               MISCELLANEOUS               ")
    print("              ---------------                    ")
    print("")
    print("[1] - Display Banner")
    print("[2] - Back to main menu")
    print("")

    response = input(" >    ")

    if response == '1':
        print(banner)

    elif response == '2':
        main_menu()
    
    else:
        print("Enter a valid option")
        miscellaneous_menu()




print(banner)
main_menu() 