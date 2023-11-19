from customexceptions import WrongValue

def summa():
    dig_1 = input('Введите первое число: ')
    if not dig_1.isdigit():
        raise WrongValue
    dig_2 = input('Введите второе число: ')
    if not dig_2.isdigit():
        raise WrongValue
    return float(dig_1) + float(dig_2)

def subtraction():
    dig_1 = input('Введите первое число: ')
    if not dig_1.isdigit():
        raise WrongValue
    dig_2 = input('Введите второе число: ')
    if not dig_2.isdigit():
        raise WrongValue
    return float(dig_1) - float(dig_2)

def multiply():
    dig_1 = input('Введите первое число: ')
    if not dig_1.isdigit():
        raise WrongValue
    dig_2 = input('Введите второе число: ')
    if not dig_2.isdigit():
        raise WrongValue
    return float(dig_1) * float(dig_2)

def devision():
    dig_1 = input('Введите первое число: ')
    if not dig_1.isdigit():
        raise WrongValue
    dig_2 = input('Введите второе число: ')
    if not dig_2.isdigit():
        raise WrongValue
    return float(dig_1) / float(dig_2)

def exponentiation():
    dig_1 = input('Введите первое число: ')
    if not dig_1.isdigit():
        raise WrongValue
    dig_2 = input('Введите второе число: ')
    if not dig_2.isdigit():
        raise WrongValue
    return float(dig_1) ** float(dig_2)