import subprocess
from time import sleep
from utils import color as c

# Helper function to check if a tool is installed
def check_tool_installed(tool):
    result = subprocess.run(f"which {tool}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

# Function to install tool
def install_tool(tool, install_command):
    print(f"{tool} is not installed.")
    install = input(f"Do you want to install {tool}? (y/n): ").strip().lower()
    if install in ['y', 'yes']:
        print(f"Installing {tool}...")
        result = subprocess.run(install_command, shell=True)
        if result.returncode == 0:
            print(f"{tool} has been successfully installed.")
        else:
            print(f"Could not install {tool}. Please install it manually.")
    else:
        print(f"{tool} will not be installed. Returning to the previous menu.")
    sleep(1)

# Function to check if gnome-terminal is installed
def check_gnome_terminal():
    tool = 'gnome-terminal'
    if check_tool_installed(tool) == False:
        install_tool(tool, "sudo apt update && sudo apt install gnome-terminal -y")
        sleep(3)

#     Functions to launch tools:


# Reconnaissance Menu

# Launch whois
def launch_whois():
    tool = 'whois'
    if check_tool_installed(tool):
        print("Launching Whois...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'whois; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install whois -y")

# Launch nslookup
def launch_nslookup():
    tool = 'nslookup'
    if check_tool_installed(tool):
        print("Launching Nslookup...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'nslookup; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install nslookup -y")

# Launch Nmap
def launch_nmap():
    tool = 'nmap'
    if check_tool_installed(tool):
        print("Launching Nmap...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'nmap; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install nmap -y")

# Launch Arp-scan
def launch_arpscan():
    tool = 'arp-scan'
    if check_tool_installed(tool):
        print("Launching Arp-scan...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'arp-scan; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install arp-scan -y")
 
# Launch Netcat
def launch_netcat():
    tool = 'netcat'
    if check_tool_installed(tool):
        print("Launching Netcat...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'netcat; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install netcat -y")

# Launch Gobuster
def launch_gobuster():
    tool = 'gobuster'
    if check_tool_installed(tool):
        print("Launching Gobuster...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'gobuster; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install gobuster -y")

# Launch Amass
def launch_amass():
    tool = 'amass'
    if check_tool_installed(tool):
        print("Launching Amass...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'amass; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install amass -y")

# Launch Whatweb
def launch_whatweb():
    tool = 'whatweb'
    if check_tool_installed(tool):
        print("Launching Whatweb...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'whatweb; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install whatweb -y")

# Launch Metasploit
def launch_metasploit():
    tool = 'msfconsole'
    if check_tool_installed(tool):
        print("Launching Metasploit...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'msfconsole; exec bash'])
    else:
        install_tool(tool, "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall && rm msfinstall")

# Launch SQLmap
def launch_sqlmap():
    tool = 'sqlmap'
    if check_tool_installed(tool):
        print("Launching SQLmap...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'sqlmap; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install python3-pip -y && sudo pip3 install sqlmap")

# Launch Hashcat
def launch_hashcat():
    tool = 'hashcat'
    if check_tool_installed(tool):
        print("Launching Hashcat...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'hashcat; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install hashcat -y")

# Launch John The Ripper
def launch_john():
    tool = 'john'
    if check_tool_installed(tool):
        print("Launching John The Ripper...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'john; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install john -y")

# Launch Aircrack-ng
def launch_aircrack():
    tool = 'aircrack-ng'
    if check_tool_installed(tool):
        print("Launching Aircrack-ng...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'aircrack-ng; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install aircrack-ng -y")

# Launch Hydra
def launch_hydra():
    tool = 'hydra'
    if check_tool_installed(tool):
        print("Launching Hydra...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'hydra; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install hydra -y")

# Launch Medusa
def launch_medusa():
    tool = 'medusa'
    if check_tool_installed(tool):
        print("Launching Medusa...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'medusa; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install medusa -y")

# Launch Wireshark
def launch_wireshark():
    tool = 'wireshark'
    if check_tool_installed(tool):
        print("Launching Wireshark...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'wireshark; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install wireshark -y")

# Launch Ettercap in GUI mode
def launch_ettercap():
    tool = 'ettercap-graphical'
    if check_tool_installed(tool):
        print("Launching Ettercap...")
        subprocess.run("ettercap -G",shell=True)
    else:
        install_tool(tool, "sudo apt update && sudo apt install ettercap-graphical -y")

# Launch Netdiscover
def launch_netdiscover():
    tool = 'netdiscover'
    if check_tool_installed(tool):
        print("Launching Netdiscover...")
        subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'netdiscover; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install netdiscover -y")

# Launch NBTscan
def launch_nbtscan():
    tool = 'nbtscan'
    if check_tool_installed(tool):
        print("Launching NBTscan...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'nbtscan; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install nbtscan -y")

# Launch SMBmap
def launch_smbmap():
    tool = 'smbmap'
    if check_tool_installed(tool):
        print("Launching SMBmap...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'smbmap; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install smbmap -y")

# Launch DNSenum
def launch_dnsenum():
    tool = 'dnsenum'
    if check_tool_installed(tool):
        print("Launching DNSenum...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'dnsenum; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install dnsenum -y")

# Launch dsniff
def launch_dsniff():
    tool = 'dsniff'
    if check_tool_installed(tool):
        print("Launching dsniff...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'dsniff; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install dsniff -y")

# Launch ARPspoof
def launch_arpspoof():
    tool = 'arpspoof'
    if check_tool_installed(tool):
        print("Launching Arpspoof...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'arpspoof; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install dsniff -y")

# Launch Crunch
def launch_crunch():
    tool = 'crunch'
    if check_tool_installed(tool):
        print("Launching Crunch...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'crunch; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install crunch -y")

# Launch cewl
def launch_cewl():
    tool = 'cewl'
    if check_tool_installed(tool):
        print("Launching cewl...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'cewl; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install cewl -y")

# Launch cupp
def launch_cupp():
    tool = 'cupp'
    if check_tool_installed(tool):
        print("Launching Cupp...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'cupp; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install cupp -y")

# Launch SEToolkit
def launch_setoolkit():
    tool = 'setoolkit'
    if check_tool_installed(tool):
        print("Launching setoolkit...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'setoolkit; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install setoolkit -y")



# Miscellaneous Function to install all tools used in the project

def install_all_tools():
    print(c.light_green + "Installing all tools; this may take a while..." + c.reset)
    
    # Update the system first
    subprocess.run("sudo apt update", shell=True)
    
    tools = {
        "Gnome-terminal": "sudo apt install gnome-terminal -y",
	    "Whois": "sudo apt install whois -y",
	    "NSlookup": "sudo apt install nslookup -y",
	    "Whatweb": "sudo apt install whatweb -y",
	    "Nmap": "sudo apt install nmap -y",
        "Netcat": "sudo apt install netcat-traditional -y",
	    "NBTscan": "sudo apt install nbtscan -y",
	    "SMBmap": "sudo apt install smbmap -y",
	    "DNSenum": "sudo apt install dnsenum -y",
        "Arp-Scan":"sudo apt install arp-scan -y",
        "Netdiscover": "sudo apt install netdiscover",
	    "Gobuster": "sudo apt install gobuster -y",
	    "Amass": "sudo apt install amass -y",
        "Metasploit": "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall && rm msfinstall",
        "SQLmap": "sudo apt install sqlmap -y",
    	"Hashcat": "sudo apt install hashcat -y",
        "John The Ripper": "sudo apt install john -y",
        "Crunch": "sudo apt install crunch -y",
        "Cewl": "sudo apt install cewl -y",
        "Cupp": "sudo apt install cupp -y",
        "Hydra": "sudo apt install hydra -y",
        "Medusa": "sudo apt install medusa -y",
        "aircrack-ng": "sudo apt install aircrack-ng -y",
        "Wireshark": "sudo apt install wireshark -y",
	    "dsniff": "sudo apt install dsniff -y",
        "ettercap": "sudo apt install ettercap-graphical -y"
    }

    installation_success = True  # Flag to track if all installations succeed
    
    for tool, command in tools.items():
        print(c.light_yellow + f"Installing {tool}..." + c.reset)
        
        # Run the installation command
        result = subprocess.run(command, shell=True)
        
        # Check if the command was successful (return code 0 means success)
        if result.returncode != 0:
            print(c.red + f"Error installing {tool}." + c.reset)
            installation_success = False

    # Print a success or failure message
    if installation_success:
        print(c.light_green + "All tools have been installed!" + c.reset)
    else:
        print(c.red + "Some tools failed to install. Please check the errors above." + c.reset)