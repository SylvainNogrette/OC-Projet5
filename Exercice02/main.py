import string

students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}
def ask_name() -> str :
    return input("Entrez le nom de l’étudiant :  ")

def calc_moyenne(student) -> float :
    maths, francais, histoire = students[student].values()
    moy = (maths + francais + histoire)/3
    print(f"Moyenne de  {student} : {moy}")
    return

def display_notes_of_student(student) -> string :


    msg = "Notes de " + student + " :  \n"

    for matiere, note in students[student].items():
        msg += matiere + " : " + str(note) + "\n"
    print(msg)
    return

student = ask_name()
if student not in students.keys():
    msg = "L'étudiant " + student + " n'existe pas dans la liste."
    print(msg)
else:
    display_notes_of_student(student)
    calc_moyenne(student)


