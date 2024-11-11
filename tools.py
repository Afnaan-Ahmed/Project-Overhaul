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




#     Functions to launch tools:


# Reconnaissance Menu

# Launch Nmap
def launch_nmap():
    tool = 'nmap'
    if check_tool_installed(tool):
        print("Launching Nmap...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'nmap; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install nmap -y")

# Launch Netcat
def launch_netcat():
    tool = 'netcat'
    if check_tool_installed(tool):
        print("Launching Netcat...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'netcat; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install netcat -y")

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




# Exploitation Menu

# Launch Metasploit
def launch_metasploit():
    tool = 'msfconsole'
    if check_tool_installed(tool):
        print("Launching Metasploit...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'msfconsole; exec bash'])
    else:
        install_tool(tool, "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")

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






# Miscellaneous Function to install all tools used in the project

def install_all_tools():
    print(c.light_green + "Installing all tools; this may take a while..." + c.reset)
    
    # Update the system first
    subprocess.run("sudo apt update", shell=True)
    
    tools = {
	    "Nmap": "sudo apt install nmap -y",
        "Netcat": "sudo apt install netcat -y",
	    "Whois": "sudo apt install whois -y",
	    "NSlookup": "sudo apt install nslookup -y",
        "Metasploit": "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall",
        "SQLmap": "sudo apt install sqlmap -y",
    	"Hashcat": "sudo apt install hashcat -y",
        "John The Ripper": "sudo apt install john -y",
        "aircrack-ng": "sudo apt install aircrack-ng -y"
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