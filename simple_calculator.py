from simple_operations import summa, subtraction, devision, multiply, exponentiation
from customexceptions import WrongOption

def users_choice():
    while True:
        try:
            user_choose = input('Доступные операции:\n+\n-\n*\n/\n**\n')
            if user_choose not in ['+', '-', '*', '/', '**']:
                raise WrongOption
            else:
                return user_choose
        except WrongOption:
            print('Выберите нужную операцию:\n') 


def calculator(operation):
    if operation == '+':
        return summa()
    if operation == '-':
        return subtraction()
    if operation == '*':
        return multiply()
    if operation == '/':
        return devision()
    if operation == '**':
        return exponentiation()

print(calculator(users_choice()))
