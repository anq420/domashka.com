import json

with open('all_users.json', 'r') as j_file:
    all_users = json.load(j_file)


def get_name():
    return input('Enter your email or nickname:\n')


def get_password():
    return input('Enter your password:\n')


def password_confirmation():
    password_1 = get_password()
    password_2 = input('Confirm your password:\n')
    while True:
        if password_1 == password_2:
            return password_2
        else:
            print("It seems you've entered incorrect data. Try again!")
            password_1 = get_password()
            password_2 = input('Confirm your password:\n')


def reg_check_name():
    while True:
        name = get_name()
        for i in all_users:
            if i['email'] == name:
                print('This name is already used')
                break
        else:
            return name


def login():
    while True:
        name, password = get_name(), get_password()
        for i in all_users:
            if i['email'] == name and i['password'] == password:
                return f'Hello, {name}'
        else:
            print("It seems you've entered incorrect data. Try again!")


def registration():
    while True:
        name = reg_check_name()
        password = password_confirmation()
        if name and password:
            new_user = {'email': name, 'password': password}
            all_users.append(new_user)
            with open('all_users.json', 'w') as file:
                json.dump(all_users, file)
            return 'Registration is over.'
        else:
            print("It seems you've entered something wrong. Try again!")


def login_register():
    while True:
        user_choice = input('What would you like to do: register or login?\n').lower
        if user_choice in 'register':
            return registration()
        if user_choice in 'login':
            return login()
        else:
            print('You need to choose: to login or to register!')


print(login_register())
