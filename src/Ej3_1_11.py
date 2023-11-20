"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""
#Preguntar por este. 

vector1 = (1,2,3)
vector2 = (-1,0,2)


def main():
    productoEscalar = 0
    for i in range(len(vector1)):
        productoEscalar += (vector1[i] * vector2[i]) 

    print(f"El producto escalar de {vector1} y {vector2} es {productoEscalar}")








if __name__ == "__main__":
    main()













