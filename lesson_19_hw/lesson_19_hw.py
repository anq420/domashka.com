from flask import (Flask, render_template, request, flash)
from sqlalchemy import (create_engine, MetaData, Table, Integer, String, Column, CheckConstraint)
from sqlalchemy.orm import Session


app = Flask(__name__)
app.secret_key = 'QwErTyUiOp[123456789010]'

metadata = MetaData()
engine = create_engine('postgresql+psycopg2://anq420:030499@localhost/lesson_19_hw_contract_first')
ses = Session(bind=engine)


users = Table(
    'users', metadata,

    Column('id', Integer(), primary_key=True),
    Column('email', String(255), nullable=False, unique=True),
    Column('password', String, nullable=False),
    Column('nickname', String(255), nullable=False, unique=True),
    CheckConstraint("email LIKE '%@%' AND LOWER(email) = email", name='email_format_check')
)
metadata.create_all(engine)


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

        user_info = email, password
        all_users = [(i[1], i[2]) for i in ses.query(users).all()]

        for user in all_users:
            if user == user_info:
                return f'Welcome back, {email}'

            if user[0] != email:
                flash('It seems you have no account here. You need to make an account first.')

            if user[0] == email and user[1] != password:
                flash('It seems you entered your password incorrectly')

    return f'''{render_template('login.html')}<p>{main}</p>'''


@app.route('/sign-up', methods=['POST', 'GET'])
def create_account():
    main = '<a href="/">MAIN PAGE</a>'
    if request.method == 'POST':
        ses = Session(bind=engine)

        check_email = [i[1] for i in ses.query(users).all()]
        check_nickname = [i[3] for i in ses.query(users).all()]

        email = request.form['email']
        password = request.form['password']
        password_2 = request.form['password_2']
        nickname = request.form['nickname']

        if password == password_2 and email not in check_email and nickname not in check_nickname:
            try:
                new_account = users.insert().values(email=email, password=password, nickname=nickname)
                ses.execute(new_account)
                ses.commit()
                ses.close()
                return f'''<h1>Registered successfully</h1><p>{main}</p>'''
            except Exception:
                flash('You need to use an email to register an account')

        if password != password_2:
            flash('It seems you have entered incorrect password')

        if email in check_email:
            flash(f'This email is already used. You can login into it.')

        if nickname in check_nickname:
            flash('This nickname is already used')

    return f'''{render_template('index_1.html')}<p>{main}</p>'''


if __name__ == '__main__':
    app.run(debug=True)
