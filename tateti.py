from tablero import tablero

class tateti:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = jugador1
        self.tablero = tablero()

    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.turno.ficha)
        if self.tablero.hay_ganador():
            print("gana", self.turno.nombre)
            return True
        self.turno = self.jugador2 if self.turno == self.jugador1 else self.jugador1
        return False
