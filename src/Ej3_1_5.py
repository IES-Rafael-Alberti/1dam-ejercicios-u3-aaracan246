"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

#bruto: 
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Así para hacerlo con constructor:

#Esto me da fallo por irme por las ramas así que lo meto instant en un print:
#def reverseNumbers(numeros):
    #numerosReversed = reversed(numeros) 


def main():
    numbers = list(range(1,11)) 
    reversedNumbers = list(reversed(numbers))
    print("The numbers reversed would be: ", reversedNumbers)
    




if __name__ == "__main__":
    main()




