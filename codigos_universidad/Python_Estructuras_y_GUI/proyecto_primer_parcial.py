class Ticket: # Creamos una clase llamada Ticket para representar cada problema de la mesa de ayuda
    def __init__(self, nombre, descripcion): # Definimos un constructor para inicializar los atributos del ticket
        self.nombre = nombre # Guardamos el nombre
        self.descripcion = descripcion # Guardamos la descripcion

class MesaAyuda: # Creamos una clase principal llamada MesaAyuda 
    def __init__(self): # Definimos el constructor de la clase para inicializar nuestras listas
        self.cola_espera = [] # Creamos una lista vacia para simular una Cola (comportamiento FIFO : el primero en llegar es el primero en ser atendido)
        self.pila_historial = [] # Creamos una lista vacia para simular una Pila (comportamiento LIFO : el ultimo en llegar es el primero en salir)

    def registrar_ticket(self, nombre, descripcion): # Definimos un metodo para agregar un nuevo ticket a la cola
        nuevo_ticket = Ticket(nombre, descripcion) # Hacemos una instancia de la clase Ticket con los datos del usuario
        self.cola_espera.append(nuevo_ticket) # Utilizamos el metodo append de nuestra lista para insertar el ticket al final de la cola
        #apend sirve para insertar lo que sea con lo que pongamos al final de una lista
        print(f"Ticket de {nombre} registrado con éxito.") # Imprimimos un mensaje confirmando el registro formateado con f, f lo utilizamos para decirle a la maquina que insertaremos una variable entre los corchetes para que imprima su valor y no solo el nombre de la variable

    def atender_siguiente_ticket(self): # Definimos un metodo para atender el ticket mas antiguo
        if len(self.cola_espera) == 0: # Utilizamos len() y un if para verificar si la cola esta vacia (tiene 0 elementos) 
            #len es una libreria de java para contabilizar
            print("No hay tickets en espera.") # Imprimimos un aviso si no hay tickets
        else: # Si hay tickets en la cola entra a este else
            ticket_atendido = self.cola_espera.pop(0) # Utilizamos pop(0) para sacar y guardar el primer elemento de la cola (el mas antiguo) , pop con numero en el parenteesis manda a llamar la posicion que pusiste el numero en el parentesis,es decir en este caso cuando esta en 0 manda a llamar el primer dato ingresado
            self.pila_historial.append(ticket_atendido) # Utilizamos append para agregar el ticket que acabamos de sacar al final de la pila (historial)
            print(f"Atendiendo el ticket de: {ticket_atendido.nombre}") # Imprimimos un mensaje mostrando a quien estamos atendiendo

    def deshacer_ultima_atencion(self): # Definimos un metodo para deshacer un error al atender
        #utilizamos self para no mezclar
        if len(self.pila_historial) == 0: # Verificamos si la pila de historial esta vacia usando len()
            print("No hay atenciones para deshacer.") # Imprimimos un mensaje si no hay nada que deshacer
        else: # Si hay atenciones guardadas entra al else
            ticket_recuperado = self.pila_historial.pop() # Utilizamos pop() sin indice para sacar y guardar el ultimo ticket agregado a la pila (LIFO)
            self.cola_espera.insert(0, ticket_recuperado) # Utilizamos el metodo insert(0) para regresar el ticket al frente (posicion 0) de la cola de espera
            print(f"Atención deshecha. El ticket de {ticket_recuperado.nombre} volvió al frente.") # Avisamos que la operacion fue exitosa formateando con f

    def mostrar_tickets_espera(self): # Definimos un metodo para ver los tickets pendientes
        if len(self.cola_espera) == 0: # Verificamos si no hay tickets en la cola
            print("No hay tickets en espera.") # Imprimimos el aviso correspondiente
        else: # Si la cola tiene elementos entra al else
            print("\n--- Tickets en Espera (FIFO) ---") # Imprimimos el titulo de la seccion
            for i in range(len(self.cola_espera)): # Utilizamos un for para recorrer la cola desde el indice 0 hasta su longitud total
                t = self.cola_espera[i] # Guardamos el ticket de la posicion actual en una variable temporal t
                print(f"Usuario: {t.nombre} | Problema: {t.descripcion}") # Imprimimos los datos del ticket sumando 1 a la i para enumerarlos

    def mostrar_historial(self): # Definimos un metodo para enlistar los tickets atendidos
        if len(self.pila_historial) == 0: # Verificamos si la pila esta vacia
            print("No hay historial de atenciones.") # Imprimimos el mensaje de aviso
        else: # Si la pila tiene elementos entra al else
            print("\n--- Historial de Atenciones (LIFO) ---") # Imprimimos el titulo del historial
            for i in range(len(self.pila_historial) - 1, -1, -1): # Utilizamos un for invertido para recorrer la pila desde el final (mas reciente) hacia el inicio
                t = self.pila_historial[i] # Guardamos el ticket de la posicion actual en la variable temporal t
                print(f"- Usuario: {t.nombre} | Problema: {t.descripcion}") # Imprimimos los datos del ticket atendido

    def buscar_ticket_recursivo(self, nombre_buscado, indice=0): # Definimos una funcion recursiva para buscar un ticket enviando un indice inicial de 0
        if indice >= len(self.cola_espera): # Condicion base: Si el indice llega al tamaño de la lista significa que recorrimos toda la cola sin encontrarlo
            return None # Regresamos None indicando que no se encontro
        if self.cola_espera[indice].nombre.lower() == nombre_buscado.lower(): # Condicion base 2: Si el nombre en la posicion actual es igual al buscado (ambos en minusculas)
            return self.cola_espera[indice] # Regresamos el ticket encontrado en esa posicion
        return self.buscar_ticket_recursivo(nombre_buscado, indice + 1) # Llamada recursiva: Retornamos la misma funcion sumando 1 al indice para avanzar a la siguiente posicion

    def mostrar_cantidad(self): # Definimos un metodo para mostrar la cantidad de tickets pendientes
        print(f"Cantidad actual de tickets pendientes: {len(self.cola_espera)}") # Imprimimos usando len() para saber cuantos elementos tiene la cola en ese momento

#  INICIO DEL PROGRAMA PRINCIPAL ---
sistema = MesaAyuda() # Hacemos una instancia de la clase MesaAyuda en la variable sistema para poder usarla

while True: # Iniciamos un ciclo while True para mantener el menu repitiendose de forma infinita
    print("\n==== SISTEMA DE MESA DE AYUDA ====") # Imprimimos el encabezado del menu
    print("1. Registrar ticket") # Imprimimos la opcion 1
    print("2. Atender siguiente ticket") # Imprimimos la opcion 2
    print("3. Deshacer última atención") # Imprimimos la opcion 3    print("4. Mostrar tickets en espera") # Imprimimos la opcion 4
    print("5. Mostrar historial de atenciones") # Imprimimos la opcion 5
    print("6. Buscar ticket por nombre de usuario") # Imprimimos la opcion 6
    print("7. Mostrar cantidad de tickets en espera") # Imprimimos la opcion 7
    print("8. Salir") # Imprimimos la opcion de salida

    opcion = input("Elige una opción: ") # Utilizamos input para pedir al usuario que ingrese un dato y lo guardamos en la variable opcion

    if opcion == "1": # Utilizamos un if para verificar si el usuario eligio la opcion 1
        nombre = input("Ingresa el nombre del usuario: ") # Pedimos el nombre por consola y lo guardamos
        descripcion = input("Breve descripción del problema: ") # Pedimos la descripcion por consola y la guardamos
        sistema.registrar_ticket(nombre, descripcion) # Mandamos llamar el metodo registrar_ticket pasandole los datos del usuario

    elif opcion == "2": # Si la opcion ingresada es la 2 entra a este elif
        sistema.atender_siguiente_ticket() # Mandamos llamar el metodo para atender el siguiente ticket

    elif opcion == "3": # Si la opcion ingresada es la 3 entra a este elif
        sistema.deshacer_ultima_atencion() # Mandamos llamar el metodo para deshacer la atencion

    elif opcion == "4": # Si la opcion ingresada es la 4 entra a este elif
        sistema.mostrar_tickets_espera() # Mandamos llamar el metodo que imprime la cola

    elif opcion == "5": # Si la opcion ingresada es la 5 entra a este elif
        sistema.mostrar_historial() # Mandamos llamar el metodo que imprime la pila invertida

    elif opcion == "6": # Si la opcion ingresada es la 6 entra a este elif
        if len(sistema.cola_espera) == 0: # Verificamos si la cola esta vacia primero
            print("La cola de espera está vacía.") # Imprimimos un mensaje si no hay tickets donde buscar
        else: # Si hay tickets entra al else
            nombre_buscado = input("Ingresa el nombre de usuario a buscar: ") # Pedimos el nombre a buscar
            resultado = sistema.buscar_ticket_recursivo(nombre_buscado) # Llamamos al metodo recursivo y guardamos lo que retorna en la variable resultado
            if resultado is not None: # Si el resultado es diferente a None significa que si lo encontro
                print(f"\n¡Ticket encontrado! -> Usuario: {resultado.nombre} | Problema: {resultado.descripcion}") # Imprimimos los datos del ticket hallado
            else: # Si nos regreso None entra al else
                print("\nNo se encontró ningún ticket con ese nombre.") # Imprimimos que no hubo coincidencias

    elif opcion == "7": # Si la opcion ingresada es la 7 entra a este elif
        sistema.mostrar_cantidad() # Mandamos llamar el metodo que imprime el largo de la cola

    elif opcion == "8": # Si la opcion ingresada es la 8 entra a este elif
        print("Cerrando el sistema...") # Imprimimos un mensaje de despedida
        break # Utilizamos break para romper el ciclo while y finalizar el programa

    else: # Si el usuario ingresa un numero que no es del 1 al 8 entra aqui
        print("Opción inválida.") # Imprimimos un aviso de error
