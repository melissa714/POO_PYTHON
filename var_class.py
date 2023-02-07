class Student:
    total_marks=1000
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks=marks
        self.total_marks=Student.total_marks

   
s1=Student('melisa',26,500)

print(s1.total_marks)