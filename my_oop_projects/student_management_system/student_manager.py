class StudentManager:
    def __init__(self):
        self.students = []
        
    def add_students(self, student):
        self.students.append(student)
        print(f"Student {student.name} has been added.")
        
    def remove_students(self, student_id):
        for student in self.students:
            if self.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student.name} has been removed.")
                return
            print("Student not found.")