"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

def pedir_numero(lista: list) -> int:
    while True:
        try:
            numero = int(input("Please, insert the numbers: "))

            if not 1 <= numero <= 49:
                raise ValueError
            
            if lista.count(numero) >= 1:
                raise ValueError
            
        except ValueError:
            print("**Error**")
        except Exception:
            print("**Error**")
        else:
            return numero


def pedir_reintegro() -> int:
    while True:
        try:
            numero = int(input("Please, insert the reintegro: "))

            if not 0 <= numero <= 9:
                raise ValueError
            
        except ValueError:
            print("**Error**")
        
        return numero



def crear_lista_primitiva(lista: list):
    #pedir los 6 números
    for i in range(6):
        lista.append(pedir_numero(lista))

    lista.sort()

    #Pedir reintegro
    lista.append(pedir_reintegro())


def main():

    lista_primitiva = []
    crear_lista_primitiva(lista_primitiva)

    print(lista_primitiva)



if __name__ == "__main__":
    main()












