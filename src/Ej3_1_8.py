"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""


def checkPalindromo():
    palabra = input("Please, insert a word: ")
    palabraAlReves = ''.join(reversed(palabra))
    
    #if (palabra == reversed(palabra)) == True: ########## Tiene que ser un iterable para ser comparable, así que así no vale.
    if palabra == palabraAlReves:
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")




def main():
    checkPalindromo()
    






if __name__ == "__main__":
    main()


