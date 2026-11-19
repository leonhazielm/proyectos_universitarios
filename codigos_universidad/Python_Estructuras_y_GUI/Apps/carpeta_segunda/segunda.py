import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class Segunda(QMainWindow):
    def __init__(self):
        super(Segunda,self).__init__()
        uic.loadUi("carpeta_segunda/secundaria.ui",self) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana2 = Segunda()
    ventana2.show()
    sys.exit(app.exec())