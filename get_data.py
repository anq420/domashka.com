import psycopg2
from database_config import host, database, user, password


def get_user_data(cursor):
    user_input = input('Enter your full name:\n')
    cursor.execute(
        f"""insert into users(name) values ('{user_input}') returning name"""
    )
    return cursor.fetchone()[0]


def get_product_data(cursor):
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host)
        conn.autocommit = True

        cursor.execute(
            """SELECT product_name from product"""
        )

        all_products = cursor.fetchall()
        unbox_products = [i[0] for i in all_products]

        product_info = 'name', 'fats (100gr)', 'carbohydrates (100gr)', 'protein (100gr)'
        user_input = [input(f'Enter product {i}:\n').lower() for i in product_info]

        if user_input[0] in unbox_products:
            return user_input[0]

        if user_input[0] not in unbox_products:
            cursor.execute(
                """insert into product(
                product_name, fats_100gr, carbohydrates_100gr, protein_100gr) values (%s, %s, %s, %s)
                returning product_name""",
                (user_input[0], user_input[1], user_input[2], user_input[3])
            )
            print("[Info] Data was successfully inserted")
            return cursor.fetchone()[0]

    except Exception as _ex:
        print("[Info] Error,", _ex)
