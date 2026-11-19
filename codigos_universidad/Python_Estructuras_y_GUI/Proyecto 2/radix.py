import sys
from PyQt6.QtWidgets import QApplication,QMainWindow, QMessageBox
from PyQt6 import uic

class VentanaRadix(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Radix.ui", self)
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
        lista_ordenada = self.ordenar_radix(lista_a_ordenar)
        
        resultado_str = ", ".join(str(x) for x in lista_ordenada)
        QMessageBox.information(self, "Resultado Ordenado", f"Lista ordenada (Radix):\n[{resultado_str}]")

    # LÓGICA DEL ALGORITMO  
    def ordenar_radix(self, arr):
        # Si la lista está vacía, no hay nada que ordenar
        if not arr:
            return arr
        
        # Búsqueda manual del número mayor para saber cuántos dígitos tiene
        # Esto respeta la restricción de no usar Max gracias Mtro. Victor >:(
        valor_maximo = arr[0]
        for num in arr:
            if num > valor_maximo:
                valor_maximo = num
                
        # Exponente inicial para unidades (1), decenas (10), centenas (100), etc.
        exponente = 1
        
        # Mientras queden dígitos por evaluar en el número más grande
        while valor_maximo // exponente > 0:
            # Creamos 10 'cubetas' vacías para clasificar dígitos del 0 al 9
            cubetas = [[] for _ in range(10)]
            
            # Clasificamos cada número en su cubeta correspondiente al dígito actual
            for num in arr:
                # Extraemos el dígito específico usando división entera y módulo
                indice = (num // exponente) % 10
                cubetas[indice].append(num)
            
            # Vaciamos todas las cubetas ordenadas de vuelta al arreglo principal
            indice_arr = 0
            for cubeta in cubetas:
                for num in cubeta:
                    arr[indice_arr] = num
                    indice_arr += 1
            
            # Multiplicamos por 10 para pasar a analizar la siguiente posición (Ej. unidades a decenas)
            exponente *= 10
            
        return arr

    # Bloque principal de ejecución: verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    # Creamos el objeto de la aplicación
    app = QApplication(sys.argv)
    # Creamos la ventana principal y la hacemos visible
    ventana = VentanaRadix()
    ventana.show()
    # Iniciamos el ciclo de eventos de la app y garantizamos un cierre limpio al salir
    sys.exit(app.exec())