import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from estructuras.arbol_binario_busqueda import ArbolBinarioBusqueda
from modelos.equipo import Equipo


class TestArbolBinarioBusqueda(unittest.TestCase):
    def crear_equipo(self, nombre):
        return Equipo(nombre, "Argentina", "Liga de prueba", 1900, 50, 0, "prueba")

    def test_busca_un_equipo_insertado(self):
        arbol = ArbolBinarioBusqueda()
        boca = self.crear_equipo("Boca Juniors")

        arbol.insertar(boca.nombre, boca)
        resultado, pasos = arbol.buscar("Boca Juniors")

        self.assertEqual(resultado, boca)
        self.assertEqual(pasos, 1)

    def test_devuelve_none_si_no_encuentra_el_equipo(self):
        arbol = ArbolBinarioBusqueda()
        arbol.insertar("River Plate", self.crear_equipo("River Plate"))

        resultado, pasos = arbol.buscar("Racing Club")

        self.assertIsNone(resultado)
        self.assertEqual(pasos, 1)

    def test_recorrido_inorden_devuelve_equipos_ordenados(self):
        arbol = ArbolBinarioBusqueda()

        for nombre in ["River Plate", "Boca Juniors", "Independiente"]:
            equipo = self.crear_equipo(nombre)
            arbol.insertar(equipo.nombre, equipo)

        nombres = [equipo.nombre for equipo in arbol.inorden()]

        self.assertEqual(nombres, ["Boca Juniors", "Independiente", "River Plate"])


if __name__ == "__main__":
    unittest.main()
