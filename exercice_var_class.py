class Circle:
    pai=3.14
    def __init__(self,raduis):
        self.raduis = raduis 
        # self.pai=pai

    def circle_circumference(self):
        value_of_circle=2*Circle.pai*self.raduis 
        return value_of_circle

    def circle_Area(self):
        Area=Circle.pai * self.raduis**2
        return Area



    
c1=Circle(23)
c2=Circle(24)
print("==>> c2: ", c2.raduis)

print(c2.circle_circumference())
print(c1.circle_Area())