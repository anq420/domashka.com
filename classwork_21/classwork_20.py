import requests
from flask import (Flask, render_template, request, redirect, flash)
from sqlalchemy import (create_engine, MetaData, Table, Integer, String, Column)
from sqlalchemy.orm import Session


app = Flask(__name__)
app.secret_key = 'QwErTyUiOp[123456789010]'


metadata = MetaData()
engine = create_engine('postgresql+psycopg2://anq420:030499@localhost/lesson_20')
ses = Session(bind=engine)

users = Table(
    'users', metadata,

    Column('id', Integer(), primary_key=True),
    Column('name', String(255), nullable=False),
    Column('email', String, nullable=False, unique=True),
    Column('age', Integer, nullable=False)
)
metadata.create_all(engine)


def get_user_info():
    req = requests.get('http://185.225.232.111:8000/user')
    dict_ = req.json()
    ids = [i['id'] for i in dict_]

    user_info = []
    for i in ids:
        response = requests.get(f'http://185.225.232.111:8000/user/{i}')
        certain_user = response.json()
        user_info.append((certain_user.get('name'), certain_user.get('email'), certain_user.get('age')))

    return user_info


def db_request():
    all_users = ses.query(users).all()
    users_ = []
    for user in all_users:
        users_.append(
            {
                'name': user[1],
                'email': user[2],
                'age': user[3]
            }
        )
    return users_


@app.route('/', methods=['GET', 'POST'])
def main():
    all_users = db_request()
    return render_template('database.html', all_users=all_users)


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':

        user_info = get_user_info()

        for user in user_info:
            name, email, age = user
            email_check = ses.query(users).filter_by(email=email).first()

            if not email_check:
                add_user = users.insert().values(name=name, email=email, age=age)
                ses.execute(add_user)
                ses.commit()

    flash('Данные обновлены')

    return redirect('/')


@app.route('/sync', methods=['GET', 'POST'])
def sync():
    ses.query(users).delete()
    ses.commit()

    get_users = get_user_info()

    for user in get_users:
        name, email, age = user
        add_user = users.insert().values(name=name, email=email, age=age)
        ses.execute(add_user)
        ses.commit()
        ses.close()

    flash('Данные синхронизированы')
    return redirect('/')


@app.route('/drop-all', methods=['POST'])
def delete_all():
    ses.query(users).delete()
    ses.commit()
    ses.close()
    flash('Данные из таблицы удалены')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
