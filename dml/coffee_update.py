from mysql.connector import Error

from dml.connection_pool import ConnectionPool


def update_product(sql, name, code):
    args = (name, code)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


def update_sale(sql, no, price, saleCnt, marginRate, updatecode):
    args = (no, price, saleCnt, marginRate, updatecode)
    # print(args)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        # cursor.execute(sql, args)
        cursor.execute(sql)
        conn.commit()
    except Error as error:
        print("err", error)
    finally:
        cursor.close()
        conn.close()

# sale(no, code, price, saleCnt, marginRate)