import time # Importamos el modulo time para poder utilizar sus funciones y medir el tiempo

class Factorial: # Creamos una clase llamada Factorial
    def __init__(self, numero): # Definimos un constructor para inicializar la variable numero con parametro self para indicar que pertenece a la clase y el parametro numero
        self.numero = numero # Creamos la variable numero y le asignamos el valor enviado por parametro, agregamos self al inicio para utilizarla en toda la clase
        
    def valido(self): # Definimos un metodo para comprobar si el numero es valido
        return self.numero >= 0 # Utilizamos return para regresar verdadero si el numero es mayor o igual a 0, o falso si es negativo
        
    def calcular(self): # Definimos un metodo para realizar el calculo matematico del factorial
        resultado = 1 # Creamos una variable local llamada resultado y la inicializamos en 1 porque el factorial se calcula multiplicando
        for i in range(1, self.numero + 1): # Utilizamos un ciclo for para iterar desde el numero 1 hasta el numero ingresado (le sumamos 1 porque range no incluye el limite superior)
            resultado *= i # Multiplicamos el valor que tiene la variable resultado por el valor de i en cada iteracion y lo guardamos ahi mismo
        return resultado # Utilizamos return para devolver el calculo final guardado en la variable resultado

# --- Bloque principal ---
 # Utilizamos esta condicion para asegurarnos de que el codigo de abajo solo corra si ejecutamos este archivo directamente
try: # Iniciamos un bloque try para intentar ejecutar el codigo y capturar errores si el usuario escribe letras en lugar de numeros
    entrada = input("Ingresa un número para calcular su factorial: ") # Utilizamos la funcion input para pedir un dato por consola y lo guardamos en la variable entrada
    numero_prueba = int(entrada) # Convertimos el texto de la variable entrada a un numero entero utilizando int() y lo guardamos en numero_prueba
    
    calculo = Factorial(numero_prueba) # Hacemos una instancia de la clase Factorial en la variable calculo y le pasamos el numero ingresado como parametro

    if calculo.valido(): # Utilizamos un if para verificar si el metodo valido() nos regresa verdadero
        print(f"\nCalculando el factorial de {numero_prueba}...") # Imprimimos un mensaje formateado con f indicando el inicio del calculo

        inicio_ejecucion = time.time() # Utilizamos el metodo time() para tomar la hora exacta del reloj de la computadora antes de iniciar
        inicio_proceso = time.process_time() # Utilizamos process_time() para registrar el tiempo que la CPU lleva trabajando antes del calculo

        resultado_final = calculo.calcular() # Mandamos llamar el metodo calcular y guardamos su retorno en la variable resultado_final

        fin_proceso = time.process_time() # Utilizamos process_time() de nuevo para registrar el tiempo del CPU justo al terminar el calculo
        fin_ejecucion = time.time() # Utilizamos time() para tomar la hora del reloj justo al terminar

        tiempo_total_ejecucion = fin_ejecucion - inicio_ejecucion # Restamos el tiempo de inicio al tiempo final para obtener los segundos reales que tardo
        tiempo_total_proceso = fin_proceso - inicio_proceso # Restamos los tiempos del CPU para saber cuanto tiempo de procesador neto se utilizo

        print("¡Cálculo terminado!\n") # Imprimimos un mensaje avisando que termino
        
        print(f"Tiempo de ejecución (Real): {tiempo_total_ejecucion:.6f} segundos") # Imprimimos el tiempo de ejecucion formateado a 6 decimales
        print(f"Tiempo de procesamiento (CPU): {tiempo_total_proceso:.6f} segundos") # Imprimimos el tiempo del CPU formateado a 6 decimales
        
        if numero_prueba <= 50: # Utilizamos un if para verificar si el numero es menor o igual a 50
            print(f"\nResultado: {resultado_final}") # Si es menor o igual a 50, imprimimos el resultado completo
        else: # Si el numero es mayor a 50 entra al else
            print("\n(El resultado numérico es demasiado grande y se ha omitido para no saturar la consola)") # Imprimimos este aviso para evitar que la consola se llene de numeros

    else: # Si el metodo valido() regresa falso entra a este else
        print("El número no es válido. Debe ser mayor o igual a 0.") # Imprimimos un mensaje de error por ser numero negativo
        
except ValueError: # Si en el bloque try ocurre un error de valor (como ingresar letras) entra a este except
    print("Error: Por favor, ingresa un número entero válido (no letras ni decimales).") # Imprimimos un mensaje pidiendo que se ingrese un numero correctamente