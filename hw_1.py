class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname}, Age: {self.age},  Married: {self.is_married}')

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        return total_marks / num_subjects if num_subjects > 0 else 0

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Marks: {self.marks}, Average: {self.calculate_average():.2f}")
class Teacher(Person):
    base_salary = 30000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            bonus_years = self.experience - 3
            bonus = self.base_salary * 0.05 * bonus_years
            return self.base_salary + bonus
        else:
            return self.base_salary

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Experience: {self.experience} years, Salary: {self.calculate_salary()}som")

teacher = Teacher("Tom Cruise", 62, True, 20)
teacher.introduce_myself()

def create_students():
    student1 = Student("Moldosheva Zarina", 16, False, {"Math": 5, "Russian": 5, "History": 4})
    student2 = Student("Bogdanov David", 15, False, {"Math": 4, "Russian": 5, "History": 3})
    student3 = Student("Hasanov Kayrat", 17, False, {"Math": 5, "Russian": 3, "History": 5})
    return [student1, student2, student3]

students = create_students()

for student in students:
    student.introduce_myself()
