from get_data import get_product_data, get_user_data
import psycopg2
from database_config import host, database, user, password


def food_intake():
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=host)
        conn.autocommit = True

        with conn.cursor() as cursor:
            user_data = get_user_data(cursor)
            product_data = get_product_data(cursor)
            cursor.execute(
                """insert into food_intake(user_name, food_name) values (%s, %s)""",
                (user_data, product_data)
            )

    except Exception as _ex:
        print("[Info] Error,", _ex)

    finally:
        conn.close()
        return "[Info] PSQL connection was closed"


print(food_intake())