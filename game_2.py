from random import randint
import sys


def get_range():
    while True:
        try:
            min_count = int(input('Введите минимальное число, которого будут загадываться числа (не меньше 5): '))
            max_count = int(input('Введите максимальное число, до которого будут загадываться числа (не больше 30): '))
            if 5 <= (max_count + 1) - min_count <= 30:
                return min_count, max_count
            else:
                print('Неправильно задан диапазон!')
        except ValueError:
            print('Необходимо вводить цифры!')


def making_digits():
    min_count, max_count = get_range()
    computers_digits = set()
    while len(computers_digits) < 3:
        computers_digits.add(randint(min_count, max_count))
    return computers_digits


def users_digits():
    while True:
        users_digits_list = set()
        try:
            for i in range(3):
                i = input('Введите число: ')
                if i == 'exit':
                    sys.exit()
                else:
                    users_digits_list.add(int(i))
        except ValueError:
            print('Нужно ввести число, если хотите играть, или exit, чтобы выйти из игры.\nВведите значения заново.')
            return users_digits()
        if len(users_digits_list) < 3:
            print('Цифры не могут повторяться!')
        else:
            return users_digits_list


def game():
    machines_digits = making_digits()
    while True:
        common_digits = set(users_digits()).intersection(set(machines_digits))
        if len(common_digits) == 3:
            return 'Вы победили'
        elif len(common_digits) == 0:
            print('Вы ничего не угадали')
        else:
            print(f'Вы проиграли, но угадали {len(common_digits)} число(а)')


print(game())
