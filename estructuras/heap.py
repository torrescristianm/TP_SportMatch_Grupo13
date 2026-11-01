class HeapMaximos:
    """Heap binaria de maximos guardada en una lista.

    Cada elemento se guarda como (prioridad, desempate, valor). La raiz es
    el elemento de mayor prioridad; ante igual prioridad gana el de menor
    desempate, para que los resultados siempre salgan en el mismo orden.
    """

    def __init__(self):
        self.elementos = []

    def __len__(self):
        return len(self.elementos)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def _tiene_mas_prioridad(self, i, j):
        prioridad_i, desempate_i, _ = self.elementos[i]
        prioridad_j, desempate_j, _ = self.elementos[j]

        if prioridad_i != prioridad_j:
            return prioridad_i > prioridad_j

        return desempate_i < desempate_j

    def _intercambiar(self, i, j):
        self.elementos[i], self.elementos[j] = self.elementos[j], self.elementos[i]

    def _subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2

            if not self._tiene_mas_prioridad(indice, padre):
                break

            self._intercambiar(indice, padre)
            indice = padre

    def _bajar(self, indice):
        cantidad = len(self.elementos)

        while True:
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            mayor = indice

            if izquierdo < cantidad and self._tiene_mas_prioridad(izquierdo, mayor):
                mayor = izquierdo

            if derecho < cantidad and self._tiene_mas_prioridad(derecho, mayor):
                mayor = derecho

            if mayor == indice:
                break

            self._intercambiar(indice, mayor)
            indice = mayor

    def insertar(self, prioridad, desempate, valor):
        self.elementos.append((prioridad, desempate, valor))
        self._subir(len(self.elementos) - 1)

    def ver_maximo(self):
        if self.esta_vacia():
            return None

        return self.elementos[0][2]

    def extraer_maximo(self):
        if self.esta_vacia():
            return None

        maximo = self.elementos[0]
        ultimo = self.elementos.pop()

        if self.elementos:
            self.elementos[0] = ultimo
            self._bajar(0)

        return maximo[2]

    @classmethod
    def desde_lista(cls, items):
        """Arma la heap en O(n) con items = [(prioridad, desempate, valor), ...]."""
        heap = cls()
        heap.elementos = list(items)

        for indice in range(len(heap.elementos) // 2 - 1, -1, -1):
            heap._bajar(indice)

        return heap

    def top_n(self, n):
        """Devuelve los n de mayor prioridad sin modificar la heap."""
        copia = HeapMaximos()
        copia.elementos = list(self.elementos)
        resultado = []

        while len(resultado) < n and not copia.esta_vacia():
            resultado.append(copia.extraer_maximo())

        return resultado
