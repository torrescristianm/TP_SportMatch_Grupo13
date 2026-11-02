import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from estructuras.grafo import Grafo
from modelos.equipo import Equipo
from servicios.grafo_equipos import construir_grafo, distancia


class TestGrafo(unittest.TestCase):
    def test_agrega_vertices_y_aristas(self):
        grafo = Grafo()
        grafo.agregar_vertice("A")
        grafo.agregar_vertice("B")

        self.assertTrue(grafo.agregar_arista("A", "B", 3))

        self.assertEqual(grafo.cantidad_vertices(), 2)
        self.assertEqual(grafo.cantidad_aristas, 1)

    def test_la_arista_es_en_los_dos_sentidos(self):
        grafo = Grafo()
        grafo.agregar_vertice("A")
        grafo.agregar_vertice("B")
        grafo.agregar_arista("A", "B", 3)

        self.assertEqual(grafo.vecinos("A"), [("B", 3)])
        self.assertEqual(grafo.vecinos("B"), [("A", 3)])

    def test_no_repite_aristas_ni_crea_bucles(self):
        grafo = Grafo()
        grafo.agregar_vertice("A")
        grafo.agregar_vertice("B")
        grafo.agregar_arista("A", "B", 3)

        self.assertFalse(grafo.agregar_arista("B", "A", 3))
        self.assertFalse(grafo.agregar_arista("A", "A", 0))
        self.assertEqual(grafo.cantidad_aristas, 1)

    def test_arista_con_vertice_inexistente_falla(self):
        grafo = Grafo()
        grafo.agregar_vertice("A")

        with self.assertRaises(KeyError):
            grafo.agregar_arista("A", "B", 1)

    def test_vecinos_de_vertice_inexistente(self):
        self.assertEqual(Grafo().vecinos("X"), [])
        self.assertEqual(Grafo().grado("X"), 0)


class TestGrafoEquipos(unittest.TestCase):
    def crear_equipo(self, nombre, liga, popularidad, titulos, estilo):
        return Equipo(nombre, "Argentina", liga, 1900, popularidad, titulos, estilo)

    def test_distancia_de_equipos_identicos_es_cero(self):
        a = self.crear_equipo("A", "Liga 1", 80, 10, "ofensivo")
        b = self.crear_equipo("B", "Liga 1", 80, 10, "ofensivo")

        self.assertEqual(distancia(a, b), 0)

    def test_distancia_suma_diferencias_y_penalidades(self):
        a = self.crear_equipo("A", "Liga 1", 80, 10, "ofensivo")
        b = self.crear_equipo("B", "Liga 2", 70, 7, "tecnico")

        self.assertEqual(distancia(a, b), 10 + 3 + 15 + 10)

    def test_conecta_con_el_mas_parecido(self):
        a = self.crear_equipo("A", "Liga 1", 80, 10, "ofensivo")
        parecido = self.crear_equipo("Parecido", "Liga 1", 79, 10, "ofensivo")
        lejano = self.crear_equipo("Lejano", "Liga 2", 40, 0, "tecnico")

        grafo = construir_grafo([a, parecido, lejano], vecinos_por_equipo=1)

        self.assertTrue(grafo.tiene_arista("A", "Parecido"))
        self.assertTrue(grafo.tiene_arista("Parecido", "A"))

    def test_un_vertice_por_equipo(self):
        equipos = [
            self.crear_equipo(str(i), "Liga 1", 50 + i, i, "ofensivo") for i in range(10)
        ]

        grafo = construir_grafo(equipos, vecinos_por_equipo=3)

        self.assertEqual(grafo.cantidad_vertices(), 10)
        for equipo in equipos:
            self.assertGreaterEqual(grafo.grado(equipo.nombre), 3)


if __name__ == "__main__":
    unittest.main()
