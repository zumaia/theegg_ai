class Pokemon:
    def __init__(self, nombre, puntos_vida, puntos_ataque):
        """
        Creamos el objeto: nombre, puntos de vida y puntos de ataque
        """
        self.nombre = nombre
        self.puntos_vida = puntos_vida
        self.puntos_ataque = puntos_ataque

    def sufre_ataque(self, danos):
        """
        vemos los ataque
        """
        self.puntos_vida = self.puntos_vida - danos

    def esta_vivo(self):
        """
        Conprovar vida
        """
        # Si es mayor a 0 está vivo
        if self.puntos_vida > 0:
            return True
        # En caso contrario, no lo eá
        else:
            return False


def anunciar_ganador(ganador):
    """
    Función que anuncia el ganador
    """
    print("Gana: {}!".format(ganador.nombre))


def lucha(pok1, pok2):
    """
    Funciónn de lucha
    """
    pok1_turno = True
    # Inicializamos ronda
    ronda = 0

    while pok1.esta_vivo() and pok2.esta_vivo():
        # vamos incrementando las rondas desde la primera
        ronda = ronda + 1

        if pok1_turno:
            pok2.sufre_ataque(pok1.puntos_ataque)

        else:
            pok1.sufre_ataque(pok2.puntos_ataque)

        pok1_turno = not pok1_turno

    if pok1.esta_vivo():
        anunciar_ganador(pok1)
    else:
        anunciar_ganador(pok2)

# Introducimos los datos necesarios de los personajes
print("Inserta los puntos de vida de Pikachu")
pikachu_puntos_vida = int(input())
print("Inserta los puntos de ataque de Pikachu")
pikachu_puntos_ataque = int(input())
print("Inserta los puntos de vida de jigglipuff")
jigglipuff_puntos_vida = int(input())
print("Inserta los puntos de ataque de jigglipuff")
jigglipuff_puntos_ataque = int(input())
# Aplicamos los datos introducidos al objeto indicado en un inicio
pikachu = Pokemon("Pikachu", pikachu_puntos_vida, pikachu_puntos_ataque)
jigglipuff = Pokemon("Jigglipuff", jigglipuff_puntos_vida, jigglipuff_puntos_ataque)
# A luchar
lucha(pikachu, jigglipuff)
