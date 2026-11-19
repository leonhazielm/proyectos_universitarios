from vectorial2 import vectorial2
numero = int(input("Ingresa un numero entero positivo: "))
obj = vectorial2(numero)
if obj.valido():
    print(f"El factorial de {numero} es: {obj.calcular()}") 
else:
    print("Ingresa un numero entero no negativo")