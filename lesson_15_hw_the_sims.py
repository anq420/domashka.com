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

    def car_buy(self):
        car = Car()
        if self.__balance >= car.price:
            self.__balance -= car.price
            self.properties.car = True

    def car_sell(self):
        car = Car()
        if self.properties.car is True:
            self.__balance += car.price
            self.properties.car = None

    def house_buy(self):
        house = House()
        if self.properties.car is True and self.__balance >= house.price:
            self.__balance -= house.price
            self.properties.house = True
        else:
            return 'Not all requirements are met'

    def house_sell(self):
        house = House()
        if self.properties.house is True:
            self.__balance += house.price
            self.properties.house = None


class Properties:
    def __init__(self):
        self.car = None
        self.house = None


class Car:
    def __init__(self):
        self.price = 40


class House:
    def __init__(self):
        self.price = 100


def game():
    char = Person('Ilya')
    print(char)
    while char.balance < 140:
        char.work()
    print(char)
    char.car_buy()
    print(char)
    char.house_buy()
    print(char)
    char.car_sell()
    print(char)
    char.house_sell()
    print(char)
    return ''


print(game())
