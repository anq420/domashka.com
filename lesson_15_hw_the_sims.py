from random import randint
import json


class Person:
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        self.__car = None
        self.__house = None
        self.file_path = 'all_users_database.json'

    @property
    def balance(self):
        return self.__balance

    @property
    def car(self):
        return self.__car

    @property
    def house(self):
        return self.__house

    def creating_database(self):
        with open(self.file_path, 'w') as j_file:
            json.dump([], j_file)
            return j_file


class RealLife(Person):
    def adding_user_to_database(self):
        player_info_dict = {
            'username': self.name,
            'balance': self.balance,
            'car': self.car,
            'house': self.house
        }
        try:
            with open(self.file_path, 'r') as r_file:
                reader = json.load(r_file)
                for u_name in reader:
                    if u_name['username'] == self.name:
                        return player_info_dict
                else:
                    reader.append(player_info_dict)
                    with open(self.file_path, 'w') as w_file:
                        json.dump(reader, w_file)
        except FileNotFoundError:
            return self.creating_database(), self.adding_user_to_database()

    def work(self):
        salary = randint(5, 10)
        with open(self.file_path, 'r') as r_file:
            reader = json.load(r_file)
            for i in reader:
                balance_upd = i['balance'] + salary
                i['balance'] = balance_upd
        with open(self.file_path, 'w') as w_file:
            json.dump(reader, w_file)
        return f'Your balance now is {balance_upd} EUR'

    def car_buy(self):
        with open(self.file_path, 'r') as r_file:
            reader = json.load(r_file)
            for u_balance in reader:
                user_balance = u_balance['balance']
                car = 40
                while True:
                    user_choice = input('A car costs 40 EUR. Would you like to buy it: yes or not?\n').lower()
                    if user_choice == 'yes' and user_balance >= car:
                        for i in reader:
                            balance_upd = i['balance'] - car
                            i['balance'] = balance_upd
                            i['car'] = True
                        with open(self.file_path, 'w') as w_file:
                            json.dump(reader, w_file)
                            return f'A car was bought. Now your balance is {balance_upd} EUR'
                    elif user_choice == 'yes' and user_balance < car:
                        return 'Not enough money'
                    elif user_choice == 'not':
                        return ' '

    def house_buy(self):
        with open(self.file_path, 'r') as r_file:
            reader = json.load(r_file)
            for i in reader:
                user_balance = i['balance']
                car = i['car']
                house = 100
                while True:
                    user_choice = input('A house costs 100 EUR. Would you like to buy it: yes or not?\n').lower()
                    if user_choice == 'yes' and user_balance >= house and car is True:
                        for u_balance in reader:
                            balance_upd = u_balance['balance'] - house
                            u_balance['balance'] = balance_upd
                            i['house'] = True
                        with open(self.file_path, 'w') as w_file:
                            json.dump(reader, w_file)
                            return f'A house was bought. Now your balance is {balance_upd} EUR'
                    elif user_choice == 'yes' and user_balance < house:
                        return 'Not enough money'
                    elif user_choice == 'yes' and user_balance >= house and car is not True:
                        return 'You must buy a car first'
                    elif user_choice == 'not':
                        return 'OK, maybe next time'


player_1 = RealLife('Yoyo')
player_info = player_1.adding_user_to_database()


def the_sims_game():
    while True:
        user_choice = int(input('What you will do the next (choose a number):\n1 - Work\n2 - Buy a car\n3 - Buy a house\n'))
        if user_choice == 1:
            print(player_1.work())
        elif user_choice == 2:
            print(player_1.car_buy())
        elif user_choice == 3:
            print(player_1.house_buy())
        elif user_choice == 'exit':
            quit()


print(the_sims_game())