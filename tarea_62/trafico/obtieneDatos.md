
Instalar xmlstarlet


#!/bin/bash
# Script para tratar datos.
# Accedemos primero a la carpeta donde deseamos realizar todo el tratamiento.
cd /home/oscar/Documentos/TheEgg/tarea_62 Scripting/trafico
# Suprimimos posibles ficheros anteriores.
# El parámetro -f fuerza a no pedir nada al usuario.
rm -f IncidenciasTrafikoTDTGeoZip
rm -f IncidenciasTDTGeo*.xml
rm -f datos.csv
# Obtenemos el fichero y lo descomprimimos.
wget https://www.trafikoa.eus/servicios/IncidenciasTDT/IncidenciasTrafikoTDTGeoZip
unzip IncidenciasTrafikoTDTGeo*

# Parseamos el fichero .xml y generamos un fichero .csv
	xmlstarlet sel -t \
	  -m / -o "tipo;autonomia;provincia;matricula;causa;poblacion;fechahora_ini;nivel;carretera;sentido;longitud;latitud" -n -b \
	  -m /raiz/incidenciaGeolocalizada  \
	  -v ../tipo -o ";" -v autonomia -o ";" \
	  -v provincia -o ";" -v matricula -o ";" \
	  -v causa -o ";" -v poblacion -o ";" \
	  -v fechahora_ini -o ";" -v nivel -o ";" \
	  -v carretera -o ";" -v sentido -o ";" \
	  -v longitud -o ";" -v latitud -n \
	IncidenciasTDTGeo.xml > datos.csv

Agregamos permisos de ejecución a este fichero con el comando chmod:

	oscar@oscar:~/Documentos/TheEgg/tarea_62 Scripting/trafico$  chmod +x obtieneDatos.sh
	oscar@oscar:~/Documentos/TheEgg/tarea_62 Scripting/trafico$  ./obtieneDatos.sh

-rwxr-xr-x 1 usuario usuario 1101 de se 27 06:32 obtieneDatos.sh
Agregar una línea al fichero «/etc/crontab» que automatizaría la ejecución:
30 7 2 * *     usuario     /home/oscar/Documentos/TheEgg/tarea_62 Scripting/traficoobtieneDatos.sh
A las 7:30 del día 2 de cada mes, en esta carpeta habrá un fichero «datos.csv»