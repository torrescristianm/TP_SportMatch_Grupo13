#  Árbol AVL balanceado con comparación frente a BST.


class NodoAVL:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _obtener_altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _obtener_factor_balance(self, nodo):
        if nodo is None:
            return 0
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha)

    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))
        x.altura = 1 + max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha))

        return x

    def _rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(self._obtener_altura(x.izquierda), self._obtener_altura(x.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))

        return y

    def insertar(self, clave, valor):
        clave_normalizada = str(clave).lower()
        self.raiz = self._insertar_recursivo(self.raiz, clave_normalizada, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        if nodo is None:
            return NodoAVL(clave, valor)

        if clave < nodo.clave:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, clave, valor)
        else:
            nodo.valor = valor
            return nodo

        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda), self._obtener_altura(nodo.derecha))
        balance = self._obtener_factor_balance(nodo)

        # Rotaciones
        # Izquierda-Izquierda
        if balance > 1 and clave < nodo.izquierda.clave:
            return self._rotar_derecha(nodo)
        # Derecha-Derecha
        if balance < -1 and clave > nodo.derecha.clave:
            return self._rotar_izquierda(nodo)
        # Izquierda-Derecha
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        # Derecha-Izquierda
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def buscar(self, clave):
        clave_normalizada = str(clave).lower()
        return self._buscar_recursivo(self.raiz, clave_normalizada, 0)

    def _buscar_recursivo(self, nodo, clave, pasos):
        if nodo is None:
            return None, pasos
        pasos += 1
        if clave == nodo.clave:
            return nodo.valor, pasos
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierda, clave, pasos)
        return self._buscar_recursivo(nodo.derecha, clave, pasos)

    def inorder(self):
        resultado = []
        self._inorder_rec(self.raiz, resultado)
        return resultado

    def _inorder_rec(self, nodo, res):
        if nodo:
            self._inorder_rec(nodo.izquierda, res)
            res.append(nodo.valor)
            self._inorder_rec(nodo.derecha, res)

    def preorder(self):
        resultado = []
        self._preorder_rec(self.raiz, resultado)
        return resultado

    def _preorder_rec(self, nodo, res):
        if nodo:
            res.append(nodo.valor)
            self._preorder_rec(nodo.izquierda, res)
            self._preorder_rec(nodo.derecha, res)

    def postorder(self):
        resultado = []
        self._postorder_rec(self.raiz, resultado)
        return resultado

    def _postorder_rec(self, nodo, res):
        if nodo:
            self._postorder_rec(nodo.izquierda, res)
            self._postorder_rec(nodo.derecha, res)
            res.append(nodo.valor)

    def obtener_altura(self):
        return self._obtener_altura(self.raiz)