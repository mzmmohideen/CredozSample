import MySQLdb #this going to create a bridge between python and mysql
#pip install MySQL-python
# pip install mysqlclient
import pickle
import shelve

class moveData(object):

    def db_conn(self):

        _db = "sample_db"
        _host = "127.0.0.1"
        _tableName = ""
        self.conn = MySQLdb.connect(host=_host, port=3306, user="root", passwd="mohideen", db=_db)
        self.curr = self.conn.cursor()
    
    def db_createTable(self):
        self.db_conn()
        self.curr.execute("CREATE TABLE employee_2020 (name VARCHAR(255), address VARCHAR(255))")
        self.curr.close()

    def db_insert(self): 
        self.db_conn()
        _data = [
            {
                "name": "sudharsan", "address": "chennai"
            },
            {
                "name": "ramesh", "address": "chennai"
            },
            {
                "name": "catherine", "address": "chennai"
            }
            # {
            #     "name": "jambu", "address": "chennai"
            # },
            # {
            #     "name": "malola krishnan", "address": "chennai"
            # },
            # {
            #     "name": "balaji", "address": "chennai"
            # },
            # {
            #     "name": "pramil", "address": "chennai"
            # },
            # {
            #     "name": "vasupradha", "address": "chennai"
            # }
        ]
        for i in _data:
            query = "insert into sample_db.employee_2020 (name, address) values ('{name}', '{address}')".format(**i)
            print('query', query)
            self.curr.execute(query) #pass sql queries
            self.conn.commit()
        self.curr.close()
        # print 'query', query
        # self.curr.execute(query)
        # self.curr.close()
        # self.conn.commit()

    def db_read(self):
        self.db_conn()
        self.curr.execute("select * from employee order by id desc limit 3")
        print(self.curr.description)
        header = [i[0] for i in self.curr.description]
        print(header)
        # print(self.curr.fetchall())
        # out = []
        # for i in self.curr.fetchall():
        #     print 'i', dict(zip(header, i))
        print [dict(zip(header, i)) for i in self.curr.fetchall()]


def pickleEg():
    print 'started'
    variety = ["sweet", "box", "cat"]
    shape = ["back","spear", "log"]
    sam = dict(zip(variety, shape))
    pickleFile = open("/home/mohideen/Desktop/pickle.txt", 'w')
    # pickle.dump(variety, pickleFile)
    # pickle.dump(shape, pickleFile)
    # pickle.dump(sam, pickleFile)
    for i in [variety, shape, sam]:
        pickle.dump(i, pickleFile)
    # h = pickle.dumps(variety)
    # print 'h', h
    pickleFile.close()

# pickleEg()


def pickleLoad():
    pickleFile = open("/home/mohideen/Desktop/pickle.txt", 'r')
    # l = pickle.load(pickleFile)
    # print 'l from a file ', l
    print pickle.load(pickleFile)
    print pickle.load(pickleFile)
    print pickle.load(pickleFile)
    # variety = ["sweet", "box", "cat"]
    # h = pickle.dumps(variety)
    # print 'd', h
    # print 'l', pickle.loads(h)


# def shelveEg():
#     d = shelve.open("shelveSample.dbm")
#     >>> d['student1'] = 'ponnuswamy'
# >>> d['student2'] = 'sugumar'
# >>> d
# {'student2': 'sugumar', 'student1': 'ponnuswamy', 'name': 'ponnuswamy'}
# >>> del d['name']
# >>> d
# {'student2': 'sugumar', 'student1': 'ponnuswamy'}
# >>> d.close()


def zodb():
    storage = ZODB.FileStorage.FileStorage('mydata.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# 
# mydb.commit()


if __name__ == "__main__":
    # pickleLoad()
    w = moveData()
    # w.db_createTable()
    # w.db_insert()
    w.db_read()
    # pickleEg()
    # pickleLoad()