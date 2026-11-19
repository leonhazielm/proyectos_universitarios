import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic

class Finonacci(QMainWindow):
    def __init__(self):
        super(Finonacci,self).__init__()
        uic.loadUi("fibo.ui",self) 

        
        self.igual.clicked.connect(self.calcular_fibo)
        self.cero.clicked.connect(self.boton_cero)
        self.uno.clicked.connect(self.boton_uno)
        self.dos.clicked.connect(self.boton_dos)
        self.tres.clicked.connect(self.boton_tres)
        self.cuatro.clicked.connect(self.boton_cuatro)
        self.cinco.clicked.connect(self.boton_cinco)
        self.seis.clicked.connect(self.boton_seis)
        self.siete.clicked.connect(self.boton_siete)
        self.ocho.clicked.connect(self.boton_ocho)
        self.nueve.clicked.connect(self.boton_nueve)
        self.AC.clicked.connect(self.boton_AC)
        self.volver.clicked.connect(self.close)

    

    def boton_cero(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "0"
                      self.lineEdit.setText(texto_calculadora)  
    def boton_uno(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "1"
                      self.lineEdit.setText(texto_calculadora)    
    def boton_dos(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "2"
                      self.lineEdit.setText(texto_calculadora)         
    def boton_tres(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "3"
                      self.lineEdit.setText(texto_calculadora)
    def boton_cuatro(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "4"
                      self.lineEdit.setText(texto_calculadora)
    def boton_cinco(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "5"
                      self.lineEdit.setText(texto_calculadora)
    def boton_seis(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "6"
                      self.lineEdit.setText(texto_calculadora) 
    def boton_siete(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "7"
                      self.lineEdit.setText(texto_calculadora)                           
    def boton_ocho(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "8"
                      self.lineEdit.setText(texto_calculadora)
    def boton_nueve(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "9"
                      self.lineEdit.setText(texto_calculadora)
    def boton_AC(self):
              self.lineEdit.clear()                      
    def boton_volver(self):
            self.close()
    def calcular_fibo(self):
        try:
            n = int(self.lineEdit.text())
            a, b = 0, 1
            resultado = ""
            for _ in range(n):
                resultado += str(a) + " "
                a, b = b, a + b
            self.label.setText(f"Secuencia: {resultado}")
        except ValueError:
            self.label.setText("Error: Ingresa un número entero")        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_Fibo = Finonacci()
    ventana_Fibo.show()
    sys.exit(app.exec())