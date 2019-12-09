import pandas as pd
from dml.Fetch_Query import query_with_fetchmany
from dml.coffee_delete import delete_product
from dml.coffee_insert import insert_product, insert_products, insert_sale, insert_sales
from dml.coffee_procedure import call_sale_stat_sp, call_order_price_by_issale
from dml.coffee_select import query_with_fetchone, query_with_fetchall, query_with_fetchall2, \
    query_with_fetchall_by_code
from dml.coffee_update import update_product, update_sale
from dml.connection_pool import ConnectionPool


def connection_pool_test():
    connect_pool = ConnectionPool.get_instance()
    print("connection pool : ", connect_pool)
    connection = connect_pool.get_connection()
    print("connection : ", connection)


def fetchone_test():
    sql_select_product = "select * from product"
    sql_select_sale = "select * from sale"

    query_with_fetchone(sql_select_product)
    query_with_fetchone(sql_select_sale)


def fetchall():
    sql_select_product = "select * from product"
    sql_select_sale = "select * from sale"

    query_with_fetchall(sql_select_product)
    query_with_fetchall(sql_select_sale)


def fetchall2():
    sql_select_product = "select * from product"
    sql_select_sale = "select * from sale"

    res = query_with_fetchall2(sql_select_product)
    print(type(res), 'size = ', len(res))
    for pno, pname in res:
        print(pno, pname)

    res = query_with_fetchall2(sql_select_sale)
    print(type(res), 'size = ', len(res))
    for no, code, price, saleCnt, marginRate in res:
        print(no, code, price, saleCnt, marginRate)

    product_select_where01 = "select * from product where code = %s"
    res = query_with_fetchall_by_code(product_select_where01, 'A001')
    print(res)                                          # 매개변수를 넣어줘서 만듦
    product_select_where02 = "select * from product where code = '{}'".format('A001')
    query_with_fetchall(product_select_where02)         # 문장 자체를 만들어서

    product_select_where01 = "select * from sale where code = %s"
    res = query_with_fetchall_by_code(product_select_where01, 'A001')
    print(res)
    product_select_where02 = "select * from sale where code = '{}'".format('A001')
    query_with_fetchall(product_select_where02)


def fetchmany_insert():
    sql_select_product = "select * from product"
    sql_select_sale = "select * from sale"

    query_with_fetchmany(sql_select_product)
    query_with_fetchmany(sql_select_sale)


def fetchone_insert():
    sql_select_product = "select * from product"
    sql_select_sale = "select * from sale"
    sql_insert_product = "insert into product values(%s, %s)"
    sql_insert_sale = "insert into sale values(%s, %s, %s, %s, %s)"


    query_with_fetchall(sql_select_product)         # insert a row into product table
    insert_product(sql_insert_product, 'C001', '라떼')
    query_with_fetchall(sql_select_product)
    products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼3')]
    insert_products(sql_insert_product, products)   # insert rows into product table
    query_with_fetchall(sql_select_product)

    query_with_fetchall(sql_select_sale)         # insert a row into product table
    insert_sale(sql_insert_sale, 5, 'C001', 4000, 100, 10)
    query_with_fetchall(sql_select_sale)
    sales = [(6, 'C002', 4000, 100, 10), (7, 'C003', 5000, 100, 10), (8, 'C004', 6000, 100, 10)]
    insert_sales(sql_insert_sale, sales)   # insert rows into product table
    query_with_fetchall(sql_select_sale)



def fetchone_update():
    sql_select_by_code = "select code, name from product where code = '{code}'".format(code='C001')
    query_with_fetchone(sql_select_by_code)
    update_sql = "update product set name = %s where code = %s"
    update_product(update_sql, '라떼', 'C001')
    query_with_fetchone(sql_select_by_code)

    sql_select_by_code = "select * from sale where code = '{code}'".format(code='C001')
    query_with_fetchone(sql_select_by_code)
    # update_sql = "update sale set no = %d, price = %d, saleCnt = %d, marginRate = %d where code = %s".format(5, 4444, 111, 11, 'C001')
    update_sql = "update sale set no = {}, price = {}, saleCnt = {}, marginRate = {} where code = '{}'".format(5, 4444,
                                                                                                             111, 11,
                                                                                                             'C001')
    update_sale(update_sql, 5, 4444, 111, 11, 'C001')

    query_with_fetchone(sql_select_by_code)

    # sale(no, code, price, saleCnt, marginRate)
    # update_sale(sql, no, code, price, saleCnt, marginRate)

def fetchone_delete():
    sql_select_product_1 = "select code, name from product where code like 'C___'"
    res = query_with_fetchall2(sql_select_product_1)
    columns_list = ['code', 'name']
    df = pd.DataFrame(res, columns=columns_list)
    print(df)
    sql_delete_product = "delete from product where code = %s"
    delete_product(sql_delete_product, 'C004')
    for code, name in (query_with_fetchall2(sql_select_product_1)):
        print(code, " ", name)


if __name__ == "__main__":

    # ctrl + alt + m : extract Method / main을 줄이자
    connection_pool_test()
    # fetchone_test()
    # fetchall()
    # fetchall2()
    # fetchmany_insert()

    # fetchone_insert()
    # fetchone_update()
    # fetchone_delete()
    # transaction_fail1()
    # transaction_fail2()
    # transaction_success()
    # create_procedure()
    call_sale_stat_sp('proc_sale_stat')
    print()
    call_order_price_by_issale('proc_saledetail_orderby', False)
    print()
    call_order_price_by_issale('proc_saledetail_orderby', True)
