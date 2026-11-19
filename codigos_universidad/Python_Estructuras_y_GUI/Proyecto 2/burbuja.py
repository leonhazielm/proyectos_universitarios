# Importamos las librerías necesarias de PyQt6
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow, QMessageBox
from PyQt6 import uic

# Clase para manejar la lógica y la interfaz del ordenamiento Burbuja
class VentanaBurbuja(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargamos la ventana para este método
        uic.loadUi("burbuja.ui", self)
        
        # Lista temporal para guardar los números que el usuario va tecleando
        self.lista_numeros = []
        
        # Conectamos los botones de esta interfaz con sus funciones lógicas
        self.Guardar.clicked.connect(self.guardar_numero)
        self.pushButton_Ele.clicked.connect(self.mostrar_elementos)
        self.Resultado.clicked.connect(self.mostrar_resultado)

    def guardar_numero(self):
        # Obtenemos el texto introducido en el cuadro de texto
        texto = self.lineEdit.text()
        # Estructura try-except para validar que el usuario ingrese un número real
        try:
            # Intentamos convertir el texto a un número entero
            numero = int(texto)
            self.lista_numeros.append(numero)  # Lo añadimos a la lista
            self.lineEdit.clear()             # Limpiamos el cuadro para el siguiente número
        except ValueError:
            # Si el usuario metió letras, atrapamos el error y mostramos una alerta
            QMessageBox.critical(self, "Error", "Por favor, ingresa un número entero .")

    def mostrar_elementos(self):
        # Validamos si la lista tiene elementos antes de intentar mostrarlos
        if not self.lista_numeros:
            QMessageBox.warning(self, "Aviso", "La lista está vacia.")
            return
        # Convertimos la lista de enteros a un texto legible, separado por comas
        elementos_str = ", ".join(str(x) for x in self.lista_numeros)
        # Mostramos los elementos almacenados usando QMessageBox
        QMessageBox.information(self, "Elementos Almacenados", f"Lista actual:\n[{elementos_str}]")

    def mostrar_resultado(self):
        # Validamos que existan datos a ordenar
        if not self.lista_numeros:
            QMessageBox.warning(self, "Aviso", "No hay numeros para ordenar.")
            return
        
        # Hacemos una copia de la lista original para no modificar los datos introducidos
        lista_a_ordenar = self.lista_numeros.copy()
        
        # Llamamos al algoritmo de ordenar y guardamos su retorno
        lista_ordenada = self.ordenar_burbuja(lista_a_ordenar)
        
        # Mostramos el resultado final ordenado al usuario
        resultado_str = ", ".join(str(x) for x in lista_ordenada)
        QMessageBox.information(self, "Resultado Ordenado", f"Lista ordenada (Burbuja):\n[{resultado_str}]")

    # LÓGICA DEL ALGORITMO 
    def ordenar_burbuja(self, arr): #usamos arr (arraylist) para no correr el riesgo que con otro metodo se alteren nuestros datos 
        n = len(arr)
        # El ciclo externo indica cuántas "pasadas" dará el algoritmo
        for i in range(n):
            # El ciclo interno compara elementos adyacentes (ignorando los que ya están ordenados al final)
            for j in range(0, n - i - 1):
                # Si el elemento actual es mayor al siguiente, se intercambian de lugar
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    # Bloque principal de ejecución: verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    # Creamos el objeto de la aplicación
    app = QApplication(sys.argv)
    # Creamos la ventana principal y la hacemos visible
    ventana = VentanaBurbuja()
    ventana.show()
    # Iniciamos el ciclo de eventos de la app y garantizamos un cierre limpio al salir
    sys.exit(app.exec())