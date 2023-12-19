from random import randint


class Person:
    def __init__(self, name):
        self.name = name
        self.properties = Properties()
        self.__balance = 0

    def __repr__(self):
        return f'''
{self.name} has on his balance {self.__balance} EUR
Car - {self.properties.car}, house - {self.properties.house}'''

    @property
    def balance(self):
        return self.__balance

    def work(self):
        self.__balance += randint(5, 10)
        return self.__balance

    def car_buy(self, car):
        if self.__balance >= car.price:
            self.__balance -= car.price
            self.properties.car = 'available'

    def car_sell(self, car):
        if self.properties.car == 'available':
            self.__balance += car.price
            self.properties.car = 'unavailable'

    def house_buy(self, house):
        if self.properties.car == 'available' and self.__balance >= house.price:
            self.__balance -= house.price
            self.properties.house = 'available'
        else:
            return 'Not all requirements are met'

    def house_sell(self, house):
        if self.properties.house == 'available':
            self.__balance += house.price
            self.properties.house = 'unavailable'


class Properties:
    def __init__(self):
        self.car = 'unavailable'
        self.house = 'unavailable'


class Car:
    def __init__(self):
        self.price = 40

    def __str__(self):
        return 'available'


class House:
    def __init__(self):
        self.price = 100

    def __str__(self):
        return 'available'


def game():
    char = Person('Ilya')
    car = Car()
    house = House()
    print(char)
    while char.balance < 140:
        char.work()
    print(char)
    char.car_buy(car)
    print(char)
    char.house_buy(house)
    print(char)
    char.car_sell(car)
    print(char)
    char.house_sell(house)
    print(char)
    return ''


print(game())
