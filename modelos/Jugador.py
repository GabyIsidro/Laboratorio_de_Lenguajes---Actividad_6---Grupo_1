class Jugador (object):
    #creador de un objeto tipo jugador
    def __init__(self,numeroCamiseta, apellido, posicion, minutosJugados = 0): #asigno al 0 como valor default de minutosJugados
        self.numeroCamiseta = numeroCamiseta
        self.apellido = apellido
        self.posicion = posicion
        self.minutosJugados = minutosJugados

    #muestro todos los datos del jugador en un print simple
    def mostrarDatos(self):
        print("jugador = '{self.apellido}'\n numero = '{self.numeroCamiseta}' \n posición = '{self.posicion}' \n minutos jugaods = '{sel.minutosJugados}'")

    #permite que se puedan editar los minutos jugados de un jugador
    def setMinutosJugados(self, minutosJugados):
        self.minutosJugados = minutosJugados
        
    #muestra los minutos jugados de un jugador
    def getMinutosJugados(self):
         print("el jugador '{self.apellido}' jugó '{sel.minutosJugados}' minutos.")