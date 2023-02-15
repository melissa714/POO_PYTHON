class Date: 
    def __init__(self,year,month,day): #
        self.year = year 
        self.month=month 
        self.day = day 

    def arrange_value(self): #methode instance
        """concatené les attributs"""
        date = str(self.day) + '-' + str(self.month) +'-' + str(self.year)
        return  date

date1=Date(2022,6,17)

print(date1.__dict__)

print(date1.arrange_value())