students = ['Hermione', 'Herry', 'Ron']

for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])


students = {
    'Hermoine': 'Gryffindor',
    'Harry': 'Gryffindor',
    'Ron': 'Gryffindor',
    'Draco': 'Slytherin',
}

for student in students:
    print(student, students[student], sep=': ')