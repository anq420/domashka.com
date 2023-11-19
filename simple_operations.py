from customexceptions import WrongValue

def get_user_digit():
    while True:
        try:
            dig_1 = input('Введите первое число: ')
            if not dig_1.isdigit():
                raise WrongValue
            dig_2 = input('Введите второе число: ')
            if not dig_2.isdigit():
                raise WrongValue
            break
        except WrongValue:
            print('Необходимо вводить числа!')
    return dig_1, dig_2

def summa():
    user_digit = get_user_digit()
    dig_1, dig_2 = user_digit[0], user_digit[1]
    return int(dig_1) + int(dig_2)

def subtraction():
    user_digit = get_user_digit()
    dig_1, dig_2 = user_digit[0], user_digit[1]
    return int(dig_1) - int(dig_2)

def multiply():
    user_digit = get_user_digit()
    dig_1, dig_2 = user_digit[0], user_digit[1]
    return int(dig_1) * int(dig_2)

def devision():
    user_digit = get_user_digit()
    dig_1, dig_2 = user_digit[0], user_digit[1]
    return int(dig_1) / int(dig_2)

def exponentiation():
    user_digit = get_user_digit()
    dig_1, dig_2 = user_digit[0], user_digit[1]
    return int(dig_1) ** int(dig_2)
