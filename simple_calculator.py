from simple_operations import summa, subtraction, devision, multiply, exponentiation
from customexceptions import WrongOption, WrongValue

def calculator():
    users_choice = input('Доступные операции:\n+\n-\n*\n/\n**\n')
    error_message = 'Вводить необходимо только цифры! Попробуйте заново.'
    if users_choice == '+':
        while True:
            try:
                return summa()
            except WrongValue:
                print(f'{error_message}')
    if users_choice == '-':
            while True:
                try:
                    return subtraction()
                except WrongValue:
                    print(f'{error_message}')
    if users_choice == '*':
        while True:
            try:
                return multiply()
            except WrongValue:
                print(f'{error_message}')
    if users_choice == '/':
        while True:
            try:
                return devision()
            except WrongValue:
                print(f'{error_message}')
    if users_choice == '**':
        while True:
            try:
                return exponentiation()
            except WrongValue:
                print(f'{error_message}')
    if users_choice not in ['+', '-', '*', '/', '**']:
        raise WrongOption('Необходимо ввести название функции.')

while True:
    try:
        print(calculator())
        break
    except WrongOption:
        print('Необходимо правильно ввести название функции.')
