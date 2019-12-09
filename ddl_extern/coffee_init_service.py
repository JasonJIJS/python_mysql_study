from mysql.connector import Error, errorcode

from connection_pool.connection_pool_study02 import ExplicitlyConnectionPool
from ddl_extern.read_ddl import read_ddl_file


class DbInit:
    def __init__(self):
        self._db = read_ddl_file()


    def __create_database(self):
        try:
            sql = read_ddl_file()
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self._db['database_name']))
            print("CREATE DATABASE {}".format(self._db['database_name']))
        except Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                cursor.execute("DROP DATABASE {} ".format(self._db['database_name']))
                print("DROP DATABASE {}".format(self._db['database_name']))
                cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self._db['database_name']))
                print("CREATE DATABASE {}".format(self._db['database_name']))
            else:
                print(err.msg)
        finally:
            cursor.close()
            conn.close()


    def __create_table(self):
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("USE {}".format(self._db['database_name']))
            for table_name, table_sql in self._db['sql'].items():
                try:
                    print("Creating table {}:".format(table_name), end='')
                    cursor.execute(table_sql)
                except Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print("already exists.")
                    else:
                        print(err.msg)
                else:
                    print("OK")
        except Error as err:
            print(err)
        finally:
            cursor.close()
            conn.close()


    def __create_trigger(self):
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("USE {}".format(self._db['database_name']))
            for trigger_name, trigger_sql in self._db['trigger'].items():
                try:
                    print("Creating trigger {}:".format(trigger_name), end='')
                    cursor.execute(trigger_sql)
                except Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print("already exists.")
                    else:
                        print(err.msg)
                else:
                    print("OK")

        except Error as err:
            print(err)
        finally:
            cursor.close()
            conn.close()


    def __create_procedure(self):
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("USE {}".format(self._db['database_name']))
            for procedure_name, procedure_sql in self._db['procedure'].items():
                try:
                    print("Creating procedure {}:".format(procedure_name), end='')
                    cursor.execute(procedure_sql)
                except Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print("already exists.")
                    else:
                        print(err.msg)
                else:
                    print("OK")

        except Error as err:
            print(err)
        finally:
            cursor.close()
            conn.close()


    def __sql_select(self):
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("USE {}".format(self._db['database_name']))
            for sql_select_name, sql_select_sql in self._db['sql_select'].items():
                try:
                    print("Creating sql_select {}:".format(sql_select_name), end='')
                    cursor.execute(sql_select_sql)
                except Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print("already exists.")
                    else:
                        print(err.msg)
                else:
                    print("OK")
                    print(sql_select_sql)
        except Error as err:
            print(err)
        finally:
            cursor.close()
            conn.close()



    def __create_user(self):
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            print("Creating user: ", end='')
            cursor.execute(self._db['user_sql'])
            print("OK")
        except Error as err:
            print(err)
        finally:
            cursor.close()
            conn.close()

    def service(self):
        # self.__create_database()
        # self.__create_table()
        self.__create_trigger()
        # self.__create_procedure()
        # self.__sql_select()
        # self.__create_user()


