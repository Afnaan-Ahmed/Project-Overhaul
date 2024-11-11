import subprocess
from time import sleep

# Helper function to check if a tool is installed
def check_tool_installed(tool):
    result = subprocess.run(f"which {tool}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

# Function to install tools
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

# Launch Nmap
def launch_nmap():
    tool = 'nmap'
    if check_tool_installed(tool):
        print("Launching Nmap...")
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'nmap; exec bash'])
    else:
        install_tool(tool, "sudo apt update && sudo apt install nmap -y")

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
