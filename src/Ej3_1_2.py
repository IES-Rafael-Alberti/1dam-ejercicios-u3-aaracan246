"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
donde <asignatura> sobre cada una de las asignaturas de la lista.
"""

miLista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

def imprimirLista():
    print(miLista)






def main():
    for asignatura in miLista:
        print("Yo estudio", asignatura)









if __name__ == "__main__":
    main()

