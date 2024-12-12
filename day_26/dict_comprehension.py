import random

names = ["Chisom", "Ikenna", "Venessa",
         "Chinwendu", "Jack", "Kane", "Alex", "Hannah"]
students_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for (
    student, score) in students_scores.items() if score >= 60}
print(passed_students)
