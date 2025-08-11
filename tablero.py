class PosOcupadaException(Exception):
    pass

class tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def poner_la_ficha(self, fil, col, ficha):
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")

    def hay_ganador(self):
        for fila in self.contenedor:
            if fila[0] != "" and fila.count(fila[0]) == 3:
                return True
        for col in range(3):
            if self.contenedor[0][col] != "" and \
               self.contenedor[0][col] == self.contenedor[1][col] == self.contenedor[2][col]:
                return True
        if self.contenedor[0][0] != "" and \
           self.contenedor[0][0] == self.contenedor[1][1] == self.contenedor[2][2]:
            return True
        if self.contenedor[0][2] != "" and \
           self.contenedor[0][2] == self.contenedor[1][1] == self.contenedor[2][0]:
            return True
        return False

    def esta_lleno(self):
        for fila in self.contenedor:
            for celda in fila:
                if celda == "":
                    return False
        return True
