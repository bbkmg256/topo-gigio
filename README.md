# Remote Access Trojan
Trojano de acceso remoto (RAT) con Python.

[SOLO LINUX, por ahora]

# Requerido:
	* Sistema (APT):
		* Docker (solo para compilar cliente windows desde linux) [No requerido de momento]
		* Binutils
		* Python-venv
	* PIP3:
		* Configparser
		* Pyinstaller

# Script de preparacion:
Puede ejecutar el script "prep-ent.sh" una vez (o cada que limine el directorio oculto '.venv') para preparar el entorno descargando los paquetes necesarios de APT y de PIP3 para cumplimentar las dependencias.

Bash:
	```
	sudo chmod +x prep-ent.sh
	./prep-ent.sh
	```

# Mini demostración:
![Demo](https://github.com/bbkmg256/topo-gigio/raw/main/assets/demo.gif)
