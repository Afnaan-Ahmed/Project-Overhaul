#!/usr/bin/python3

import subprocess
from time import sleep


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
        subprocess.run("clear", shell=True)
        print(light_blue + "               Mode               ")
        print("              -------                  " + reset)
        print()
        print(light_green + "[1]" + reset + " - Nmap Payload Generator")
        print(light_cyan + "[2]" + reset + " - Launch Nmap")
        print()

        response = input(" >    ")

        if response == '1':
            print()
            nmap_payload_generator()
            reconnaissance_menu()
        elif response == '2':
            print()
            print(light_green + "Launching nmap..." + reset)
            print()
            result = subprocess.run("nmap",stderr=subprocess.DEVNULL, shell=True)
            if result.returncode != 0:
                print(light_red + "Error: nmap is not installed" + reset)
                install = input("Do you wish to install nmap? (requires sudo password)")
                if install in ['YES','Y','yes','y','1','Yes','yES','yEs','YeS']:
                    print(light_green + "Installing Nmap..." + reset)
                    result = subprocess.run("sudo apt update && sudo apt install nmap",shell=True)
                    if result.returncode == 0:
                        print(light_green + "Nmap has been successfully installed" + reset)
                        reconnaissance_menu()
                    else:
                        print(light_red + "Could not install nmap! Please install it manually" + reset)
                else:
                    reconnaissance_menu()

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
    print(light_green + "[3]" + reset + " - John The Ripper")
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
            install = input("Do you wish to install Metasploit Framework? (requires sudo password)")
            if install in ['YES','Y','yes','y','1','Yes','yES','yEs','YeS']:
                print(light_green + "Installing Metasploit Framework..." + reset)
                result = subprocess.run("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall",shell=True)
                if result.returncode == 0:
                    print(light_green + "Metasploit Framework has been successfully installed" + reset)
                    exploitation_menu()
                else:
                    print(light_red + "Could not install Metasploit Framework! Please install it manually" + reset)
            else:
                exploitation_menu()

    elif response == '2':
        print()
        print(light_green + "Launching SQLmap..." + reset)
        print()
        result = subprocess.run("sqlmap",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: sqlmap is not installed" + reset)
            install = input("Do you wish to install sqlmap? (requires sudo password)")
            if install in ['YES','Y','yes','y','1','Yes','yES','yEs','YeS']:
                print(light_green + "Installing sqlmap..." + reset)
                result = subprocess.run("sudo apt update && sudo apt install python3-pip && sudo pip3 install sqlmap",shell=True)
                if result.returncode == 0:
                    print(light_green + "sqlmap has been successfully installed" + reset)
                    exploitation_menu()
                else:
                    print(light_red + "Could not install sqlmap! Please install it manually" + reset)
            else:
                exploitation_menu()

    elif response == '3':
        print()
        print(light_green + "Launching John The Ripper..." + reset)
        print()
        result = subprocess.run("john",stderr=subprocess.DEVNULL, shell=True)
        if result.returncode != 0:
            print(light_red + "Error: John the ripper is not installed" + reset)
            install = input("Do you wish to install John The Ripper? (requires sudo password)")
            if install in ['YES','Y','yes','y','1','Yes','yES','yEs','YeS']:
                print(light_green + "Installing John The Ripper..." + reset)
                result = subprocess.run("sudo apt update && sudo apt install john",shell=True)
                if result.returncode == 0:
                    print(light_green + "John The Ripper has been successfully installed" + reset)
                    exploitation_menu()
                else:
                    print(light_red + "Could not install John The Ripper! Please install it manually" + reset)
            else:
                exploitation_menu()
    

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
    print(light_green + "[2]" + reset + " - Install all tools included in project overhaul")
    print(light_cyan + "[3]" + reset + " - Back to main menu")
    print()

    response = input(" >    ")

    if response == '1':
        print(light_cyan + banner + reset)
        miscellaneous_menu()

    elif response == '2':
        print(light_green + "Installing all tools, This may take a while..." + reset)
        noerrors = True
        subprocess.run("sudo apt update",shell=True)
        
        #nmap
        print(light_green + "Installing nmap..." + reset)
        result = subprocess.run("sudo apt install nmap -y",shell=True)
        if result.returncode == 0:
            print(light_green + "Nmap has been successfully installed" + reset)
        else:
            print(light_red + "Could not install nmap! Please install it manually" + reset)
            noerrors = False
        
        #metasploit
        result = subprocess.run("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall",shell=True)
        if result.returncode == 0:
            print(light_green + "Metasploit Framework has been successfully installed" + reset)
        else:
            print(light_red + "Could not install Metasploit Framework! Please install it manually" + reset)
            noerrors = False
        
        #sqlmap
        print(light_green + "Installing sqlmap..." + reset)
        result = subprocess.run("sudo apt install python3-pip -y && sudo pip3 install sqlmap -y",shell=True)
        if result.returncode == 0:
            print(light_green + "sqlmap has been successfully installed" + reset)
        else:
            print(light_red + "Could not install sqlmap! Please install it manually" + reset)
            noerrors = False

        #John The Ripper
        print(light_green + "Installing John The Ripper..." + reset)
        result = subprocess.run("sudo apt install john -y",shell=True)
        if result.returncode == 0:
            print(light_green + "John the ripper has been successfully installed" + reset)
        else:
            print(light_red + "Could not install John The Ripper! Please install it manually" + reset)
            noerrors = False
        

        if noerrors == True:
            print(light_green + "All tools have been installed!" + reset)
        else:
            print(light_red + "one or more tools were not installed due to an error!" + reset)

    elif response == '3':
        main_menu()
    
    else:
        print("")
        print(light_red + "Enter a valid option" + reset)
        miscellaneous_menu()





#                       Nmap Payload Generator


def nmap_payload_generator():
    payload = "sudo nmap"
    subprocess.run("clear")
    print(light_cyan +"Scan type:"+reset)
    print(f'''
{light_green}[1] {reset}- TCP SYN port scan (Default)
{light_green}[2] {reset}- TCP connect port scan (Default without root privilege)
{light_green}[3] {reset}- UDP port scan
{light_green}[4] {reset}- TCP ACK port scan
{light_green}[5] {reset}- TCP Window port scan
{light_green}[6] {reset}- TCP Maimon port scan
{light_green}[7] {reset}- Skip''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-sS',
        '2':'-sT',
        '3':'-sU',
        '4':'-sA',
        '5':'-sW',
        '6':'-sM',
        '7':'',
    }
    try:
        payload += ' '+dictionary[response]
    except:
        print()
    
    subprocess.run("clear")
    print(light_cyan+"Host Discovery:"+reset)
    print(f'''
{light_green}[1] {reset}- No Scan. List targets only
{light_green}[2] {reset}- Disable port scanning. Host discovery only.
{light_green}[3] {reset}- Disable host discovery. Port scan only.
{light_green}[4] {reset}- TCP SYN discovery on port x. Port 80 by default
{light_green}[5] {reset}- TCP ACK discovery on port x. Port 80 by default
{light_green}[6] {reset}- UDP discovery on port x. Port 40125 by default
{light_green}[7] {reset}- ARP discovery on local network
{light_green}[8] {reset}- Never Do DNS resolution
{light_green}[9] {reset}- Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-sL',
        '2':'-sn',
        '3':'-Pn',
        '4':'-PS',
        '5':'-PA',
        '6':'-PU',
        '7':'-PR',
        '8':'-n',
        '9':'',
    }
    try:
        payload += ' '+dictionary[response]
    except:
        print()
    
    subprocess.run("clear")
    print(light_cyan + "Service and Version Detection:" + reset)
    print(f'''
{light_green}[1] {reset}- Detect OS 
{light_green}[2] {reset}- Detect Version of service
{light_green}[3] {reset}- Enables OS detection, version detection, script scanning, and traceroute
{light_green}[7] {reset}- Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-O',
        '2':'-sV',
        '3':'-A',
        '4':'',
        }
    try:
        payload += ' '+dictionary[response]
    except:
        print()

    subprocess.run("clear")
    print(light_cyan + "Scan Speed" + reset)
    print(f'''
{light_green}[1] {reset}- Paranoid - Intrusion Detection System evasion
{light_green}[2] {reset}- Sneaky - Intrusion Detection System evasion
{light_green}[3] {reset}- Polite - slows down the scan to use less bandwidth and use less target machine resources
{light_green}[4] {reset}- Normal - which is default speed
{light_green}[5] {reset}- Aggressive - speeds scans; assumes you are on a reasonably fast and reliable network
{light_green}[6] {reset}- Insane - speeds scan; assumes you are on an extraordinarily fast network
{light_green}[7] {reset}- Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-T0',
        '2':'-T1',
        '3':'-T2',
        '4':'-T3',
        '5':'-T4',
        '6':'-T5',
        '7':'',
        }
    try:
        payload += ' '+dictionary[response]
    except:
        print()
    

    subprocess.run("clear")
    print(light_cyan + "Scripts:" + reset)
    print(f'''
{light_green}[1] {reset}- Scan with default NSE scripts. Considered useful for discovery and safe
{light_green}[2] {reset}- Scan for vulnerabilities 
{light_green}[3] {reset}- Use only safe scripts
{light_green}[4] {reset}- Use intrusive scripts. Considered unsafe.
{light_green}[5] {reset}- Skip
''')
    response = input("> ")
    if response not in ['1','2','3','4','5','6','7','8','9']:
        print(light_red+"Invalid input, skipping..."+reset)
        sleep(0.7)

    dictionary = {
        '1':'-sC',
        '2':'--script=vuln',
        '3':'--script=safe',
        '4':'--script=intrusive',
        '5':'',
        }
    try:
        payload += ' '+dictionary[response]
    except:
        print()

    
    print()          
    print("Your payload is: "+light_green+ payload +" <IP address/range>" + reset)
    print("Replace <IP address/range>")
    print()









#                           Running code
try:
    main_menu()
except KeyboardInterrupt:
    print(light_red + "Program was interrupted by the user" + reset)