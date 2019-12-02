from configparser import ConfigParser


def read_db_config(filename = "Config.ini", section = "mysql"):
    parser: ConfigParser = ConfigParser()
    parser.read(filename)

    db  = {} # 딕셔너리 만들어 주고
    if parser.has_section(section):
        for item in parser.items(section):
            db[item[0]] = item[1]

    else:
        raise Exception('{} not found in the {} file'.format(section, filename) ) # 예외만들어 던지는 throw랑 비슷

    return db
