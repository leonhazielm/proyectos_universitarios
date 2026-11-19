from PyQt6.QtWidgets import QMainWindow ,   QApplication
from PyQt6 import uic
import sys

class mi_primera_ventana(QMainWindow):
    def __init__(self):
        super(mi_primera_ventana, self).__init__()    
        uic.loadUi("ventana.ui",self)

        self.btnGuardar.clicked.connect(self.accion_guardar)   
    
    def accion_guardar(self):
        contenido = self.txtNombre.text()
        print(f"Hiciste click en el boton guardar y el contenido es {contenido}")




app = QApplication(sys.argv)
ventana = mi_primera_ventana()       
ventana.show()
sys.exit(app.exec()) 