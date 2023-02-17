# Heritage

class Phone:
    """classe parent ou super classe"""

    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price, 0)

    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera):
        """Herite des attributs de la classe Phone"""
        # Phone.__init__(self,brand,model_name,price)
        super().__init__(brand, model_name, price)  # façon commune de faire l'heritage
        self.ram = ram
        self.internal_memory = internal_memory
        self.rare_camera = rare_camera


        self.rare_camera = rare_camera


class FlagShip(SmartPhone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rare_camera,front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rare_camera)
        """Herite des attributs de la classe Phone"""
        # Phone.__init__(self,brand,model_name,price)
        self.front_camera = front_camera



phone1 = Phone('Nokia', '1100', 40000)
print(phone1.price)
print(phone1.full_name())

smartphone1 = SmartPhone('samsung', 'A7', 60000, '4GB', '128GB', '25MP')
smart = FlagShip('Nasco', 'A7', 80000, '4GB', '128GB', '25MP','45MP')
print(smart.__dict__)
print(smart.price)

print(smartphone1.price)
print(smartphone1.full_name())
print(smart.full_name())
