class Factorial:
    def __init__(self, numero):
        self.numero = numero
        
    def valido(self):
        return self.numero >= 0
        
    def calcular(self):
        resultado = 1
        for i in range(1, self.numero + 1):
            resultado *= i
        return resultado

    