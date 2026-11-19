print ("hello world" )
#except Exception as ex :
#print (ex)
saludo = "hola"
print(saludo)
def suma (a, b):
        resultado = a + b 
        return resultado
print("la suma es :" ,suma(10,10))
def resta (a, b):
        resultado = a - b 
        return resultado
print ("el resultado de la resta es : ",  resta (20,80))
def multiplicacion (a,b):
        resultado = a * b 
        return resultado
print("el resultado de la multiplicacion es " , multiplicacion (60,80))
def division (a,b) :
    
        resultado = a / b 
        return resultado
print("el resultado de la division es ", division (20,20))
def suma():
            a = input("ingresa el primer numero :")
            b = input("inggrese el segundo numero ")

            try :
                a = int(a)
                b = int (b)
            except :
                print("Los numeros que ingresaste no son validos " )
                suma()
            resultado = a + b 
            print("La suma es :" , resultado)
suma ()


while True :
       operacion = input ("Ingresa el tipo de operacion :")
       if operacion == "suma" :
              suma () 
       