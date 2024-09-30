class StudentManager:
    def __init__(self):
        self.students = []
        
    def add_students(self, student):
        self.students.append(student)
        print(f"Student {student.name} has been added.")
        
    def remove_student(self, student_id):
        for student in self.students:
            if self.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student.name} has been removed.")
                return
        print("Student not found.")
        
    def display_students(self, student_id):
        if student_id not in self.studnts:
            print("No student available.")
        else:
            print("Students List:")
            for student in self.students:
                print(student)