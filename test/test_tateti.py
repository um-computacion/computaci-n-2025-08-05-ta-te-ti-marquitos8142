import unittest
from tablero import tablero, PosOcupadaException
from jugador import Jugador
from tateti import tateti

class test_tablero(unittest.TestCase):
    def test_poner_ficha_en_posicion_libre(self):
        t = tablero()
        t.poner_la_ficha(0, 0, "x")
        self.assertEqual(t.contenedor[0][0], "x")

    def test_no_permitir_posicion_ocupada(self):
        t = tablero()
        t.poner_la_ficha(0, 0, "x")
        with self.assertRaises(PosOcupadaException):
            t.poner_la_ficha(0, 0, "o")

    def test_hay_ganador_en_fila(self):
        t = tablero()
        t.poner_la_ficha(0, 0, "x")
        t.poner_la_ficha(0, 1, "x")
        t.poner_la_ficha(0, 2, "x")
        self.assertTrue(t.hay_ganador())

    def test_hay_ganador_en_columna(self):
        t = tablero()
        t.poner_la_ficha(0, 1, "o")
        t.poner_la_ficha(1, 1, "o")
        t.poner_la_ficha(2, 1, "o")
        self.assertTrue(t.hay_ganador())

    def test_hay_ganador_en_diagonal(self):
        t = tablero()
        t.poner_la_ficha(0, 0, "x")
        t.poner_la_ficha(1, 1, "x")
        t.poner_la_ficha(2, 2, "x")
        self.assertTrue(t.hay_ganador())

    def test_tablero_lleno(self):
        t = tablero()
        fichas = ["x", "o"]
        f = 0
        for i in range(3):
            for j in range(3):
                t.poner_la_ficha(i, j, fichas[f])
                f = 1 - f
        self.assertTrue(t.esta_lleno())

class test_tateti(unittest.TestCase):
    def test_cambiar_turno(self):
        j1 = Jugador("ana", "x")
        j2 = Jugador("juan", "o")
        juego = tateti(j1, j2)
        juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(juego.turno, j2)

    def test_ganar_con_tateti(self):
        j1 = Jugador("ana", "x")
        j2 = Jugador("juan", "o")
        juego = tateti(j1, j2)
        juego.ocupar_una_de_las_casillas(0, 0)
        juego.ocupar_una_de_las_casillas(1, 0)
        juego.ocupar_una_de_las_casillas(0, 1)
        juego.ocupar_una_de_las_casillas(1, 1)
        gano = juego.ocupar_una_de_las_casillas(0, 2)
        self.assertTrue(gano)

if __name__ == "__main__":
    unittest.main()
