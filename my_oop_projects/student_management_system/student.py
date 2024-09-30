class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
        
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}"