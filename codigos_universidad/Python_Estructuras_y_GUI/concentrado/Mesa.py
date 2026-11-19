import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class Ticket: 
    def __init__(self, nombre, descripcion): 
        self.nombre = nombre 
        self.descripcion = descripcion 

class Mesa(QMainWindow): 
    def __init__(self): 
        super(Mesa, self).__init__()
        uic.loadUi("mesa.ui", self)
        
        self.cola_espera = [] 
        self.pila_historial = [] 
        self.registrar.clicked.connect(self.registrar_ticket)
        self.atender.clicked.connect(self.atender_siguiente_ticket)
        self.deshacer.clicked.connect(self.deshacer_ultima_atencion)
        self.mostrar_espera.clicked.connect(self.mostrar_tickets_espera)
        self.historial.clicked.connect(self.mostrar_historial)
        self.buscar.clicked.connect(self.iniciar_busqueda)
        self.mostrar.clicked.connect(self.mostrar_cantidad)
        self.volver.clicked.connect(self.close)

    def registrar_ticket(self): 
        nombre = self.lineEdit.text().strip()
        descripcion = self.lineEdit_2.text().strip()
        
        if nombre != "" and descripcion != "":
            nuevo_ticket = Ticket(nombre, descripcion) 
            self.cola_espera.append(nuevo_ticket) 
            self.pantalla_salida.setText(f"Ticket de '{nombre}' registrado con éxito.")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        else:
            self.pantalla_salida.setText("Error: Debes ingresar el nombre y la descripción para registrar.")

    def atender_siguiente_ticket(self): 
        if len(self.cola_espera) == 0: 
            self.pantalla_salida.setText("No hay tickets en espera para atender.") 
        else: 
            ticket_atendido = self.cola_espera.pop(0) 
            self.pila_historial.append(ticket_atendido) 
            self.pantalla_salida.setText(f"Atendiendo el ticket de: {ticket_atendido.nombre}\nProblema: {ticket_atendido.descripcion}")

    def deshacer_ultima_atencion(self):
        if len(self.pila_historial) == 0:
            self.pantalla_salida.setText("No hay atenciones para deshacer.")
        else:
            ticket_recuperado = self.pila_historial.pop()
            self.cola_espera.insert(0, ticket_recuperado)
            self.pantalla_salida.setText(f"Atención deshecha.\nEl ticket de '{ticket_recuperado.nombre}' volvió al frente de la cola.")

    def mostrar_tickets_espera(self): 
        if len(self.cola_espera) == 0: 
            self.pantalla_salida.setText("La cola de espera está vacía.") 
        else: 
            texto = "--- Tickets en Espera (FIFO) ---\n\n" 
            for i in range(len(self.cola_espera)): 
                t = self.cola_espera[i] 
                texto += f"{i + 1}. Usuario: {t.nombre} | Problema: {t.descripcion}\n"
            self.pantalla_salida.setText(texto)

    def mostrar_historial(self): 
        if len(self.pila_historial) == 0: 
            self.pantalla_salida.setText("No hay historial de atenciones.") 
        else: 
            texto = "--- Historial de Atenciones (LIFO) ---\n\n" 
            for i in range(len(self.pila_historial) - 1, -1, -1): 
                t = self.pila_historial[i] 
                texto += f"- Usuario: {t.nombre} | Problema: {t.descripcion}\n"
            self.pantalla_salida.setText(texto)

    def iniciar_busqueda(self):
        nombre_buscado = self.lineEdit.text().strip()
        if len(self.cola_espera) == 0:
            self.pantalla_salida.setText("La cola de espera está vacía, no hay dónde buscar.")
            return
            
        if nombre_buscado == "":
            self.pantalla_salida.setText("Error: Ingresa un nombre en la primera caja de texto para buscar.")
            return

        resultado = self.buscar_ticket_recursivo(nombre_buscado)
        
        if resultado is not None:
            self.pantalla_salida.setText(f"¡Ticket encontrado!\nUsuario: {resultado.nombre}\nProblema: {resultado.descripcion}")
        else:
            self.pantalla_salida.setText(f"No se encontró ningún ticket en espera para el usuario: '{nombre_buscado}'.")

    def buscar_ticket_recursivo(self, nombre_buscado, indice=0): 
        if indice >= len(self.cola_espera): 
            return None 
        if self.cola_espera[indice].nombre.lower() == nombre_buscado.lower(): 
            return self.cola_espera[indice] 
        return self.buscar_ticket_recursivo(nombre_buscado, indice + 1)

    def mostrar_cantidad(self): 
        cantidad = len(self.cola_espera)
        self.pantalla_salida.setText(f"Cantidad actual de tickets pendientes en la cola: {cantidad}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Mesa()
    ventana.show()
    sys.exit(app.exec())