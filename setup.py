# Setup.py EvilShell
# Noctis Atrae, ver.0.1.5

import os
import sys


banner = """
▓█████ ██▒   █▓ ██▓ ██▓         ██████  ██░ ██ ▓█████  ██▓     ██▓    
▓█   ▀▓██░   █▒▓██▒▓██▒       ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    
▒███   ▓██  █▒░▒██▒▒██░       ░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    
▒▓█  ▄  ▒██ █░░░██░▒██░         ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    
░▒████▒  ▒▀█░  ░██░░██████▒   ▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
░░ ▒░ ░  ░ ▐░  ░▓  ░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
 ░ ░  ░  ░ ░░   ▒ ░░ ░ ▒  ░   ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░
   ░       ░░   ▒ ░  ░ ░      ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   
   ░  ░     ░   ░      ░  ░         ░   ░  ░  ░   ░  ░    ░  ░    ░  ░ 
Noctis_Atrae, v0.1, setup.py
"""

print(banner)
print("""setup.py va installer tout les modules nécessaires à l'éxecution d'EvilShell. Voici la liste de ce(s) module(s) :
- Termcolor
""")
while True:
  choix = input("Êtes-vous d'accord (O/n) ?: ")
  if choix == "O" or "o":
    os.system("python3 -m pip install termcolor")
  elif choix == "N" or "n":
    sys.exit("OK ! Au revoir !")
