from getters import get_email, get_password
from validators import check_data

current_users = [{'email': 'anq1@gmail.com', 'password': '12345'}, {'email': 'anq2@gmail.com', 'password': '54321'}]

def app():
    while True:
        email = get_email()
        if email in ['EXIT', 'exit', 'Exit']:
            print ('Goodbye!')
            break
        password = get_password()
        if check_data(email, password, current_users):
            print(f'Hello, dear {email}')
            break
        else:
            print('Oops! An error occured!')


app()
