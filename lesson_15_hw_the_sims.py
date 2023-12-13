from random import randint


class RealLife:
    def __init__(self):
        self.balance = 0
        self.car = None
        self.house = None

    def work(self):
        salary = randint(5, 10)
        self.balance = self.balance + salary
        return f'Your balance now is {self.balance} EUR'

    def car_buy(self):
        car = 40
        while True:
            user_choice = input('A car costs 40 EUR. Would you like to buy it: yes or not?\n').lower()
            if user_choice == 'yes' and self.balance >= car:
                self.balance = self.balance - car
                return f'A car was bought. Now your balance is {self.balance} EUR'
            elif user_choice == 'yes' and self.balance < car:
                return 'Not enough money'
            elif user_choice == 'not':
                return 'Ok, maybe next time'

    def house_buy(self):
        house = 100
        while True:
            user_choice = input('A house costs 100 EUR. Would you like to buy it: yes or not?\n').lower()
            if user_choice == 'yes' and self.balance >= house and self.car is True:
                self.balance = self.balance - house
                self.house = True
                return f'A house was bought. Now your balance is {self.balance} EUR'
            elif user_choice == 'yes' and self.balance < house:
                return 'Not enough money'
            elif user_choice == 'yes' and self.balance >= house and self.car is not True:
                return 'You must buy a car first'
            elif user_choice == 'not':
                return 'OK, maybe next time'


person = RealLife()
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.house_buy())
print(person.car_buy())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.house_buy())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.work())
print(person.house_buy())
print(person.car_buy())
