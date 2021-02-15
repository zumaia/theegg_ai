import random

"""
Un entero se dice que es un palíndromo si es igual al número que se obtiene al invertir el orden de sus cifras. 
Por ejemplo, 79197 y 324423 son palíndromos. En esta tarea se le dará un entero N, 1 <= N <= 1.000.000. 
Usted debe encontrar el menor entero M tal que M <= N que es primo y M es un palíndromo N.

Por ejemplo, si N es 31, entonces la respuesta es 101.

Formato de entrada:
Un solo entero N, (1 <= N <= 1.000.000), en una sola línea.

Formato de salida:
Su salida debe consistir en un solo número entero, el más pequeño palíndromo primo mayor que o igual a N.
"""
numero = random.randint(1, 1000000)
# Imprimio en número aleatorio
print("El número aleatorio es {}".format(numero))

# Palindrome test
def palindrome(num):
    """
    Función que testea de palindronomo
    """
    return str(num) == str(num)[::-1]


# Prime Test
def is_prime(n):
    """
    Función que testea si el número es primo
    """
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


# Indicamos los rangos
N = numero  # Número mínimo
M = 1000000  # Número máximo


def ejercicio():
    """
    función para obtener el primer número palindromo primo desde el número aleatorio obtenido y 1.000.000
    """
    num_palind = [0]
    for x in range(N, M):

        # Check for palindrome and prime number
        if palindrome(x) and is_prime(x):

            # Omitting 2,3,5,7 as per request
            if (
                abs(x) % 2 != 0
                and abs(x) % 3 != 0
                and abs(x) % 5 != 0
                and abs(x) % 7 != 0
            ):
                num_palind.append(x)

    if not num_palind[0]:
        print("No hay número palindromo mayor a {}".format(N))
    else:
        print(
            "El más pequeño palíndromo primo mayor que o igual a {}: {}".format(
                N, num_palind[0]
            )
        )


ejercicio()
