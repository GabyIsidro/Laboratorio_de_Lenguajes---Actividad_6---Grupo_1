from modelos.Jugador import Jugador

class JugadorCampo(Jugador):
  def __init__(self, numeroCamiseta, apellido, posicion, minutosJugados, golesMarcados):
    # Llama al constructor del padre (Jugador).
    super().__init__(numeroCamiseta, apellido, posicion, minutosJugados)
    
    if golesMarcados < 0:
      raise ValueError("El número de goles no puede ser menor a 0.")
      
    self.__golesMarcados = golesMarcados

  def setGolesMarcados(self, goles):
    self.__golesMarcados = goles
      
  def getGolesMarcados(self):
    return self.__golesMarcados
      
  def mostrarDatos(self):
    # Obtenemos la base del padre y le añadimos el atributo de golesMarcados.
    atributos_base = super().mostrarDatos()
    return (f"{atributos_base}\n"
           f"Goles marcados: {self.__golesMarcados}"
           )
