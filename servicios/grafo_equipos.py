import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from estructuras.grafo import Grafo

PENALIDAD_OTRA_LIGA = 15
PENALIDAD_OTRO_ESTILO = 10


def distancia(a, b):
    """Que tan distintos son dos equipos: 0 significa identicos."""
    costo = abs(a.popularidad - b.popularidad) + abs(a.titulos - b.titulos)

    if a.liga != b.liga:
        costo = costo + PENALIDAD_OTRA_LIGA

    if a.estilo != b.estilo:
        costo = costo + PENALIDAD_OTRO_ESTILO

    return costo


def construir_grafo(equipos, vecinos_por_equipo=5):
    """Conecta cada equipo con los equipos mas parecidos (menor distancia).

    Se limita a `vecinos_por_equipo` conexiones propuestas por equipo para que el
    grafo quede ralo; como las aristas no tienen direccion, un equipo puede
    terminar con mas vecinos de los que el propuso.
    """
    grafo = Grafo()

    for equipo in equipos:
        grafo.agregar_vertice(equipo.nombre, equipo)

    for equipo in equipos:
        candidatos = []

        for otro in equipos:
            if otro is not equipo:
                candidatos.append((distancia(equipo, otro), otro.nombre))

        candidatos.sort()

        for peso, nombre_otro in candidatos[:vecinos_por_equipo]:
            grafo.agregar_arista(equipo.nombre, nombre_otro, peso)

    return grafo
