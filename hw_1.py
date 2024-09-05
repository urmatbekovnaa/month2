class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'hi, my name is: {self.fullname} my age: {self.age} married: {self.is_married}')

person = Person("Adina", 17, "False")
(person.introduce_myself())

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

