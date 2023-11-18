from operations import summa, vichitanie, delenie, umnozhenie, stepen

def calculator():
    while True:
        users_choice = input('Доступные операции:\n-Сложение\n-Вычитание\n-Умножение\n-Деление\n-Возведение в степень. Напишите название операции, чтобы её выполнить.\n')
        if users_choice in ['Сложение', 'сложение']:
            return summa()
        if users_choice in ['Вычитание', 'вычитание']:
            return vichitanie()
        if users_choice in ['Умножение', 'умножение']:
            return umnozhenie()
        if users_choice in ['Деление', 'деление']:
            return delenie()
        if users_choice in ['Возведение в степень', 'возведение в сепень']:
            return stepen()
        else:
            print('Необходимо ввести название операции!')

print(calculator())