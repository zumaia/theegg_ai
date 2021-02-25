# Actualizador

Este script sirve para actualizar el software y distribuciones de ubuntu

Abrimos un editor de texto plano

    #!/bin/bash
    sudo apt-get update
    sudo apt-get -y upgrade
    sudo apt-get -y dist-upgrade
    sudo apt-get clean
    sudo apt-get -y autoremove
    # reboot

Guardamos como actualizador.sh

Agregamos permisos de ejecución a este fichero con el comando chmod:

	oscar@oscar:~/Documentos/TheEgg/tarea_62 Scripting/trafico$  chmod +x actualizador.sh
	oscar@oscar:~/Documentos/TheEgg/tarea_62 Scripting/trafico$  ./actualizador.sh

Editamos el crontb

    $ sudo crontab -e
    
    o 
    
    $ crontab -e

añadimos esta linea

0 3 * * * sudo bash /home/oscar/Documentos/TheEgg/tarea_62 Scripting/actualizador

