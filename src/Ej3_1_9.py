"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
####NO SÉ SACARLO ME MATO
def contarVocales(palabra):
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    palabra = palabra.lower()

    for letra in palabra:
        if letra in vocales:
            vocales[letra] +=1




def main():
    palabra = input("Please, insert a word: ")
    resultado = contarVocales(palabra)

    for vocal in range(len()):
        print(f"{vocal}: {[]}")




if __name__ == "__main__":
    main()





