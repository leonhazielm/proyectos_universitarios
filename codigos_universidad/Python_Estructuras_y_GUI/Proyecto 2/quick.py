import sys
from PyQt6.QtWidgets import QApplication,QMainWindow, QMessageBox
from PyQt6 import uic

class VentanaQuicksort(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("quick.ui", self)
        self.lista_numeros = []
        
        # Conexión de botones
        self.Guardar.clicked.connect(self.guardar_numero)
        self.pushButton_Ele.clicked.connect(self.mostrar_elementos)
        self.Resultado.clicked.connect(self.mostrar_resultado)

    # (La lógica de guardar y mostrar se repite igual que en Burbuja)
    def guardar_numero(self):
        texto = self.lineEdit.text()
        try:
            numero = int(texto)
            self.lista_numeros.append(numero)
            self.lineEdit.clear()
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingresa un numero entero valido.")

    def mostrar_elementos(self):
        if not self.lista_numeros:
            QMessageBox.warning(self, "Aviso", "La lista está vacía.")
            return
        elementos_str = ", ".join(str(x) for x in self.lista_numeros)
        QMessageBox.information(self, "Elementos Almacenados", f"Lista actual:\n[{elementos_str}]")

    def mostrar_resultado(self):
        if not self.lista_numeros:
            QMessageBox.warning(self, "Aviso", "No hay numeros para ordenar.")
            return
        
        lista_a_ordenar = self.lista_numeros.copy()
        lista_ordenada = self.ordenar_quicksort(lista_a_ordenar)
        
        resultado_str = ", ".join(str(x) for x in lista_ordenada)
        QMessageBox.information(self, "Resultado Ordenado", f"Lista ordenada (Quicksort):\n[{resultado_str}]")

    # LÓGICA DEL ALGORITMO QUICKSORT
    def ordenar_quicksort(self, arr):
        # Caso base de la recursividad: Si la lista tiene 1 o 0 elementos, ya está ordenada
        if len(arr) <= 1:
            return arr
            
        # Elegimos el elemento central como pivote para comparar
        pivote = arr[len(arr) // 2]
        
        # Construimos tres sub-listas utilizando comprensión de listas
        izq = [x for x in arr if x < pivote]      # Elementos menores al pivote
        medio = [x for x in arr if x == pivote]   # Elementos iguales al pivote
        der = [x for x in arr if x > pivote]      # Elementos mayores al pivote
        
        # Llamamos a la función de manera recursiva uniendo los fragmentos
        return self.ordenar_quicksort(izq) + medio + self.ordenar_quicksort(der)

    # Bloque principal de ejecución: verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    # Creamos el objeto de la aplicación
    app = QApplication(sys.argv)
    # Creamos la ventana principal y la hacemos visible
    ventana = VentanaQuicksort()
    ventana.show()
    # Iniciamos el ciclo de eventos de la app y garantizamos un cierre limpio al salir
    sys.exit(app.exec())