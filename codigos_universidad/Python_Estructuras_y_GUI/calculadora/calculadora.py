from PyQt6.QtWidgets import QMainWindow ,   QApplication , QMessageBox
from PyQt6 import uic
import sys

class Calculadora(QMainWindow):
        def __init__(self):
            super(Calculadora,self).__init__()
            uic.loadUi("ventana_calculadora.ui",self)


            self.mas.clicked.connect(self.boton_mas)   
            self.igual.clicked.connect(self.boton_igual)
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
            self.multiplicacion.clicked.connect(self.boton_multiplicacion)
            self.division.clicked.connect(self.boton_division)
            self.AC.clicked.connect(self.boton_AC)

         
        

        def boton_mas(self):
              texto_calculadora = self.lineEdit.text() 
              texto_calculadora = texto_calculadora + "+"
              self.lineEdit.setText(texto_calculadora)

        def boton_igual(self):
              try:
                    texto_calculadora = self.lineEdit.text()
                    resultado = eval(texto_calculadora.replace(" ",""))
                    self.lineEdit.setText(str(resultado))
              except:
                    QMessageBox.critical(self,"Error","Texto del mensaje")

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
        def boton_multiplicacion(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "*"
                      self.lineEdit.setText(texto_calculadora)
        def boton_division(self):
                      texto_calculadora = self.lineEdit.text() 
                      texto_calculadora = texto_calculadora + "/"
                      self.lineEdit.setText(texto_calculadora)

        def boton_AC(self):
              self.lineEdit.clear()




app = QApplication(sys.argv)
calculadora = Calculadora()       
calculadora.show()
sys.exit(app.exec())         

        