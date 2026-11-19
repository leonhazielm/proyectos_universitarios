class AnalizadorPalindromo:
    def __init__(self, texto_original):
        # Guardamos el texto original
        self.texto_original = texto_original
        
        self.texto_limpio = texto_original.lower().replace(" ", "")


    def verificar(self):
        inicio = 0
        fin = len(self.texto_limpio) - 1
        
        while inicio < fin:
            # Comparamos los extremos
            if self.texto_limpio[inicio] != self.texto_limpio[fin]:
                return False  # Si una letra no coincide, no es palíndromo
            
            # Movemos los índices hacia el centro
            inicio += 1
            fin -= 1
            
        return True  # Si terminó de revisar todo sin fallar, sí es

# terminal 
print("(Escribe 'salir' para terminar)\n")

while True:
    entrada = input("Escribe una palabra o frase: ")
    
    if entrada.lower() == 'salir':
        print("¡Programa terminado!")
        break
        
    analizador = AnalizadorPalindromo(entrada)
    
    if analizador.verificar():
        print(" Sí Es un palíndromo.\n")
    else:
        print(" No no es un palíndromo.\n")