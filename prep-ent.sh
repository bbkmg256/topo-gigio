#!/bin/bash

echo -e " * Preparando entorno...\n"
sleep 2

# Si binutils y python3-venv no están instalados
if [[ $(sudo dpkg --get-selections | grep binutils) == "" && $(sudo dpkg --get-selections | grep python3-venv) == "" ]]; then
	sudo apt update
	sudo apt install -y binutils python3-venv
fi

# Si no se encuentra el dir ".venv"
if [ $(ls .venv &> /dev/null; echo $?) -gt 0 ]; then
	python3 -m venv .venv
fi

# Ingresa en entorno virtual
source .venv/bin/activate
pip3 install -r requirements.txt
echo -e " * Entorno preparado!\n"
echo -e " * Ejecute 'source .venv/bin/activate' para entrar en el entorno virtual.\n"
exit 0
