#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  decimal_a_binary.py

"""
Básicamente crear un programa que divida un número por 2 hasta llegar a 0 y luego agrega a una lista en ese orden,
una vez que la lista está terminada, da la vuelta a la lista hacia atrás para mostrar el número binario correcto.
"""

# ==Global Variables==#
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


def decimal_to_binary_convert(numero):
    """
    Función destinada a convertir el número decimal en binario
    """
    # Creo una lista vacia
    binary_list = []
    # Para tener como referencia
    old_number = numero
    # Configuramos nuestro bucle para terminar una conversión completa.
    while numero > 0.5:
        # If a number/2 = a number and 1/2
        if numero % 2 != 0:
            binary_list.append(1)
        else:
            # Si un numero es entero
            binary_list.append(0)  # If a number is a whole number.
        # divido el número inicial por 2
        numero /= 2
        # Deshágase del 0,5 si hay uno.
        numero = int(numero)
        # Si quiero ver como trabaja, puedo habilitar la siguiente opciónl
        # print(binary_list)
        print()
    print("La forma Binaria " + str(old_number) + " es: ")
    # Imprime la lista binaria del revés para mostrarla correctamente.
    print(binary_list[::-1])


def main():
    """
    Función destinada a ejecutar lo anterior
    """
    print("Convertidor Decimal a Binario!")
    switch = 0
    while switch == 0:
        numero = int(input("Por favor, inserta un número decimal para convertir: "))
        # Llamo a la función generada
        decimal_to_binary_convert(numero)
        print()
        question = 1
        while question == 1:
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
    print("Ultima actualización: " + last_updated)


# Ejecuto la función principal
main()
