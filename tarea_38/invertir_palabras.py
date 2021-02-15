archivo = "texto_entrada.txt"


def inver_palabras(archivo):
    """
    Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso.
    Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio entre cada pareja de palabras. La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco y de la frase invertida.
    """
    # Genero una lista vacia
    lista_texto = []
    with open(archivo, "r") as texto:
        lista_texto = texto.readlines()
    # Genero un bucle para poder
    for i, line in enumerate(lista_texto[1:], 1):
        ## por cada elemento de la lista divido la cadena en el espacio
        words = line.split()
        ## invertir las palabras utilizando la función reversed()
        words = list(reversed(words))
        ## junto las palabras y las imprimo
        line = " ".join(words)
        print("Case #{}: {}".format(i, line))


inver_palabras(archivo)
