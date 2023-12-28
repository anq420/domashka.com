from flask import (Flask, render_template, request, flash)
from making_db import engine, users
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from password_actions import hash_password, check_password


app = Flask(__name__)
app.secret_key = 'QwErTyUiOp[123456789010]'


@app.route('/')
def get_main_page():
    sign_in = '<a href="/sign-in">SIGN IN</a>'
    sign_up = '<a href="/sign-up">SIGN UP</a>'
    return f'''<h1>Hello there!</h1><p>If you already have account - you can {sign_in}</p>
    <p>If you do not have account - you can {sign_up}</p>'''


@app.route('/sign-in', methods=['POST', 'GET'])
def login():
    main = '<a href="/">MAIN PAGE</a>'
    if request.method == 'POST':
        ses = Session(bind=engine)

        email = request.form['email']
        password = request.form['password']

        user = ses.query(users).filter_by(email=email).first()

        if user:
            user_pass = user.password
            checked = check_password(password, user_pass)
            if checked:
                return f'Welcome back, {email}'

        if user:
            user_pass = user.password
            checked = check_password(password, user_pass)
            if not checked:
                flash('It seems you have entered your password incorrectly')

        if not user:
            flash('Oops! We could not find such email. Maybe you have no account here?')

    return f'''{render_template('login.html')}<p>{main}</p>'''


@app.route('/sign-up', methods=['POST', 'GET'])
def create_account():
    main = '<a href="/">MAIN PAGE</a>'
    if request.method == 'POST':
        ses = Session(bind=engine)

        email = request.form['email']
        password = request.form['password']
        password_2 = request.form['password_2']
        nickname = request.form['nickname']

        check_email = ses.query(users).filter_by(email=email).first()
        check_nickname = ses.query(users).filter_by(nickname=nickname).first()

        if password == password_2 and check_email is None and check_nickname is None:
            try:
                password_hashed = hash_password(password)
                new_account = users.insert().values(email=email, password=password_hashed, nickname=nickname)
                ses.execute(new_account)
                ses.commit()
                ses.close()
                return f'''<h1>Registered successfully</h1><p>{main}</p>'''
            except IntegrityError:
                ses.rollback()
                flash('You need to use an email to register an account')

        if password != password_2:
            flash('It seems you have entered incorrect password')

        if check_nickname:
            flash('Nickname is already in use')

        if check_email:
            flash('Email is already in use')

    return f'''{render_template('index_1.html')}<p>{main}</p>'''


if __name__ == '__main__':
    app.run(debug=True)
