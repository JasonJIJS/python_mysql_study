import inspect

from conncection.conncect_study01 import connect, connect_use_config
from conncection.python_mysql_dbconfig import read_db_config


def connect01(): # connect             # connect 에서 alt + enter
    print("\n=={}()==".format(inspect.stack()[0][3]))
    print(inspect.stack()[0])
    connect()


def read_config():
    print("\n=={}()==".format(inspect.stack()[0][3]))
    db = read_db_config()
    print(type(db), db)


def connect02():
    print("\n=={}()==".format(inspect.stack()[0][3]))
    connect_use_config()


if __name__ == "__main__":
    connect01()
    read_config()
    connect02()