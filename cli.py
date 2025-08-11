from tateti import tateti
from jugador import Jugador
from tablero import PosOcupadaException

def main():
    print("bienvenidos al tateti")
    nombre1 = input("nombre del jugador 1 (x): ")
    nombre2 = input("nombre del jugador 2 (o): ")
    j1 = Jugador(nombre1, "x")
    j2 = Jugador(nombre2, "o")
    juego = tateti(j1, j2)

    while True:
        print("tablero:")
        for fila in juego.tablero.contenedor:
            print(fila)
        print("turno de", juego.turno.nombre)
        try:
            fil = int(input("ingrese fila (1-3): ")) - 1
            col = int(input("ingrese columna (1-3): ")) - 1
            if fil not in [0, 1, 2] or col not in [0, 1, 2]:
                print("entrada invalida")
                continue
            if juego.ocupar_una_de_las_casillas(fil, col):
                for fila in juego.tablero.contenedor:
                    print(fila)
                print("fin del juego, gano", juego.turno.nombre)
                break
            if juego.tablero.esta_lleno():
                print("empate")
                break
        except ValueError:
            print("entrada invalida")
        except PosOcupadaException as e:
            print(e)

if __name__ == "__main__":
    main()
