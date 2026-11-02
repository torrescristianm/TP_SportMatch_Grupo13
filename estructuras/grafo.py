class Grafo:
    """Grafo no dirigido y pesado con lista de adyacencia.

    Cada vertice guarda su valor y la lista de sus vecinos como
    (vecino, peso). Como el grafo no es dirigido, cada arista se
    guarda en las listas de sus dos extremos.
    """

    def __init__(self):
        self.valores = {}
        self.adyacentes = {}
        self.cantidad_aristas = 0

    def agregar_vertice(self, vertice, valor=None):
        if vertice not in self.adyacentes:
            self.adyacentes[vertice] = []

        self.valores[vertice] = valor

    def tiene_vertice(self, vertice):
        return vertice in self.adyacentes

    def tiene_arista(self, a, b):
        if a not in self.adyacentes:
            return False

        for vecino, _ in self.adyacentes[a]:
            if vecino == b:
                return True

        return False

    def agregar_arista(self, a, b, peso):
        if a not in self.adyacentes or b not in self.adyacentes:
            raise KeyError("Los dos vertices deben existir antes de conectarlos")

        if a == b or self.tiene_arista(a, b):
            return False

        self.adyacentes[a].append((b, peso))
        self.adyacentes[b].append((a, peso))
        self.cantidad_aristas = self.cantidad_aristas + 1

        return True

    def vecinos(self, vertice):
        return list(self.adyacentes.get(vertice, []))

    def grado(self, vertice):
        return len(self.adyacentes.get(vertice, []))

    def obtener_valor(self, vertice):
        return self.valores.get(vertice)

    def cantidad_vertices(self):
        return len(self.adyacentes)
