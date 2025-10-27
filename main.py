import subprocess
import os
from tools import *
from menus import *
from utils import banner, color as c
from time import sleep

print(c.light_cyan + banner.banner_text + c.reset)
check_gnome_terminal()
if os.geteuid()!=0:
    print(c.red + "Not running as root, some features may not work correctly...." + c.reset)
    sleep(2)

try:
    main_menu()
except (KeyboardInterrupt, EOFError):
    print(c.light_red + "Program interrupted by user" + c.reset)
