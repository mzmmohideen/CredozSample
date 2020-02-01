import json


def fileOp():	
	f = open('/home/mohideen/Desktop/pyDocs/pyModules/sample1.txt', 'x')
	f.write("Hi hello")
	# f.close()

	for i in [1,2,3]:
		f.write("\n" + str(i))
	f.close()
	# print dir(f)

	# print(type(f.readlines()))
	# for i in f.readlines():
	# 	print(i)

	# exit()

stuRec = [
	{
		"name": "Student1",
		"age": "10",
		"location": "Chennai"
	},
	{
		"name": "Student2",
		"age": "11",
		"location": "Madurai"
	},
	{
		"name": "Student3",
		"age": "12",
		"location": "Trichy"
	}
]

cond = "json"
#file operations
if cond == "file":
	file = open('/home/mohideen/Desktop/pyDocs/pyModules/sample.json', 'r')
	# print(dir(file))
	print(eval(file.read()))
	# print(len(file.readlines()), len(file.read()))
	# file.write('\nHi hello')
	file.close()


#json
if cond == "json":
	# l = "len('credo')"
	f = open('/home/mohideen/Desktop/pyDocs/pyModules/sample1.json', 'w')
	j = json.dump(str(stuRec), f)
	# print(f)
	# json.load(f, stuRec)
	f.close()
	# print(type(j))