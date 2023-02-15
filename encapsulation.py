class Employee: 
    #constructeur 
    def __init__(self,name,salary,project):

        self.name=name 
        self.salary=salary 
        self.project = project 


    def show(self):
        print("le nom est:",self.name , "le salaire est :",self.salary)


    def work(self):
        print(self.name,'le travail est',self.project)
    

emp=Employee('Jessa',80000,'NLP')

print(emp.__dict__)
print(emp.show())
print(emp.work())
        