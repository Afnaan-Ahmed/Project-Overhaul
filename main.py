import subprocess
import os
import tools  # Correct import statement

from utils import banner, color as c
tools.check_gnome_terminal()
def main_menu():
    subprocess.run("clear")
    print(c.light_cyan + banner.banner_text + c.reset)
    print(c.light_blue + "               MENU              " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Reconnaissance")
    print(c.light_red + "[2]" + c.reset + " - Exploitation")
    print(c.light_purple + "[3]" + c.reset + " - Miscellaneous")
    print(c.light_cyan + "[4]" + c.reset + " - Exit")
    print()
    
    response = input(" >    ")
    if response == '1':
        reconnaissance_menu()
    elif response == '2':
        exploitation_menu()
    elif response == '3':
        miscellaneous_menu()
    elif response == '4':
        print(c.light_cyan + "\nGoodbye!\n" + c.reset)
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        main_menu()

def reconnaissance_menu():
    print(c.light_blue + "               RECONNAISSANCE              " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Whois - (passive)")
    print(c.light_green + "[2]" + c.reset + " - NSlookup - (passive)")
    print(c.light_green + "[3]" + c.reset + " - Whatweb - (passive)")
    print(c.light_green + "[4]" + c.reset + " - Nmap - (active)")
    print(c.light_green + "[5]" + c.reset + " - Netcat - (active)")
    print(c.light_green + "[6]" + c.reset + " - Gobuster - (active)")
    print(c.light_green + "[7]" + c.reset + " - Amass - (active)")
    print(c.light_cyan + "[8]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        tools.launch_whois()
        main_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        tools.launch_nslookup()
        main_menu()
    elif response == '3':
        tools.launch_whatweb()
        main_menu()
    elif response == '4':
        tools.launch_nmap()
        main_menu()
    elif response == '5':
        tools.launch_netcat()
        main_menu()
    elif response == '6':
        tools.launch_gobuster()
        main_menu()
    elif response == '7':
        tools.launch_amass()
        main_menu()
    elif response == '8':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        reconnaissance_menu()

def exploitation_menu():
    print(c.light_blue + "               EXPLOITATION                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Metasploit")
    print(c.light_green + "[2]" + c.reset + " - SQLmap")
    print(c.light_green + "[3]" + c.reset + " - Hashcat")
    print(c.light_green + "[4]" + c.reset + " - John The Ripper")
    print(c.light_green + "[5]" + c.reset + " - Aircrack-ng")
    print(c.light_cyan + "[6]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        tools.launch_metasploit()
        main_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        tools.launch_sqlmap()
        main_menu()  
    elif response == '3':
        tools.launch_hashcat()
        main_menu()
    elif response == '4':
        tools.launch_john()
        main_menu()  
    elif response == '5':
        tools.launch_aircrack()
        main_menu()
    elif response == '6':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        exploitation_menu()

def miscellaneous_menu():
    print(c.light_blue + "               MISCELLANEOUS              " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Install all tools")
    print(c.light_green + "[2]" + c.reset + " - Install Gnome Terminal")
    print(c.light_cyan + "[3]" + c.reset + " - Back to main menu")

    response = input(" >    ")
    if response == '1':
        tools.install_all_tools()
        main_menu()  # Return to the main menu after installing tools
    elif response == '2':
        if tools.check_gnome_terminal():
            print(c.light_green + "Gnome Terminal is already installed" + c.reset)
        main_menu()
    elif response == '3':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        miscellaneous_menu()

try:
    main_menu()
except (KeyboardInterrupt, EOFError):
    print(c.light_red + "Program interrupted by user" + c.reset)
