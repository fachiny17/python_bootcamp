from student import Student
from student_manager import StudentManager

student_manager = StudentManager()

while True:
    print("\nWelcome to our Student Management Menu")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice in ["1","Add Student"]:
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        student = Student(student_id, name, age)
        student_manager.add_students(student)
        
    elif choice in ["2","Remove Student"]:
        student_id = input("Enter student ID: ")
        student_manager.remove_student(student_id)
        
    elif choice in ["3","Display Student"]:
        student_manager.display_students(student_id)
        
    elif choice in ["4", "Exit"]:
        print("Exiting the Student Management System. Gye!")
        break
    
    else:
        print("Invalid choice. Choos from the above options.")