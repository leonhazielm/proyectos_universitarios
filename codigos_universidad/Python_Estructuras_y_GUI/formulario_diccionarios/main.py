import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("formulario.ui", self)

        self.diccionario_registros = {}

        self.pushButton.clicked.connect(self.guardar_datos)
        self.pushButton_2.clicked.connect(self.buscar)
        self.pushButton_3.clicked.connect(self.eliminar)
        self.pushButton_4.clicked.connect(self.limpiar_campos)

    def guardar_datos(self):
        numero_control = self.lineEdit_9.text()
        persona = {
            "nombre": self.lineEdit.text(),
            "apellido_paterno": self.lineEdit_2.text(),
            "apellido_materno": self.lineEdit_3.text(),
            "edad": self.lineEdit_4.text(),
            "carrera": self.lineEdit_5.text(),
            "semestre": self.lineEdit_6.text(),
            "municipio": self.lineEdit_7.text(),
            "estado": self.lineEdit_8.text(),
            "Numero de control": numero_control
        }

        if not persona["nombre"] or not persona["Numero de control"]:
            QMessageBox.warning(self, "Campos vacios", "Por favor llena el nombre y el numero de control como minimo para registrarlo")
            return

        if numero_control in self.diccionario_registros:
            respuesta = QMessageBox.question(
                self,
                "Pregunta",
                "Quieres sobrescribir los datos?"
            )
            if respuesta != QMessageBox.StandardButton.Yes:
                return

        self.diccionario_registros[numero_control] = persona
        print("Diccionario individual:", persona)
        print("Diccionario de diccionario:", self.diccionario_registros)
        self.limpiar_campos()

    def buscar(self):
        numero_control = self.lineEdit_9.text()
        if numero_control in self.diccionario_registros:
            datos = self.diccionario_registros[numero_control]

            self.lineEdit.setText(datos["nombre"])
            self.lineEdit_2.setText(datos["apellido_paterno"])
            self.lineEdit_3.setText(datos["apellido_materno"])
            self.lineEdit_4.setText(datos["edad"])
            self.lineEdit_5.setText(datos["carrera"])
            self.lineEdit_6.setText(datos["semestre"])
            self.lineEdit_7.setText(datos["municipio"])
            self.lineEdit_8.setText(datos["estado"])
            self.lineEdit_9.setText(datos["Numero de control"])
        else:
            QMessageBox.warning(self, "No encontrado", "No existe ningun registro con ese numero de control.")

    def eliminar(self):
        numero_control = self.lineEdit_9.text()
        if numero_control in self.diccionario_registros:
            del self.diccionario_registros[numero_control]
            QMessageBox.information(self,"Eliminado","Ha sido eliminado correcta mente")        
            print("Diciionario actualizado:", self.diccionario_registros)
            self.limpiar_campos
        else:
            QMessageBox.warning(self,"No hay nadie con esos datos")    

    def limpiar_campos(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec())