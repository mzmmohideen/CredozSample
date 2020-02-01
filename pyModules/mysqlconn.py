import MySQLdb

# print help(MySQLdb.connect)
conn = MySQLdb.connect(host="", port=3306, user="root", passwd="mohideen", db="sample_db")
# print 'conn', dir(conn)
cursor = conn.cursor()

# cursor.execute("select * from employee")
# # print cursor.fetchall()
# header = [i[0] for i in cursor.description]
# print header
# out = []
# for i in cursor.fetchall():
# 	out.append(dict(zip(header, i)))
# print out


def db_insert():
    for i in [('Vishwa', 'south'), ('veera', 'chennai')]:
	    query = "insert into employee (name, address) values ('{}', '{}')".format(*i)
	    print 'query', query
	    cursor.execute(query)
	    # print dir(cursor)
	    # print cursor.rownumber, cursor.rowcount, cursor.lastrowid
	    # cursor.close()
	    conn.commit()
	    # break
	    # self.conn.commit()

def db_select():
	print("1")
	cursor.execute("select * from employee")
	# print list(cursor.description)
	header = [i[0] for i in cursor.description]
	# print header
	out = []
	# print(list(cursor.fetchall()))
	for i in cursor.fetchall():
		out.append(dict(zip(header, i)))
	return out
# db_insert()
a = db_insert()
print('out', a)
