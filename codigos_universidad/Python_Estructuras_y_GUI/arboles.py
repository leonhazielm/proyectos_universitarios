class Nodo:
   # Representa cada nodo dentro del árbol.

    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
   
#Clase que gestiona las operaciones del arbol

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
       # Inserta un elemento manteniendo el orden del árbol BST.
        if self.raiz is None:
            self.raiz = Nodo(valor)
            print(f"Raíz creada con valor: {valor}")
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
                print(
                    f"Insertado {valor} a la IZQUIERDA de {nodo_actual.valor}"
                )
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
                print(f"Insertado {valor} a la DERECHA de {nodo_actual.valor}")
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    def recorrido_inorden(self, nodo):
       # recorrido Inorden (Izquierda -> Raíz -> Derecha): imprime valores de menor a mayor.
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.recorrido_inorden(nodo.derecho)

    def buscar(self, nodo, valor):
      # Busca si un valor existe dentro del árbol.
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self.buscar(nodo.izquierdo, valor)
        else:
            return self.buscar(nodo.derecho, valor)


# Ejemplo de Ejecución 
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()

    # Construcción del árbol
    valores = [50, 30, 70, 20, 40, 60, 80]
    print(" Construcción del Árbol ")
    for v in valores:
        arbol.insertar(v)

    print("Recorrido Inorden (Valores Ordenados)")
    arbol.recorrido_inorden(arbol.raiz)
    print()

    print(" Búsqueda de Valores ")
    for num in [40, 90]:
        existe = arbol.buscar(arbol.raiz, num)
        print(f"¿El valor {num} existe en el árbol?: {existe}")