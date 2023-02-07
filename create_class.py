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


class Bird:
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions={}
    """un oiseau"""
    def __init__(self,name) :
        """les attributs definis ici sont des attributs d'instance """
        self.wings=2 
        self.position=1,2
        self.name=name

        self.positions[self.position]=self.name


    @classmethod
    def find_bird(cls,position):
        """retrouve un oiseau selon sa position"""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]}"
        return "On a rien trouvé"


# bird=Bird()
# print(bird.wings)




rect1 = Rectangle(4, 2, color="blue")

rectangle=Rectangle(10,12)
print(rectangle.color)

rectangle.color="yellow"
print(rectangle.color)

print(Bird.names[1])
Bird.names 
Bird.positions
bird = Bird("hirronde")
print(Bird.find_bird((1,2)))
print(Bird.find_bird((2, 5)))
