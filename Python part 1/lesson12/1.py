class Passport():

    def __init__(self, name, sname, date, country, number):
        self.name = name
        self.sname = sname
        self.date = date
        self.country = country
        self.number = number

    def PrintInfo(self):
        print(f"Name: {self.sname} {self.name}.")
        print(f'Date: {self.date}.')
        print(f'Country: {self.country}.')
        print(f'Passport number: {self.number}.')

class ForeignPassport(Passport):
    def __init__(self, name, sname, date, country, number, visa, exp_date):
        super().__init__(name, sname, date, country, number)
        self.visa = visa
        self.exp_date = exp_date

    def PrintInfo(self):
        super().PrintInfo()
        print(f'Visa: {self.visa}.')
        print(f'Expiration date: {self.exp_date}.')

    def days_before_expiration(self):
        from datetime import datetime
        start = datetime.today()
        end = datetime.strptime(self.exp_date, "%d/%m/%y")
        diff = (end - start)
        diff = diff.days
        print(f" Осталось дней: {diff}")




passport_1 = Passport("Tatyana", "Latukhina", "17.02", "Russia", 4509123456)
#passport_1.PrintInfo()
print("\n")
foreignPassport_1 = ForeignPassport("Tatyana", "Latukhina", "17.02", "Russia", 4509123456, "Visa USA", "22/5/23")
#foreignPassport_1.PrintInfo()
passport_list = []
passport_list.append(passport_1)
passport_list.append(foreignPassport_1)

for i in passport_list:
    i.PrintInfo()
    print("\n")

foreignPassport_1.days_before_expiration()

