"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

miLista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
grades = []

    
def addSubjectGrade():
    for asignatura in miLista:
       grade = float(input(f"Please, insert {asignatura}'s grade: "))
       grades.append(grade) 

#Añadir método para eliminar las que estén por debajo del 5. Requiere volver a repasar la lista para ver cuáles cumplen el requisito.
def substractPassedSubject():
    nonPassedSubject = []
    for i in range(len(miLista)):
        if grades[i] < 5.0:
            nonPassedSubject.append(miLista[i])
    return nonPassedSubject


#Añadir una variable donde se almacene cuáles no están aprobadas.
def main():
    addSubjectGrade()
    print("Your grades are: ")
    for i in range(len(miLista)):
        print(f"In {miLista[i]} I've got a {grades[i]}")
    
    nonPassedSubject = substractPassedSubject()
    print("You have to repeat these subjects: ")
    if nonPassedSubject:
        for subject in nonPassedSubject:
            print(subject)







if __name__ == "__main__":
    main()

