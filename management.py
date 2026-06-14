import json
import os
from student import Student


class StudentManagementSystem:
    FILE_NAME = "students.json"

    def __init__(self):
        self.students = []
        self.load_students()

    def add_student(self):
        try:
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            student = Student(
                student_id,
                name,
                age,
                course,
                marks
            )

            self.students.append(student)
            self.save_students()

            print("Student added successfully!")

        except ValueError:
            print("Invalid input.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print(f"""
ID     : {student.get_student_id()}
Name   : {student.name}
Age    : {student.age}
Course : {student.course}
Marks  : {student.marks}
Grade  : {student.calculate_grade()}
""")

    def search_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student.get_student_id() == student_id:
                print(f"""
ID     : {student.get_student_id()}
Name   : {student.name}
Age    : {student.age}
Course : {student.course}
Marks  : {student.marks}
Grade  : {student.calculate_grade()}
""")
                return

        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student.get_student_id() == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully.")
                return

        print("Student not found.")

    def save_students(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(
                [student.to_dict() for student in self.students],
                file,
                indent=4
            )

    def load_students(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)

                for item in data:
                    student = Student(
                        item["student_id"],
                        item["name"],
                        item["age"],
                        item["course"],
                        item["marks"]
                    )
                    self.students.append(student)

        except Exception as e:
            print("Error loading data:", e)

    def menu(self):
        while True:
            print("""
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
""")

            choice = input("Choose: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")