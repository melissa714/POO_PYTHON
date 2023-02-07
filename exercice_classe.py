class Product:
    def __init__(self,product_name,brand_name,mode_name,price):
        """constructeur"""
        self.product_name=product_name
        self.brand_name=brand_name
        self.mode_name=mode_name
        self.price=price
        self.productNameWithModeName=product_name+''+mode_name


"""creation d'objet à partir de la classe product"""
laptop=Product('Laptop','Dell','m4800',55000)
mobile=Product('Mobile','Samsumg','A7',50000)

print(laptop.mode_name)
print(laptop.brand_name)
print(laptop.productNameWithModeName)
print(mobile.productNameWithModeName)

print(laptop)