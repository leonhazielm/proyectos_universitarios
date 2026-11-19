import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from Finonacci import Finonacci
from Facto import Facto
from Mesa import Mesa
from Calculadora import Calculadora
class principal(QMainWindow):
    def __init__(self):
        super(principal,self).__init__()
        uic.loadUi("main.ui",self) 

        self.pushButton_Fibo.clicked.connect(self.abrir_ventana_fibo)
        self.pushButton_Facto.clicked.connect(self.abrir_ventana_facto)
        self.pushButton_Calc.clicked.connect(self.abrir_ventana_calc)
        self.pushButton_Mesa.clicked.connect(self.abrir_ventana_mesa)

    def abrir_ventana_fibo(self):
        self.abrir_ventana_fibo= Finonacci()
        self.abrir_ventana_fibo.show()
    def abrir_ventana_facto(self):
        self.abrir_ventana_facto= Facto()
        self.abrir_ventana_facto.show()
    def abrir_ventana_calc(self):
        self.abrir_ventana_calc= Calculadora()     
        self.abrir_ventana_calc.show()
    def abrir_ventana_mesa(self):
        self.abrir_ventana_mesa=Mesa()
        self.abrir_ventana_mesa.show()
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = principal()
    ventana_principal.show()
    sys.exit(app.exec())