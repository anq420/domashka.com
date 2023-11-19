from simple_operations import summa, subtraction, devision, multiply, exponentiation
from customexceptions import WrongOption, WrongValue

def calculator():
    users_choice = input('Доступные операции:\n-Сложение\n-Вычитание\n-Умножение\n-Деление\n-Возведение в степень. Напишите название операции, чтобы её выполнить.\n')
    if users_choice in ['Сложение', 'сложение']:
        while True:
            try:
                print(summa())
                break
            except WrongValue:
                print('Вводить необходимо только цифры! Попробуйте заново.')
    if users_choice in ['Вычитание', 'вычитание']:
            while True:
                try:
                    print(subtraction())
                    break
                except WrongValue:
                    print('Вводить необходимо только цифры! Попробуйте заново.')
    if users_choice in ['Умножение', 'умножение']:
        while True:
            try:
                print(multiply())
                break
            except WrongValue:
                print('Вводить необходимо только цифры! Попробуйте заново.')
    if users_choice in ['Деление', 'деление']:
        while True:
            try:
                print(devision())
                break
            except WrongValue:
                print('Вводить необходимо только цифры! Попробуйте заново.')
    if users_choice in ['Возведение в степень', 'возведение в сепень']:
        while True:
            try:
                print(exponentiation())
                break
            except WrongValue:
                print('Вводить необходимо только цифры! Попробуйте заново.')
    else:
        raise WrongOption('Необходимо ввести название функции.')

while True:
    try:
        print(calculator())
        break
    except WrongOption:
        print('Необходимо правильно ввести название функции.')