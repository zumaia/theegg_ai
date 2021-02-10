# Empezando con las redes de comunicación

![](https://www.ionos.es/digitalguide/fileadmin/DigitalGuide/Screenshots_2019/ip-adresse-EN-1.png)
¿Quién no ha hecho alguna vez un "teléfono" con 2 envases de yogur y un hilo para unirlos? Este podría ser un ejemplo gráfico de cómo funcionan las redes digitales:  

1.- Los yogures serían los ordenadores  
2.- El hilo sería la fibra óptica o el ADSL  

Ahora, imagínate no dos sino millones de yogures con millones de hilos transmitiendo mensajes secretos de uno a otro. Necesitaríamos de intermediarios, de gestores que se encarguen de que las comunicaciones lleguen a su destino. Árbitros que se encarguen de conectar nuestro ordenador de casa con el ordenador de destino, bien sea este un servidor (web, FTP, etc.) o incluso el ordenador de un amiguete.  

Estos mediadores son los routers, los gestores que conectan tú ordenador con las redes que hay fuera de tu casa. Son el puente digital (se les llama puerta de enlace o gateway) entre tu lugar de confort y el salvaje Mundo digital.

Los routes no son los únicos que intervienen en estas comunicaciones pero sí los más importantes. En cualquier caso, existen otros "aparatos" electrónicos como los switch-es o los hub-s que también son arte y parte. Mira este vídeo para entender la diferencia entre estos tres dispositivos.  

Después de esta expicación:

a.- Habrás deducido que Internet no es la única red global que existe, aunque sí la más importante y grande.  
b.- Habrás imaginado que hay redes de diferentes tamaños y construidas para diferentes propósitos.  
c.- Habrás concluido que el idioma que utilizan los ordenadores para comunicarse no es el mismo que utilizamos cuando hablamos desde un yogur.

¿Y qué idioma utilizan los ordenadores para comunicarse?

Los idiomas digitales se conocen como protocolos de comunicación y existen de diferentes tipos. Un protocolo no es mas que un idioma común que los ordenadores deben entender para comunicarse. Son secuencias de bits debidamente ordenadas para que todos los ordenadores descifren correctamente la información que comparten. Quizás, hoy en día, uno de los más importantes es el protocolo TCP/IP.  

¿Y cómo se encuentran los ordenadores entre sí para comunicarse?

Todos los ordenadores tienen su propia dirección, conocida como la dirección IP, que no es mas que una secuencia de 32 bits que sirve para identificar y encontrar a las computadoras (bien sea un servidor o un
ordenador cliente) dentro de una misma red. En una misma red ninguna IP se repite.

Dado que nos estamos quedando sin direcciones ip disponibles por el alto numero de dispositivos que están conectados a Internet actualmente se está pasando a una nueva versión para asignar IP-s compuesta por más bits (la versión 6).

Pongamos un ejemplo: Desde vuestro ordenador escribís en el navegador https://theegg.ai y...
¿qué pasa cuando pulsáis la tecla ENTER?

1.- Vuestro ordenador tiene una IP privada (por ejemplo, 192.168.0.55) para vuestra red de casa y envía la petición al router de casa (192.168.0.1).  
2.- El router con IP privada (192.168.0.1) captura la petición de la IP: 192.168.0.55 y se pone en contacto con un servidor DNS (en Internet) para saber a qué IP corresponde la dirección https://theegg.ai que ha tecleado el usuario. Esta vez el router se pone en contacto con este servidor de DNS con su IP pública (la IP que utiliza para conectarse de puertas para afuera). Entended que el router es el puente de comunicación entre 2 redes, por lo que tendrá 2 IP-s. Una para la red interna (privada) y otra para la externa (pública).    
3.- El servidor de DNS busca en sus tablas internas y encuentra la dirección IP que corresponde a https://theegg.ai . Se hace la petición a la dirección IP identificada que corresponde al servidor web donde está alojado "el huevo".  
4.- Este responde enviando la información requerida a la IP pública del router de tu casa.  
5.- Finalmente el router te enviará la información. Lo enviará a la IP privada de su red, a esa IP que le había hecho la petición. A tu ordenador.  

Lecturas obligadas

1.- ¿Cómo funciona Internet? Fuente: Djangogirls  
2.- PDF adjunto sobre redes. Fuente: portaleso

Nota: Debes saber que la IP no es la única dirección mágica que existe. Hay otra que se conoce como dirección MAC y es la matrícula de tu computadora, única en el Mundo. Este registro también juega su papel en todo este tinglado.


### HASHTAGS (etiquetas de ayuda para búsqueda de información relevante)

##### #redes-informáticas #dirección-IP   #protocolo-TCP-IP   #máscara-de-subred   #dirección-MAC #router #puerta-de-enlace #IP-pública #IP-privada #servidor-de-DNS #red-LAN #red-WAN

LINKS DE INTERÉS

https://www.youtube.com/watch?v=4FHWE6QOgQE   
https://openwebinars.net/blog/que-es-tcpip/   
https://tutorial.djangogirls.org/es/how_the_internet_works/   
http://www.portaleso.com/Redes/Ud_4_redes_V1_c.pdf  
https://www.youtube.com/watch?v=liudX0oskwM  
https://es.wikipedia.org/wiki/Fibra_Ã³ptica  
https://es.wikipedia.org/wiki/LÃ­nea_de_abonado_digital_asimÃ©trica  
https://concepto.de/protocolo-informatico/  
https://openwebinars.net/blog/que-es-tcpip/
https://www.ionos.es/digitalguide/fileadmin/DigitalGuide/Screenshots_2019/ip-adresse-EN-1.png
https://tutorial.djangogirls.org/es/how_the_internet_works/
http://www.portaleso.com/Redes/Ud_4_redes_V1_c.pdf  
https://www.xataka.com/basics/que-es-la-direccion-mac-de-tu-ordenador-del-movil-o-de-cualquier-dispositivo  


DICCIONARIO

dirección-IP | Internet | red-WAN | red-LAN | máscara-de-subred | router | switch | TCP-IP | IP-pública | IP- privada

PUNTUACIÓN

Programación: 1  
Redes: 6
