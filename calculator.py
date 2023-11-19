from operations import summa, subtraction, devision, multiply, exponentiation
from customexceptions import WrongOption

def calculator():
    users_choice = input('Доступные операции:\n-Сложение\n-Вычитание\n-Умножение\n-Деление\n-Возведение в степень. Напишите название операции, чтобы её выполнить.\n')
    if users_choice in ['Сложение', 'сложение']:
        return summa()
    if users_choice in ['Вычитание', 'вычитание']:
        return subtraction()
    if users_choice in ['Умножение', 'умножение']:
        return multiply()
    if users_choice in ['Деление', 'деление']:
        return devision()
    if users_choice in ['Возведение в степень', 'возведение в сепень']:
        return exponentiation()
    else:
        raise WrongOption('Необходимо ввести название функции.')

while True:
    try:
        print(calculator())
        break
    except WrongOption:
        print('Необходимо правильно ввести название функции.')
