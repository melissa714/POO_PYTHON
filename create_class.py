class Cake: 
    def __init__(self,flavor,color="jaune") :
        self.flavor = flavor
        self.color=color


    def cut_in_part(self,color): 
        print("le gateau est coupé en 4 part",color)


    def eat_cake(self):
        print("miam miam")




gateau=Cake("vanille")
print(gateau.flavor)
cake=Cake("chocolate")
print(cake.flavor)

print(cake.cut_in_part("vert"))






class Student:
    def __init__(self,name,roll_num,marks):
        self.name=name 
        self.roll_num=roll_num 
        self.marks=marks
        

class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color


rect1 = Rectangle(4, 2, color="blue")

rectangle=Rectangle(10,12)
print(rectangle.color)