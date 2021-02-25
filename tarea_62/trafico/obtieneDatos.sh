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
# Obtenemos el nombre del fichero concreto, puesto que varía cada mes.
# Se ubica en una variable de entorno.
# nombrefichero="*.xml"
# Obtenemos el número de registros que se van a tratar.
#d=`head -2 $nombrefichero | tail -1 | cut -c 55-62`
#n=`expr $d + 2`
# Generamos un fichero diferente para cada campo.
#head -$n $nombrefichero | tail -$d | cut -c22-121 > descripcion.txt
#head -$n $nombrefichero | tail -$d | cut -c131-138 > coste.txt
# Unimos ambos ficheros y generamos un fichero .csv
xmlstarlet sel -t -m //List/Job -v @name -o "|" -v @id -n IncidenciasTDTGeo.xml > datos.csv

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