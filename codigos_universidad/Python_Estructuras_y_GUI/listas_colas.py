class Operaciones: #creamos una clase llamda operaciones 
    def __init__(self):  #Definimos un contructor para inicializaar la variable lista con arametro self para indicar que pertenece a a clase  
        self.lista_elementos = [] #creamos la varible lista decelementos vacia, agregamos self al inicio para utilizarla en toda la clase 

    def agregar_nuevo_elemento(self, elemento): #definimos un metodo para agregar u elemento nuevo a la lista con un parametro llamado elemento
        self.lista_elementos.append(elemento) #utilizamos el metodo append de nuestra lista para insertar un uevo elemento enviandoselo como parametro

    def agregar_nuevo_elemento_con_posicion(self, posicion, elemento): #definimos un metodo para agregar un nuevo elemento mediante 2 parametrps (posicion)
       self.lista_elementos.insert(posicion, elemento)   #utilizamos el metodo de insert para agregar un nuevo elemento pasando el parametro de posicion

    def eliminar_elemento(self,elemento):  #definimos un metodo paara eliminar un parametro
        self.lista_elementos.remove(elemento) #utilizamos el metodo remove pAra eliminar el elemento de la lista enviado por parametro

    def eliminar_elemento_con_posicion(self,posicion): #definims un metodo para eliminar por posicion 
        self.lista_elementos.pop(posicion)    #utilizamos el metodo pop para eliminar un elemento indicandole la posicion 

    def eliminar_primer_elemento(self):#definimos un metodo para eliminar el primer metodo
        self.lista_elementos.pop(0)    #utilizamos el metodo pop para eliminar un elemento especificando la posicion 

    def eliminar_ultimo_elemento(self): #defini, un metodo para eliminar rl ultimo elemento 
        self.lista_elementos.pop()    #utilizamos el metodo pop para eliminarel ultimo eleento dejando vacio el parametro

    def mostrar_ellementos(self):#definimos un metodo para mostarar elementos en la lista 
        print("\n elementos de la lista\n")     #imprimimos un mensaje para especificar eel titulo  
        for elemento in self.lista_elementos: # utulizamos un for para recorrer la lista a traves de la variable
            print(elemento) #imprimimos la variable elemento

    def mostrar_cantidad_elementos(self): #definimos un metodo para mostrar la catidad de elementos
        print(f"la cantidad de elementos de la lista es {len(self.lista_elementos)}") #imprimimos la cantidad de elementos formateada con f y utilizando el metodo para que nos regrese el tamano de la lista

operaciones_clase = Operaciones()  #Hacemos una instacncia de la clase em la variable operaciones de esta forma podemos acceder 
 
operaciones_clase.agregar_nuevo_elemento("Leon") #mandamos llamar el metodo agregar nuevo elemento y le mandas string como parametro esperado del metodo
operaciones_clase.agregar_nuevo_elemento("Nery") #mandamos llamar el metodo agregar nuevo elemento y le mandas string como parametro esperado del metodo
operaciones_clase.agregar_nuevo_elemento("Moises") #mandamos llamar el metodo agregar nuevo elemento y le mandas string como parametro esperado del metodo

operaciones_clase.agregar_nuevo_elemento_con_posicion(1,"Miguel")
#print(operaciones_clase.lista_elementos)

operaciones_clase.eliminar_elemento("Moises")

operaciones_clase.eliminar_elemento_con_posicion(1)
#print(operaciones_clase.lista_elementos)  

operaciones_clase.eliminar_primer_elemento()
#print(operaciones_clase.lista_elementos)

operaciones_clase.eliminar_ultimo_elemento()
#print(operaciones_clase.lista_elementos)

operaciones_clase.mostrar_cantidad_elementos()
print(operaciones_clase.mostrar_cantidad_elementos)