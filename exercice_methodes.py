
class Product:
    """creation de classe Product"""
    def __init__(self,productName,price):
        """constructeur"""
        self.productName=productName
        self.price=price

    def discount(self,discountvalue):
        """formule pour calculer le pourcentage du montant de l'accompte"""
        discountAmount=(self.price/100)*discountvalue
        final_price= self.price - discountAmount
        return int(final_price)



"""creation d'objet """
laptop=Product('Laptop',40000)
print(laptop.discount(10))
print(laptop.price)