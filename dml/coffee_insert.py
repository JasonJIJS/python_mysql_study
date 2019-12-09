from mysql.connector import Error
from dml.connection_pool import ConnectionPool


def insert_product(sql, code, name):            # insert a row into product table
    args = (code, name)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def insert_sale(sql, no, code, price, saleCnt, marginRate):
    args = (no, code, price, saleCnt, marginRate)   # insert a row into sale table
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def insert_products(sql, products):            # insert rows into product table
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, products)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def insert_sales(sql, sales):            # insert rows into sale table
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, sales)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


