from customexceptions import WrongValue


def user_digit_amount():
    while True:
        try:
            total_digs = int(input('Сколько всего чисел в операции?\n'))
            if total_digs <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            else:
                break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')
    return total_digs

def get_numbers(total_digs):
    digit_list = []   
    while len(digit_list) != total_digs:
        i = input('Введите число:\n')
        is_digit = all((i.isdigit() or i == '.' for i in i))
        try:
            digit_list.append(float(i))
            if not is_digit:
                raise WrongValue
        except WrongValue:
            print('Ошибка! Попробуйте заново!')
    return digit_list

def get_numbers_2(total_digs):
    digit_list = []
    while len(digit_list) != total_digs-1:
        i = input('Введите число:\n')
        is_digit = all((i.isdigit() or i == '.' for i in i))
        try:
            digit_list.append(float(i))
            if not is_digit:
                raise WrongValue
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    return digit_list

def summa():
    digit_list = get_numbers(user_digit_amount())
    final_count = 0  
    for i in digit_list:
        final_count = final_count + i
    return final_count

def subtraction():
    digs_amount = user_digit_amount()
    dig_1 = float(input('Введите число, из которого будем вычитать:\n'))
    digit_list = get_numbers_2(digs_amount)
    for i in digit_list:
        dig_1 = dig_1 - i
    return dig_1

def multiply():
    digit_list = get_numbers(user_digit_amount())
    final_count = 1    
    for i in digit_list:
        final_count = final_count * i
    return final_count

def devision():
    digs_amount = user_digit_amount()
    dig_1 = float(input('Введите число, которое будем делить на другие числа:\n'))
    digit_list = get_numbers_2(digs_amount)
    try:
        for i in digit_list:
            dig_1 = dig_1 / i
    except ZeroDivisionError:
        return 'На 0 делить нельзя! Ответ - 0.'
    return dig_1

def exponentiation():
    while True:
        try:
            dig_1 = input('Введите число:\n')
            is_digit = all((i.isdigit() or i == '.' for i in dig_1))
            if not is_digit:
                raise WrongValue
            dig_2 = input('Введите степень:\n')
            is_digit = all((i.isdigit() or i == '.' for i in dig_2))
            if not is_digit:
                raise WrongValue 
            return float(dig_1) ** float(dig_2)
        except WrongValue:
            print('Нужно вводить только числа с точкой')
