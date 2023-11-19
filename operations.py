def summa():
    digit_list = []
    while True:
        try:
            total_digs = int(input('Сколько всего чисел будем складывать?\n'))
            if total_digs <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')     
    while len(digit_list) != total_digs:
        i = input('Введите число, которое будем складывать с другими числами:\n')
        try:
            digit_list.append(float(i))
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    final_count = 0    
    for i in digit_list:
        final_count = final_count + i
    return final_count

def subtraction():
    digit_list = []
    while True:
        try:
            total_digs = int(input('Сколько всего чисел будем использовать в вычитании?\n'))
            if total_digs <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')
    dig_1 = float(input('Введите число, из которого будем вычитать другие числа:\n'))
    while len(digit_list) != total_digs-1:
        i = input('Введите число, которое будем отнимать от предыдущего:\n')
        try:
            digit_list.append(float(i))
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    for i in digit_list:
        dig_1 = dig_1 - i
    return dig_1

def multiply():
    digit_list = []
    while True:
        try:
            total_digs = int(input('Сколько всего чисел будем умножать друг на друга?\n'))
            if total_digs <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')
    while len(digit_list) != total_digs:
        i = input('Введите число, которое будем умножать на другие числа:\n')
        try:
            digit_list.append(float(i))
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    final_count = 1    
    for i in digit_list:
        final_count = final_count * i
    return final_count

def devision():
    digit_list = []
    while True:
        try:
            total_digs = int(input('Сколько всего чисел будем использовать в делении?\n'))
            if total_digs <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')
    dig_1 = float(input('Введите число, которое будем делить на другие числа:\n'))
    while len(digit_list) != total_digs-1:
        i = input('Введите число, на которое будем делить предыдущее:\n')
        try:
            digit_list.append(float(i))
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    try:
        for i in digit_list:
            dig_1 = dig_1 / i
    except ZeroDivisionError:
        return 'На 0 делить нельзя! Ответ - 0.'
    return dig_1

def exponentiation():
    dig_1 = float(input('Введите число, которое будем возводить в степень:\n'))
    dig_2 = float(input('Введите в какую степень будем возводить предыдущее число:\n'))
    result = dig_1 ** dig_2
    return result
