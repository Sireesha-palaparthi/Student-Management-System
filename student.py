class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, student_id, name, age, course, marks):
        super().__init__(name, age)

        # Encapsulation
        self.__student_id = student_id
        self.course = course
        self.marks = marks

    def get_student_id(self):
        return self.__student_id

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"
        
    def to_dict(self):
        return {
            "student_id": self.__student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
            "grade": self.calculate_grade()
        }