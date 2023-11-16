"""
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""

def calcularMedia(numeros):
    
    suma = sum(numeros)
    
    return suma / len(numeros)
   


def main():

    listaDeNumeros = []

    numeros = int(input("Please, insert the numbers: "))
    
    calcularMedia()








if __name__ == "__main__":
    main()
