"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> 
has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

miLista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
grades = []

    
def addSubjectGrade():
    for asignatura in miLista:
       grade = float(input(f"Please, insert {asignatura}'s grade: "))
       grades.append(grade) 




def main():
    addSubjectGrade()
    print("Your grades are: ")
    for i in range(len(miLista)):
        print(f"In {miLista[i]} I've got a {grades[i]}")
    








if __name__ == "__main__":
    main()




