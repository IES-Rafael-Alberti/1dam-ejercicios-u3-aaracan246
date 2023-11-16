"""
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
"""

lista = [50, 75, 46, 22, 80, 65, 8]

#Ordenamos la lista y luego simplemente mostramos la primera y última posición jeje // no sé cómo coger el último ítem de la lista (?)

def main():
    listaOrdenada = sorted(lista)
    print(listaOrdenada[0], listaOrdenada[6])



if __name__ == "__main__":
    main()



