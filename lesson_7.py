from time import time
from random import randint

def time_check(func):
    def calculating_time():
        start_time = time()
        result = func()
        end_time = time()
        return result, f'Вы справились за {int(end_time-start_time)} секунд'
    return calculating_time     

@time_check
def mathematic():
    d1, d2 = randint(0, 1000), randint(0, 1000)
    while True:
        print(f'Сколько будет {d2}-{d1}?')
        user_d = int(input('Введите ваш ответ:\n'))
        if int(d2-d1) == user_d:
            print('Правильно')
            break
        else:
            print('Неправильно')

print(mathematic())
