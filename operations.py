def summa():
    spisok = []
    while True:
        try:
            a = int(input('Сколько всего чисел будем складывать?\n'))
            if a <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')     
    while len(spisok) != a:
        i = input('Введите число, которое будем складывать с другими числами:\n')
        try:
            spisok.append(float(i))
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    final_count = 0    
    for i in spisok:
        final_count = final_count + i
    return final_count

def vichitanie():
    spisok = []
    while True:
        try:
            a = int(input('Сколько всего чисел будем использовать в вычитании?\n'))
            if a <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')
    dig_1 = float(input('Введите число, из которого будем вычитать другие числа:\n'))
    while len(spisok) != a-1:
        i = input('Введите число, которое будем отнимать от предыдущего:\n')
        try:
            spisok.append(float(i))
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    for i in spisok:
        dig_1 = dig_1 - i
    return dig_1

def umnozhenie():
    spisok = []
    while True:
        try:
            a = int(input('Сколько всего чисел будем умножать друг на друга?\n'))
            if a <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')
    while len(spisok) != a:
        i = input('Введите число, которое будем умножать на другие числа:\n')
        try:
            spisok.append(float(i))
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    final_count = 1    
    for i in spisok:
        final_count = final_count * i
    return final_count

def delenie():
    spisok = []
    while True:
        try:
            a = int(input('Сколько всего чисел будем использовать в делении?\n'))
            if a <= 1:
                print('Для работы функции нужно хотя бы два числа!')
            break
        except ValueError:
            print('Ошибка! Ответ необходимо ввести числом! Например, 5!\nПопробуйте заново!')
    dig_1 = float(input('Введите число, которое будем делить на другие числа:\n'))
    while len(spisok) != a-1:
        i = input('Введите число, на которое будем делить предыдущее:\n')
        try:
            spisok.append(float(i))
        except ValueError:
            print('Ошибка! Попробуйте заново!')
    try:
        for i in spisok:
            dig_1 = dig_1 / i
    except ZeroDivisionError:
        return 'На 0 делить нельзя! Ответ - 0.'
    return dig_1

def stepen():
    dig_1 = float(input('Введите число, которое будем возводить в степень:\n'))
    dig_2 = float(input('Введите в какую степень будем возводить предыдущее число:\n'))
    result = dig_1 ** dig_2
    return result
