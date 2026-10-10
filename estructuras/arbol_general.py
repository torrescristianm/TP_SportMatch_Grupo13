# Árbol N-ario / General para categorías o jerarquías.

class NodoGeneral:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []


class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def insertar_raiz(self, valor):
        self.raiz = NodoGeneral(valor)
        return self.raiz

    def agregar_hijo(self, nodo_padre, valor):
        nuevo_hijo = NodoGeneral(valor)
        nodo_padre.hijos.append(nuevo_hijo)
        return nuevo_hijo

    def buscar(self, valor_buscado):
        return self._buscar_rec(self.raiz, str(valor_buscado).lower())

    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return None
        if str(nodo.valor).lower() == valor:
            return nodo
        for hijo in nodo.hijos:
            encontrado = self._buscar_rec(hijo, valor)
            if encontrado:
                return encontrado
        return None

    def amplitud(self):
        if not self.raiz:
            return []
        resultado = []
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            resultado.append(actual.valor)
            for hijo in actual.hijos:
                cola.append(hijo)
        return resultado

    def profundidad_preorder(self):
        resultado = []
        self._preorder_rec(self.raiz, resultado)
        return resultado

    def _preorder_rec(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            for hijo in nodo.hijos:
                self._preorder_rec(hijo, resultado)

    def cantidad_nodos(self):
        return self._contar_rec(self.raiz)

    def _contar_rec(self, nodo):
        if not nodo:
            return 0
        total = 1
        for hijo in nodo.hijos:
            total += self._contar_rec(hijo)
        return total