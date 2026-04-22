class Jugador (object):
    #creador de un objeto tipo jugador
    def __init__(self,numeroCamiseta, apellido, posicion, minutosJugados = 0): #asigno al 0 como valor default de minutosJugados
        self.numeroCamiseta = numeroCamiseta
        self.apellido = apellido
        self.posicion = posicion
        self.minutosJugados = minutosJugados

    #muestro todos los datos del jugador
    def mostrarDatos(self):
        return f"Jugador = '{self.apellido}'\n Número = '{self.numeroCamiseta}' \n Posición = '{self.posicion}' \n Minutos jugados = '{self.minutosJugados}'"

    #permite que se puedan editar los minutos jugados de un jugador
    def setMinutosJugados(self, minutosJugados):
        self.minutosJugados = minutosJugados
        
    #muestra los minutos jugados de un jugador
    def getMinutosJugados(self):
         return f"el jugador '{self.apellido}' jugó '{self.minutosJugados}' minutos."