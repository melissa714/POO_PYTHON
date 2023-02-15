class Date: 
    def __init__(self,year,month,day): #
        self.year = year 
        self.month=month 
        self.day = day 

    def arrange_value(self): #methode instance
        """concatené les attributs"""
        date = str(self.day) + '-' + str(self.month) +'-' + str(self.year)
        return  date

    # @classmethod
    # def getDataformString(cls,string):
    #     import re 
    #     date = re.findall('\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}') # format 17-06-2022 ou 17/06/2022
    #     list_date=date.replace('/','-').split('-')
    #     print(list_date)
    #     day = list_date[0]
    #     month = list_date[1]
    #     year = list_date[2]
    #     return cls(year,month,day)

date1=Date(2022,6,17)

print(date1.__dict__)

print(date1.arrange_value())
date2=Date(2022,6,17)
print(date2.__dict__)
