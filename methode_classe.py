class Laptop:
    def __init__(self,name,price):
        """constructeur"""
        self.name = name 
        self.price = price

    @classmethod
    def from_string(cls,string):
        """methode de classe"""
        import re 
        item = re.findall('')



    def applydiscount(self):
        """methode d'instance"""
        discountAmount = (self.price/100)*self.discount
        final_ammount = self.price - discountAmount
        return int(final_ammount)


m6600=Laptop('m6600',50000)

print(m6600.__dict__)