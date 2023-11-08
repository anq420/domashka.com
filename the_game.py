from random import randint
import sys


def game():
    while True:
        min_count = int(input('Введите минимальное число, которого будут загадываться числа (не меньше 5): '))
        max_count = int(input('Введите максимальное число, до которого будут загадываться числа (не больше 30): '))
        if 5 <= (max_count + 1) - min_count <= 30:
            break
        else:
            print('Неправильно задан диапазон')
    
    def making_digits():
        computers_digits = set()
        while len(computers_digits) < 3:
            a = randint (min_count, max_count)
            computers_digits.add(a)
        print (f'Я загадал кое-какие числа {computers_digits}. Угадаешь какие?') #вывожу здесь список для проверки того, что "загадывает" комп - можно выбросить строку
        return computers_digits
    
    def users_digits():
        while True:
            users_digits_list = set()
            for i in range(3):
                i = input('Введите число: ')
                if i == 'exit':
                    sys.exit()
                else:
                    users_digits_list.add(int(i))
            if len(users_digits_list) < 3:
                print('Значения не могут повторяться. Попробуйте ввести заново разные значения!')
            else:
                break
        return users_digits_list
    
    def check():
        machines_digits = making_digits()
        while True:
            common_digits = set(users_digits()).intersection(set(machines_digits))
            if len(common_digits) == 3:
                print('Вы победили')
                break
            elif len(common_digits) == 0:
                print(f'Вы ничего не угадали')
            else:
                print(f'Вы проиграли, но угадали {len(common_digits)} число(а)')
        return f'Загаданные мной числа - {common_digits}' #просто так вывожу список "загаданных" компом чисел, чтобы не возвращалось None

    return check()

print(game())
