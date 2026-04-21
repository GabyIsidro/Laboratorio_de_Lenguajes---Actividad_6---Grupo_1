from modelos.jugador import Jugador

class Arquero(Jugador):
    # creador de un objeto tipo arquero
    def __init__(self, numeroCamiseta, apellido, minutosJugados=0):
        # llamo al constructor de Jugador (Arquero)
        super().__init__(numeroCamiseta, apellido, "Arquero", minutosJugados)

    # sobrescribo el método mostrarDatos para indicar que es un arquero
    def mostrarDatos(self):
        print(f"ARQUERO = '{self.apellido}'\n"
              f" número = '{self.numeroCamiseta}' \n"
              f" posición = '{self.posicion}' \n"
              f" minutos jugados = '{self.minutosJugados}'")
