import subprocess
import os
from tools import *
from utils import banner, color as c

def main_menu():
    subprocess.run("clear")
    print(c.light_cyan + banner.banner_text + c.reset)
    print(c.light_blue + "               MENU              " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Passive Reconnaissance")
    print(c.light_yellow + "[2]" + c.reset + " - Active Reconnaissance")
    print(c.light_red + "[3]" + c.reset + " - Network Scanning")
    print(c.light_red + "[4]" + c.reset + " - Enumeration")
    print(c.red + "[5]" + c.reset + " - Exploitation")
    print(c.red  + "[6]" + c.reset + " - Web Application Hacking")
    print(c.light_blue + "[7]" + c.reset + " - Sniffing")
    print(c.light_red + "[8]" + c.reset + " - Hash Cracking")
    print(c.light_yellow + "[9]" + c.reset + " - Wordlist Building")
    print(c.red + "[10]" + c.reset + " - Bruteforce")
    print(c.red + "[11]" + c.reset + " - Wireless Hacking")
    print(c.red + "[12]" + c.reset + " - Social Engineering")
    print(c.light_green + "[13]" + c.reset + " - Miscellaneous")
    print(c.light_cyan + "[0]" + c.reset + " - Exit")
    print()
    
    response = input(" >    ")
    if response == '1':
        passive_reconnaissance_menu()
    elif response == '2':
        active_reconnaissance_menu()
    elif response == '3':
        network_scanning_menu()
    elif response == '4':
        enumeration_menu()
    elif response == '5':
        exploitation_menu()
    elif response == '6':
        web_application_hacking_menu()
    elif response == '7':
        sniffing_menu()
    elif response == '8':
        hash_cracking_menu()
    elif response == '9':
        wordlist_building_menu()
    elif response == '10':
        bruteforce_menu()
    elif response == '11':
        wireless_hacking_menu()
    elif response == '12':
        social_engineering_menu()
    elif response == '13':
        miscellaneous_menu()
    elif response == '0':
        print(c.light_cyan + "\nGoodbye...\n" + c.reset)
        sleep(1)
        subprocess.run("clear")
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        main_menu()

def passive_reconnaissance_menu():
    print(c.light_blue + "               RECONNAISSANCE              " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Whois - (passive)")
    print(c.light_green + "[2]" + c.reset + " - NSlookup - (passive)")
    print(c.light_green + "[3]" + c.reset + " - Whatweb - (passive)")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_whois()
        passive_reconnaissance_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        launch_nslookup()
        passive_reconnaissance_menu()
    elif response == '3':
        launch_whatweb()
        passive_reconnaissance_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        passive_reconnaissance_menu()

def active_reconnaissance_menu():
    print(c.light_blue + "               Active Reconnaissance                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Nmap - (active)")
    print(c.light_green + "[2]" + c.reset + " - Netcat - (active)")
    print(c.light_green + "[3]" + c.reset + " - Gobuster - (active)")
    print(c.light_green + "[4]" + c.reset + " - Amass - (active)")
    print(c.light_green + "[5]" + c.reset + " - Netdiscover")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_nmap()
        active_reconnaissance_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        launch_netcat()
        active_reconnaissance_menu()
    elif response == '3':
        launch_gobuster()
        active_reconnaissance_menu()
    elif response == '4':
        launch_amass()
        active_reconnaissance_menu()
    elif response == '5':
        launch_netdiscover()
        active_reconnaissance_menu()
    elif response == '0': 
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        active_reconnaissance_menu()

def network_scanning_menu():
    print(c.light_blue + "               Network Scanning                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Nmap")
    print(c.light_green + "[2]" + c.reset + " - Netcat")
    print(c.light_green + "[3]" + c.reset + " - Arp-Scan")
    print(c.light_green + "[4]" + c.reset + " - Netdiscover")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_nmap()
        network_scanning_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        launch_netcat()
        network_scanning_menu()  
    elif response == '3':
        launch_arpscan()
        network_scanning_menu()  
    elif response == '4':
        launch_netdiscover()
        network_scanning_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        network_scanning_menu()

def enumeration_menu():
    print(c.light_blue + "               Enumeration                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Amass")
    print(c.light_green + "[2]" + c.reset + " - NBTscan")
    print(c.light_green + "[3]" + c.reset + " - SMBmap")
    print(c.light_green + "[4]" + c.reset + " - DNSenum")
    print(c.light_green + "[5]" + c.reset + " - nmap")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_amass()
        enumeration_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        launch_nbtscan()
        enumeration_menu()  
    elif response == '3':
        launch_smbmap()
        enumeration_menu()
    elif response == '4':
        launch_dnsenum()
        enumeration_menu()
    elif response == '5':
        launch_nmap()
        enumeration_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        enumeration_menu()

def exploitation_menu():
    print(c.light_blue + "               EXPLOITATION                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Metasploit")
    print(c.light_green + "[2]" + c.reset + " - SQLmap")
    print(c.light_green + "[3]" + c.reset + " - Aircrack-ng")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_metasploit()
        exploitation_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        launch_sqlmap()
        exploitation_menu()  
    elif response == '3':
        launch_aircrack()
        exploitation_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        exploitation_menu()

def web_application_hacking_menu():
    print(c.light_blue + "               Web Application Hacking                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Whatweb")
    print(c.light_green + "[2]" + c.reset + " - Amass")
    print(c.light_green + "[3]" + c.reset + " - Gobuster")
    print(c.light_green + "[4]" + c.reset + " - SQLmap")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_whatweb()
        web_application_hacking_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        launch_amass()
        web_application_hacking_menu()  
    elif response == '3':
        launch_gobuster()
        web_application_hacking_menu()
    elif response == '4':
        launch_sqlmap()
        web_application_hacking_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        web_application_hacking_menu()

def sniffing_menu():
    print(c.light_blue + "               Sniffing                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Wireshark")
    print(c.light_green + "[2]" + c.reset + " - Ettercap")
    print(c.light_green + "[3]" + c.reset + " - dsniff")
    print(c.light_green + "[4]" + c.reset + " - ARPspoof")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_wireshark()
        sniffing_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        launch_ettercap()
        sniffing_menu()  
    elif response == '3':
        launch_dsniff()
        sniffing_menu()
    elif response == '4':
        launch_arpspoof()
        sniffing_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        sniffing_menu()

def hash_cracking_menu():
    print(c.light_blue + "               Hash Cracking                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Hashcat")
    print(c.light_green + "[2]" + c.reset + " - John The Ripper")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_hashcat()
        hash_cracking_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        launch_john()
        hash_cracking_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        hash_cracking_menu()

def wordlist_building_menu():
    print(c.light_blue + "               Wordlist Building                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - crunch")
    print(c.light_green + "[2]" + c.reset + " - cewl")
    print(c.light_green + "[3]" + c.reset + " - cupp")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_crunch()
        wordlist_building_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        wordlist_building_menu()
        main_menu()  
    elif response == '3':
        launch_cupp()
        wordlist_building_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        wordlist_building_menu()

def bruteforce_menu():
    print(c.light_blue + "               Bruteforce                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Hydra")
    print(c.light_green + "[2]" + c.reset + " - Medusa")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_hydra()
        bruteforce_menu()  # Return to the main menu after launching the tool
    elif response == '2':
        bruteforce_menu()
        main_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        bruteforce_menu()

def wireless_hacking_menu():
    print(c.light_blue + "               Wireless Hacking                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Aircrack-ng")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_aircrack()
        wireless_hacking_menu()  # Return to the main menu after launching the tool
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        wireless_hacking_menu()

def social_engineering_menu():
    print(c.light_blue + "               Social Engineering                " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - SEToolkit")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")
    print()

    response = input(" >    ")
    if response == '1':
        launch_setoolkit()
        social_engineering_menu()  # Return to the main menu after launching the tool
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        social_engineering_menu()

def miscellaneous_menu():
    print(c.light_blue + "               MISCELLANEOUS              " + c.reset)
    print(c.light_green + "[1]" + c.reset + " - Install all tools")
    print(c.light_green + "[2]" + c.reset + " - Install Gnome Terminal")
    print(c.light_green + "[3]" + c.reset + " - Display Banner")
    print(c.light_cyan + "[0]" + c.reset + " - Back to main menu")

    response = input(" >    ")
    if response == '1':
        install_all_tools()
        miscellaneous_menu()  # Return to the main menu after installing tools
    elif response == '2':
        if check_gnome_terminal():
            print(c.light_green + "Gnome Terminal is already installed" + c.reset)
        miscellaneous_menu()
    elif response == '3':
        print(c.light_cyan + banner.banner_text + c.reset)
        miscellaneous_menu()
    elif response == '0':
        main_menu()
    else:
        print(c.light_red + "Enter a valid option" + c.reset)
        miscellaneous_menu()