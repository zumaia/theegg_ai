#!/bin/bash
echo "Examinando versión de Ubuntu y fecha de instalación"
neofetch
lsb_release -a
ls -alct / |tail -1|awk '{print $6, $7, $8}'
echo "Examinando usuarios:"
whoami
id
a=$(wc -l /etc/passwd | cut -f 1 -d " ")
echo "Examinando conexión a Internet"
ping -c 1 https://theegg.ai/
echo "Total de líneas en el fichero de passwords: " $a
echo "Examinando sistema de ficheros"
df -h | grep -v loop | grep -v tmpfs
echo "Examinando la instalación de software: "
awk -W version 2> /dev/null | head -1
sed --version | head -1
grep --version | head -1
java -version
python --version
jq --version
xmlstarlet --version
csvstat --version
