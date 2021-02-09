# Construye un simulador

### Para ejecutar:
# $python decimal_a_binary.py

Cabe de decir que TODO es analógico en este Mundo, hasta los ordenadores "digitales" aunque parezca contradictorio ;-)

Los ordenadores no son mas que circuitos eléctricos que funcionan con intensidades y diferencias de tensión. La única diferencia es que están pensados para trabajar en 2 estados:

1.- Intensidad SÍ en código binario es un 1 2.- Intensidad NO en código binario es un 0

El 0 y el 1 sólo existen en nuestras cabezas, realmente lo que hay detrás son transistores abiertos y cerrados. Sí, el transistor es la clave de la revolución digital y no nos referimos a la radio.
Nota para la juventud: a la radio se le llamaba transistor.

Imaginad el transistor como una compuerta que se abre y se cierra muy rápidamente, sin estados intermedios. A esta apertura y cierre se la conoce como conmutación y es uno de los modos más habituales de trabajo de estos componentes. Pues bien, esta rapidísima conmutación es la responsable de generar corriente o no, de generar bits con valor 1 o 0.

Ahora imagínate millones de transistores trabajando en paralelo. Eso significa millones de bits por segundo. Si un bit es la unidad de información más pequeña millones de bits puede ser muchísima información que se gestiona velozmente.

Caso de uso: La gestión del color de un píxel. Un píxel no es mas que una pequeña "bombillita" (se conoce como led) que tienes en el monitor de tu ordenador. Muchas "bombillitas" puestas matricialmente dibujan lo que ves en cada momento en el ordenador. Como sabréis todo color tiene 3 colores fundamentales (rojo, verde, azul) y la mezcla de estos tres es el color resultante. Los ordenadores utilizan 8 bits por cada color, desde el 00000000 hasta el 11111111. Esto traducido a números decimales es desde 0 hasta el 255, donde el 0 es ausencia de color (negro) y el 255 (blanco). Para un led en escala de grises con 8 bits (8 transistores) podríamos gestionar la intensidad de luz. En el caso de leds de colores necesitaremos 8x3 (RGB) = 24 bits. De este modo, con 24 bits podríamos gestionar el color de un led. 24 transistores para un led???

Pues sí, actualmente los ordenadores tienen miles de millones de transistores... y creciendo.

Lo cierto, aunque parezca mentira, es que este nuevo idioma (el binario) facilita mucho el cálculo y el diseño de circuitos electrónicos más baratos y con muchas más prestaciones si los comparamos con los circuitos analógicos "puros y clásicos". Estas nuevas reglas diseñadas para construir circuitos digitales se conocen como la algebra boole.

Vayamos al grano:
En este caso hay que desarrollar un programa donde una vez enviado un valor decimal a una función este lo convierta a binario y nos lo devuelva. Se trata de construir un simulador de un convertidor analógico digital mediante un programa (software). El hardware lo dejamos para otro día.

#HASHTAGS (etiquetas de ayuda para búsqueda de información relevante)

#convertidor-analógico-digital #sistema-binario #algebra-booleana

LINKS DE INTERÉS

https://www.youtube.com/watch?v=9_rpiAScBvk https://www.calculadoraconversor.com/decimal-a-binario-online/ https://www.youtube.com/watch?v=dIV5l9cx_ck https://www.youtube.com/watch?v=9_rpiAScBvk https://soundgirls.org/entendiendo-los-convertidores-ad-da/

DICCIONARIO

convertidor-analógico-digital | transistores-bipolares | frecuencia-de-muestreo | sistema-binario | algebra- booleana

PUNTUACIÓN

Programación: 3
Redes: 1
Seguridad: 0
Algoritmia: 3


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  decimal_a_binary.py

'''
Básicamente crear un programa que divida un número por 2 hasta llegar a 0 y luego agrega a una lista en ese orden,
una vez que la lista está terminada, da la vuelta a la lista hacia atrás para mostrar el número binario correcto.
'''

#==Global Variables==#
version = "0.0.1"
dev_team = ["Oscar Rojo"]
last_updated = "10 de febrero de 2021"


def mode_menu():
	"""
	Función que define el inicio
	"""
	print("#===========================================#")
	print("#   Convertidor Decimal a Binario           #")
	print("#===========================================#")

# Ejecuto la presentación
mode_menu()
```

    #===========================================#
    #   Convertidor Decimal a Binario           #
    #===========================================#



```python
def decimal_to_binary_convert(numero):
	"""
	Función destinada a convertir el número decimal en binario
	"""
	# Creo una lista vacia
	binary_list = []
	# Para tener como referencia
	old_number = numero
	# Configuramos nuestro bucle para terminar una conversión completa.
	while (numero > .5):
		# If a number/2 = a number and 1/2
		if numero % 2 != 0:
			binary_list.append(1)
		else:
			# Si un numero es entero
			binary_list.append(0) # If a number is a whole number.
		# divido el número inicial por 2
		numero /= 2
		# Deshágase del 0,5 si hay uno.
		numero = int(numero)
		# Si quiero ver como trabaja, puedo habilitar la siguiente opciónl
		# print(binary_list)
		print()
	print("La valor Binaria de " + str(old_number) + " es: ")
	# Imprime la lista binaria del revés para mostrarla correctamente.
	print(binary_list[::-1])

def main():
	"""
	Función destinada a ejecutar lo anterior
	"""
	print("Convertidor Decimal a Binario!")
	switch = 0
	while (switch == 0):
		numero = int(input("Por favor, inserta un número decimal para convertir: "))
		# Llamo a la función generada
		decimal_to_binary_convert(numero)
		print()
		question = 1
		while(question == 1):
			user_response = input("Has terminado? Si o No: ").lower()
			print()
			if user_response == "si":
				switch = 1
				question = 0
			elif user_response == "no":
				switch = 0
				question = 0
			else:
				print("Respuesta incorrecta, intenta otra vez")
				question = 1
	print("Gracias por utilizar el programa")
	print("version: " + str(version))
	print("Ultima actualización: " + last_updated )
```


```python
# Ejecuto la función principal
main()
```

    Convertidor Decimal a Binario!


    Por favor, inserta un número decimal para convertir:  15


    
    
    
    
    La forma Binaria 15 es: 
    [1, 1, 1, 1]
    


    Has terminado? Si o No:  si


    
    Gracias por utilizar el programa
    version: 0.0.1
    Ultima actualización: 10 de febrero de 2021

