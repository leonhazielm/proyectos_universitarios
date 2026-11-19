# 1. Creamos la memoria con 5 posiciones iniciales vacías
memoria = [None] * 5


# 2. Función HASH: convierte el texto a número con ord() y acota con % 5
def mi_hash(clave):
    suma = 0
    print(f"\n--- Convirtiendo '{clave}' a números ---")
    for letra in clave:
        numero_ascii = ord(letra)
        suma += numero_ascii
        print(f"Letra '{letra}' -> ASCII: {numero_ascii}")

    posicion = suma % 5
    print(f"Suma total: {suma} | Hash final (Suma % 5): {posicion}")
    return posicion


# 3. Función para guardar la clave y el valor en la posición calculada
def guardar(clave, valor):
    posicion = mi_hash(clave)
    memoria[posicion] = (clave, valor)
    print(
        f"\n[Éxito] '{clave}' guardado en la Posición [{posicion}] de la memoria."
    )


# 4. Función para imprimir el estado actual de la memoria
def mostrar_memoria():
    print("\n ESTADO DE LA MEMORIA ")
    for i in range(len(memoria)):
        print(f"Posición [{i}]: {memoria[i]}")


# 5. Bucle principal para que el usuario ingrese datos
while True:
    print("\n MENÚ HASH ")
    print("1. Agregar un dato")
    print("2. Ver estado de la memoria")
    print("3. Salir")

    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        clave_usuario = input("Ingresa la clave (ej. 'nombre'): ")
        valor_usuario = input("Ingresa la informacion de la clave (ej. 'leon'): ")
        guardar(clave_usuario, valor_usuario)

    elif opcion == "2":
        mostrar_memoria()

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción incorrecta, intenta de nuevo.")