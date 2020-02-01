from ZODB import FileStorage, DB
import transaction
 
# pip install ZODB

class MyZODB:
    def __init__(self, path):
        self.storage = FileStorage.FileStorage(path) # creating file storage
        self.db = DB(self.storage) # initializing the database
        self.connection = self.db.open() # initializing the connections
        # print 'sss', help(self.connection.root)
        self.dbroot1 = self.connection.root() # connection to store and retreive datas
 
    def close(self):
      self.connection.close()
      self.db.close()
      self.storage.close()


class ZodbOperation:

    def store(self, path):
        db = MyZODB(path)
        # print 'dir', dir(db)
        dbroot = db.dbroot1
        dbroot['a_number'] = 3
        dbroot['a_string'] = 'Gift'
        dbroot['a_list'] = [1, 2, 3, 5, 7, 12]
        dbroot['a_dictionary'] = { 1918: 'Red Sox', 1919: 'Reds' }
        dbroot['deeply_nested'] = {
          1918: [ ('Red Sox', 4), ('Cubs', 2) ],
          1919: [ ('Reds', 5), ('White Sox', 3) ],
          }
        dbroot['auth'] = {'name': 'credo', 'app2': {'username': 'abcde', 'password': '1234'}, 'app1': {'username': 'abcd', 'password': '123'}, 'location': 'chennai'}
        transaction.commit()
        db.close()

    def retreieve(self, path):
        db = MyZODB(path)
        # print help(db.storage)
        dbroot = db.dbroot1
        print 'dbroot', dbroot
        _data = dbroot.keys()
        print(_data)
        # for i in dbroot:
        #   print 'i',dbroot[i]
        # if not _data:
        #   print "No data found!"
        # else:
        #   for k, v in dbroot.items():
        #     print "key", k, "val", v
        db.close()

opr = ZodbOperation()
opr.retreieve('/home/mohideen/Desktop/zodb.fs')