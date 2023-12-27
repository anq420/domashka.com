from flask import (Flask, render_template, request, jsonify, flash)
from sqlalchemy import (create_engine, MetaData, Table, Integer, String, Column, CheckConstraint)
from sqlalchemy.orm import registry, Session
import bcrypt


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


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)



@app.route('/')
def get_main_page():
    sign_in = '<a href="/sign-in">SIGN IN</a>'
    sign_up = '<a href="/sign-up">SIGN UP</a>'
    return f'''<h1>Добро пожаловать на сервер ШИЗОФРЕНИЯ!</h1><p>If you already have account - you can {sign_in}</p>
    <p>If you do not have account - you can {sign_up}</p>'''


@app.route('/sign-in', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        ses = Session(bind=engine)

        email = request.form['email']
        password = request.form['password']

        user_data = ses.query(users).filter(users.c.email == email).first()

        if user_data and check_password(password, hash_password(password)):
            return f'Welcome back, {email}'
        else:
            return f'Something went wrong'

    return render_template('login.html')


@app.route('/sign-up', methods=['POST', 'GET'])
def create_account():
    if request.method == 'POST':
        ses = Session(bind=engine)

        check_email = [i[1] for i in ses.query(users).all()]
        check_nickname = [i[3] for i in ses.query(users).all()]

        email = request.form['email']
        password = request.form['password']
        password_2 = request.form['password_2']
        nickname = request.form['nickname']

        if password == password_2 and email not in check_email and nickname not in check_nickname:
            hashed_password = hash_password(password)
            try:
                new_account = users.insert().values(email=email, password=hashed_password, nickname=nickname)
                ses.execute(new_account)
                ses.commit()
                ses.close()
                return 'Registered successfully'
            except Exception:
                flash('You need to use an email to register an account')

        if password != password_2:
            flash('It seems you have entered incorrect password')

        if email in check_email:
            flash(f'This email is already used. You can login into it.')

        if nickname in check_nickname:
            flash('This nickname is already used')

    return render_template('index_1.html')


if __name__ == '__main__':
    app.run(debug=True)
