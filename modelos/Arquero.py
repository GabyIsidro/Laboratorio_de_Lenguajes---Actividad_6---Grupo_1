from modelos.Jugador import Jugador

class Arquero(Jugador):
    # creador de un objeto tipo arquero
    def __init__(self, numeroCamiseta, apellido, minutosJugados=0):
        # llamo al constructor de Jugador (Arquero)
        super().__init__(numeroCamiseta, apellido, "Arquero", minutosJugados)

    # sobrescribo el método mostrarDatos para indicar que es un arquero
    def mostrarDatos(self):
        return (f"ARQUERO = '{self.apellido}'\n"
                f" Número = '{self.numeroCamiseta}' \n"
                f" Posición = '{self.posicion}' \n"
                f" Minutos jugados = '{self.minutosJugados}'")
