from ddl_extern.backup_restore_tc import BackupRestore
from ddl_extern.coffee_init_service import DbInit
from ddl_extern.read_ddl import read_ddl_file


def read_ddl_file_test():
    db = read_ddl_file()
    #print(db)
    for key, value in db.items():
        if key != 'sql':
            print("[{}] = {}".format(key, value))
        else:
            print("[{}]".format(key))
            for k, v in value.items():
                print("\t[{}]\n\t\t{}".format(k, v))


if __name__ == "__main__":
    read_ddl_file_test()
    db = DbInit()
    db.service()

    # backup_restore = BackupRestore()
    # backup_restore.data_backup('product')
    # backup_restore.data_backup('sale')
    # backup_restore.data_restore('product')
    # backup_restore.data_restore('sale')




