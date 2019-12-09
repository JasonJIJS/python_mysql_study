import os

from dml.coffee_select import query_with_fetchall
from dml_ddl_blob.blob_query import insert_blob, read_blob, update_blob, delete_blob
from dml_ddl_blob.blob_read_write import read_file_blob
from dml_ddl_blob.connection_pool_blob import ConnectionPool
from dml_ddl_blob.create_table_blob import create_table

if __name__ == "__main__":
    # create_table()
    # print(os.getcwd())
    # conn = ConnectionPool.get_instance().get_connection()
    # print(conn)

    create_table()
    data = read_file_blob('img/python-logo.png')
    print(type(data))

    insert_query = "insert into images(name, pic) values(%s, %s)"
    update_query = "update images set name=%s, pic=%s where no=%s"
    read_query = "select pic from images where no=%s"
    delete_query = "delete from images where no=%s"
    select_query = "select no, name from images"

    insert_blob(insert_query, 'python-logo', 'img/python-logo.png')
    insert_blob(insert_query, 'google-logo', 'img/google-logo.png')
    query_with_fetchall(select_query)
    print()

    read_blob(read_query, 1, 'img/read-python.png')
    read_blob(read_query, 2, 'img/read-google.png')

    update_blob(update_query, 'pycharm-logo', 'img/pycharm-logo.png', 1)
    query_with_fetchall(select_query)
    print()
    read_blob(read_query, 1, 'img/read-pycharm.png')

    delete_blob(delete_query, 1)
    query_with_fetchall(select_query)


