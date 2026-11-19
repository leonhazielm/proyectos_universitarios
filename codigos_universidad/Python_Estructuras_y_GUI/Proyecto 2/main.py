# Importamos sys para poder manejar el cierre de la aplicación de forma segura con el sistema operativo
import sys

# Importamos las herramientas de PyQt6 necesarias para crear la aplicación, ventanas y alertas
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

# Importamos nuestras clases 
from burbuja import VentanaBurbuja
from quick import VentanaQuicksort
from shell import VentanaShell
from radix import VentanaRadix 

# Definimos la clase para la ventana de inicio que hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargamos el archivo de la interfaz principal hecha en Designer
        uic.loadUi("mian.ui",self)
        
        # Implementamos la conexión de nuestros botones y ejecuten la acción de abrir su ventana correspondiente
        self.pushButton_Burbuja.clicked.connect(self.abrir_burbuja)
        self.pushButton_Qui.clicked.connect(self.abrir_quicksort)
        self.pushButton_She.clicked.connect(self.abrir_shellsort)
        self.pushButton_Ra.clicked.connect(self.abrir_radix)

    # Funciones para inicializar y mostrar las ventanas secundarias de cada método
    def abrir_burbuja(self):
        # Instanciamos la clase de la ventana Burbuja y la mostramos en pantalla
        self.ventana_burbuja = VentanaBurbuja()
        self.ventana_burbuja.show()

    def abrir_quicksort(self):
        # Instanciamos la clase de la ventana Quicksort y la mostramos en pantalla
        self.ventana_quick = VentanaQuicksort()
        self.ventana_quick.show()

    def abrir_shellsort(self):
        # Instanciamos la clase de la ventana Shellsort y la mostramos en pantalla
        self.ventana_shell = VentanaShell()
        self.ventana_shell.show()

    def abrir_radix(self):
        # Instanciamos la clase de la ventana Radix y la mostramos en pantalla
        self.ventana_radix = VentanaRadix()
        self.ventana_radix.show()

# Bloque principal de ejecución: verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    # Creamos el objeto de la aplicación
    app = QApplication(sys.argv)
    # Creamos la ventana principal y la hacemos visible
    ventana = VentanaPrincipal()
    ventana.show()
    # Iniciamos el ciclo de eventos de la app y garantizamos un cierre limpio al salir
    sys.exit(app.exec())