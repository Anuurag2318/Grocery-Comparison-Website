import sqlite3


def getAllRows():
    min_prod = {}
    try:
        connection = sqlite3.connect('../db.sqlite3')
        cursor = connection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from products_product"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            l1 = row[3:6]
            prod = row[1]
            min_val = min(l1)
            min_prod[prod] = min_val
            cursor.execute("""UPDATE products_product 
                         SET best_price = ?
                         WHERE name = ?""", (min_val, prod))
        print(min_prod)
        cursor.close()
        return min_prod


    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if connection:
            connection.close()
            print("The Sqlite connection is closed")


def get_best_price_all():
    return getAllRows()
get_best_price_all()