class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    @staticmethod 
    def prinstatement():
        print("this is static method")



s1 = Student('Sohail',26)
print(s1.__dict__)



print(s1.prinstatement())