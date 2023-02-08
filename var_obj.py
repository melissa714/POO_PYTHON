class Laptop:
    discount=10
    sno=0
    def __init__(self,name,price):
        Laptop.sno += 1
        self.sno=Laptop.sno
        self.name=name 
        self.price=price

    def applydiscount(self):
        discount_amount=(self.price/100)*self.discount
        final_amount=self.price - discount_amount
        return final_amount


m6600=Laptop('m6600',55000)
m4680 = Laptop('m4680', 50000)
m2680 = Laptop('m4680', 20000)

m4680.bluetooth='yes'
print(m4680.__dict__)
print(m4680.bluetooth)
print(m6600.name,m6600.price)
print(m6600)

print(m6600.applydiscount())

print(m4680.applydiscount())
m4680.discount=8
print(m6600.__dict__)
print(m4680.__dict__)
print(m2680.__dict__)

print(m4680.applydiscount())
