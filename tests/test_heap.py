import random
import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from estructuras.heap import HeapMaximos
from modelos.equipo import Equipo


class TestHeapMaximos(unittest.TestCase):
    def crear_equipo(self, nombre, popularidad, titulos):
        return Equipo(nombre, "Argentina", "Liga de prueba", 1900, popularidad, titulos, "prueba")

    def test_heap_vacia(self):
        heap = HeapMaximos()

        self.assertTrue(heap.esta_vacia())
        self.assertIsNone(heap.ver_maximo())
        self.assertIsNone(heap.extraer_maximo())

    def test_extrae_en_orden_de_prioridad(self):
        heap = HeapMaximos()

        for prioridad in [5, 1, 9, 3, 7]:
            heap.insertar(prioridad, str(prioridad), prioridad)

        extraidos = [heap.extraer_maximo() for _ in range(5)]

        self.assertEqual(extraidos, [9, 7, 5, 3, 1])

    def test_desempata_por_nombre(self):
        heap = HeapMaximos()
        heap.insertar(10, "river", "River")
        heap.insertar(10, "boca", "Boca")

        self.assertEqual(heap.extraer_maximo(), "Boca")

    def test_top_n_no_modifica_la_heap(self):
        heap = HeapMaximos.desde_lista([(p, str(p), p) for p in [4, 8, 2, 6]])

        self.assertEqual(heap.top_n(2), [8, 6])
        self.assertEqual(len(heap), 4)

    def test_top_n_mayor_a_la_cantidad(self):
        heap = HeapMaximos.desde_lista([(1, "a", "a"), (2, "b", "b")])

        self.assertEqual(heap.top_n(10), ["b", "a"])

    def test_desde_lista_coincide_con_sorted(self):
        random.seed(1)
        valores = [random.randint(0, 100) for _ in range(200)]
        heap = HeapMaximos.desde_lista([(v, str(i), v) for i, v in enumerate(valores)])

        extraidos = [heap.extraer_maximo() for _ in range(len(valores))]

        self.assertEqual(extraidos, sorted(valores, reverse=True))

    def test_prioridad_de_equipo(self):
        equipo = self.crear_equipo("Boca Juniors", 90, 10)

        self.assertEqual(equipo.prioridad(), 110)


if __name__ == "__main__":
    unittest.main()
