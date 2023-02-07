class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 500:
            return 'Pass'
        else:
            return 'Fail'



s1=Student("mel",200)
s2=Student("meli",500)
s3=Student("me",580)
s4=Student("melis",280)
s5=Student("melia",400)
s6=Student("mea",900)
s7=Student("meia",100)
s8=Student("mia",500)
s9 = Student("ma", 600)

# print(s1.result())
total_student=[s1,s2,s3,s4,s5,s6,s7,s8,s9]
student_pass=[]
student_fail = []
total={}
for x in total_student:
    if x.result() == 'Pass':
       student_pass.append(x.name)
       total['pass student']=student_pass
    else:
        student_fail.append(x.name)
        total['fail student'] = student_fail


print(student_fail)
print(student_pass)
print(total)