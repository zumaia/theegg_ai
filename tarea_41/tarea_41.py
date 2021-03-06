# Importamos las librerias
from bs4 import BeautifulSoup
import requests
import re
from collections import Counter

# Solicitamos la url
print("Inserta una url: por ej:(http://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/)")
url = input()

# LLamamos la url para obtenerlos datos
# url = 'http://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/'
r = requests.get(url)
# Debemos recibir código 200 de OK
print('Resultado Ok=200: {}'.format(r) + "\n")
r.status_code

# Parseamos la url
s = BeautifulSoup(r.content, "html.parser") 

# Obtenemos el texto del apartado especifico
texto = []
for text in s.find_all('div',{'class':'post-content description cf'}):
    b = text
    texto.append(b)
    
# Utilizamos el regex para eliminar los valores que no nos sirven
lista_palab = re.sub(r"<.+?>", "", str(texto))

# Eliminamos los saltos de línea
mytext = "".join(lista_palab.split("\n"))

# Seleccionamos el parrafo correspondiente
mytext= re.findall("congelación(.*?)Si tienes", mytext)

# Modificamos a minusculas
text_low = [item.lower() for item in mytext]

# Convertimos la lista de string en string
def converttostr(input_seq, seperator):
    """
    Desc:
    Function to convert List of strings to a string with a separator
    """
   # Join all the strings in list
    final_str = seperator.join(input_seq)
    return final_str

seperator = ' '
text_low = converttostr(text_low, seperator)

# Eliminamos puntos y comas
text_low = text_low.replace(",", "")
text_low = text_low.replace(".", "")
text_low = text_low.replace("…", "")

# Generamos 2 str
word_count = 0
char_count = 0
# Dividimos los str
split_string = text_low.split()

# contamos las palabras
word_count = len(split_string)

# contamos los carácteres
for word in split_string:
    char_count += len(word)

# Mostramos
print("Total words : {}".format(word_count))
print("Total characters : {}".format(char_count))


# Agrupamos y contamos
counts = Counter(split_string)
comunes = counts.most_common(10)
print("\nLas 10 mas comunes : \n {} \n".format(comunes))


print("\nTotal characters : \n {} \n".format(counts) +"\n")
