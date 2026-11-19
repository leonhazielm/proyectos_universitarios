import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

from carpeta_segunda.segunda import Segunda 

class principal(QMainWindow):
    def __init__(self):
        super(principal,self).__init__()
        uic.loadUi("principal.ui",self) 
        self.pushButton.clicked.connect(self.abrir_segunda_ventana)
    def abrir_segunda_ventana(self):
        self.ventana2 = Segunda()
        self.ventana2.show()



app = QApplication(sys.argv)
ventana1 = principal()
ventana1.show()
sys.exit(app.exec())