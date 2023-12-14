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
        while True:
            user_choice = input('A car costs 40 EUR. Would you like to buy it: yes or not?\n').lower()
            if user_choice == 'yes' and self.balance >= 40:
                self.balance = self.balance - 40
                return f'A car was bought. Now your balance is {self.balance} EUR'
            elif user_choice == 'yes' and self.balance < 40:
                return 'Not enough money'
            elif user_choice == 'not':
                return 'Ok, maybe next time'

    def house_buy(self):
        while True:
            user_choice = input('A house costs 100 EUR. Would you like to buy it: yes or not?\n').lower()
            if user_choice == 'yes' and self.balance >= 100 and self.car is True:
                self.balance = self.balance - 100
                self.house = True
                return f'A house was bought. Now your balance is {self.balance} EUR'
            elif user_choice == 'yes' and self.balance < 100:
                return 'Not enough money'
            elif user_choice == 'yes' and self.balance >= 100 and self.car is not True:
                return 'You must buy a car first'
            elif user_choice == 'not':
                return 'OK, maybe next time'

    def sell_car(self):
        if self.car is True:
            user_choice = input('Do you really want to sell a car for 40 EUR: yes or no\n').lower()
            if user_choice == 'yes':
                self.balance = self.balance + 40
                self.car = None
                return f'Your car was sold. Now your balance is {self.balance} EUR'
            if user_choice == 'no':
                return 'OK, maybe next time'
        if self.car is None:
            return 'You have nothing to sell'

    def sell_house(self):
        if self.house is True:
            user_choice = input('Do you really want to sell a house for 100 EUR: yes or no\n').lower()
            if user_choice == 'yes':
                self.balance = self.balance + 100
                self.house = None
                return f'Your house was sold. Now your balance is {self.balance} EUR'
            if user_choice == 'no':
                return 'OK, maybe next time'
        if self.house is None:
            return 'You have nothing to sell'


person = RealLife()
while person.balance < 40:
    print(person.work())
print(person.car_buy())
while person.balance < 100:
    print(person.work())
print(person.house_buy())
print(person.sell_house())
print(person.sell_car())
