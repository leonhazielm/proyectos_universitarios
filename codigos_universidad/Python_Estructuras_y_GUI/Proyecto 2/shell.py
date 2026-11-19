import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

class VentanaShell(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Shell.ui", self)
        self.lista_numeros = []
        
        self.Guardar.clicked.connect(self.guardar_numero)
        self.pushButton_Ele.clicked.connect(self.mostrar_elementos)
        self.Resultado.clicked.connect(self.mostrar_resultado)

    def guardar_numero(self):
        texto = self.lineEdit.text()
        try:
            numero = int(texto)
            self.lista_numeros.append(numero)
            self.lineEdit.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingresa un número entero válido.")

    def mostrar_elementos(self):
        if not self.lista_numeros:
            QMessageBox.warning(self, "Aviso", "La lista está vacía.")
            return
        elementos_str = ", ".join(str(x) for x in self.lista_numeros)
        QMessageBox.information(self, "Elementos Almacenados", f"Lista actual:\n[{elementos_str}]")

    def mostrar_resultado(self):
        if not self.lista_numeros:
            QMessageBox.warning(self, "Aviso", "No hay números para ordenar.")
            return
        
        lista_a_ordenar = self.lista_numeros.copy()
        lista_ordenada = self.ordenar_shell(lista_a_ordenar)
        
        resultado_str = ", ".join(str(x) for x in lista_ordenada)
        QMessageBox.information(self, "Resultado Ordenado", f"Lista ordenada (Shellsort):\n[{resultado_str}]")

    # LÓGICA DEL ALGORITMO SHELLSORT
    def ordenar_shell(self, arr):
        n = len(arr)
        # Definimos el "gap" inicial (salto o separación) como la mitad del tamaño del arreglo
        gap = n // 2
        
        # Mientras la separación sea mayor a 0, continuamos ordenando
        while gap > 0:
            # Recorremos la lista partiendo desde el valor del gap
            for i in range(gap, n):
                temp = arr[i] # Guardamos el elemento actual en una variable temporal
                j = i
                # Realizamos el desplazamiento de elementos hacia la derecha si son mayores a temp
                #Esto le permite al algoritmo retroceder a la posición anterior de ese mismo subgrupo para comprobar si el número temporal (temp) debe seguir moviéndose aún más a la izquierda antes de soltarlo en su posición definitiva.
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap #Toma el valor actual de j, le resta el valor de gap (la separación actual) y guarda ese nuevo resultado de vuelta en la misma variable j.
                # Colocamos el elemento temporal en su posición correcta
                arr[j] = temp
            # Reducimos la separación a la mitad para la siguiente iteración
            gap //= 2
            
        return arr

    # Bloque principal de ejecución: verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    # Creamos el objeto de la aplicación
    app = QApplication(sys.argv)
    # Creamos la ventana principal y la hacemos visible
    ventana = VentanaShell()
    ventana.show()
    # Iniciamos el ciclo de eventos de la app y garantizamos un cierre limpio al salir
    sys.exit(app.exec())