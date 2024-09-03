#!/bin/bash

# Script de preparacion de entorno.

comprobar(){
	if [ $(echo $?) -gt 0 ]; then
		echo -e " * Algo falló en la preparacion del entorno\n"
		exit 1
	fi
}

echo -e " * Preparando entorno...\n"
sleep 2

# Si binutils y python3-venv no están instalados
if [[ $(sudo dpkg --get-selections | grep binutils) == "" || $(sudo dpkg --get-selections | grep python3-venv) == "" ]]; then
	echo -e " * Instalando requerimientos APT\n"
	sudo apt update
	sudo apt install -y binutils python3-venv
else
	echo -e " * Requerimientos APT cumplidos!\n"
fi

comprobar

# Si no se encuentra el dir ".venv"
echo -e " * Verificando si exiten algun directorio .venv\n"
if [ $(ls .venv &> /dev/null; echo $?) -gt 0 ]; then
	echo -e " * Creando directorio .venv\n"
	python3 -m venv .venv
else
	echo -e " * Ya existe un directorio .venv!\n"
fi

comprobar

# Ingresa en entorno virtual
source .venv/bin/activate
pip3 install -r requirements.txt
echo -e " * Entorno preparado!\n"
echo -e " * Ejecute 'source .venv/bin/activate' para entrar en el entorno virtual.\n"
exit 0
