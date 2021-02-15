"""
Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN, y el
objetivo es encontrar el conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.

Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C),
guanina (G) y timina (T):

ATGTCTTCCTCGA TGCTTCCTATGAC

Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto ordenado de bases adyacentes de mayor tamaño
que se encuentra en ambas formas de vida.
"""


def localizador(string1, string2):
    """
    Función donde obtenemos el mayor subconjunto ordenado en ambos strings
    """
    respuesta = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if i + j < len1 and string1[i + j] == string2[j]:
                match += string2[j]
            else:
                if len(match) > len(respuesta):
                    respuesta = match
                match = ""
    print(
        "El mayor subconjunto ordenado en {} y {} es {}".format(
            string1, string1, respuesta
        )
    )


(a, b) = ("ctgactga", "actgagc")

localizador(a, b)
