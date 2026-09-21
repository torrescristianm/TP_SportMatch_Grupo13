class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        clave_normalizada = clave.lower()

        if self.raiz is None:
            self.raiz = NodoArbol(clave_normalizada, valor)
        else:
            self._insertar_recursivo(self.raiz, clave_normalizada, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        if clave < nodo.clave:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.izquierda, clave, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.derecha, clave, valor)

    def buscar(self, clave):
        clave_normalizada = clave.lower()
        return self._buscar_recursivo(self.raiz, clave_normalizada, 0)

    def _buscar_recursivo(self, nodo, clave, pasos):
        if nodo is None:
            return None, pasos

        pasos = pasos + 1

        if clave == nodo.clave:
            return nodo.valor, pasos

        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierda, clave, pasos)

        return self._buscar_recursivo(nodo.derecha, clave, pasos)

    def inorden(self):
        equipos = []
        self._inorden_recursivo(self.raiz, equipos)
        return equipos

    def _inorden_recursivo(self, nodo, equipos):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda, equipos)
            equipos.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, equipos)

    def preorden(self):
        equipos = []
        self._preorden_recursivo(self.raiz, equipos)
        return equipos

    def _preorden_recursivo(self, nodo, equipos):
        if nodo is not None:
            equipos.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, equipos)
            self._preorden_recursivo(nodo.derecha, equipos)

    def postorden(self):
        equipos = []
        self._postorden_recursivo(self.raiz, equipos)
        return equipos

    def _postorden_recursivo(self, nodo, equipos):
        if nodo is not None:
            self._postorden_recursivo(nodo.izquierda, equipos)
            self._postorden_recursivo(nodo.derecha, equipos)
            equipos.append(nodo.valor)
