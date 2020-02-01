import csv
import json

def writeintoCSV():
	_data = eval(json.load(open("/home/mohideen/Desktop/pyDocs/pyModules/sample1.json")))
	header = _data[0].keys()
	_csv = open("sample.csv", 'w')
	csv_writer = csv.writer(_csv)
	csv_writer.writerow(header)
	for i in _data:
		csv_writer.writerow(i.values())
	_csv.close()
	return True

def readFromCSV(path):
	_f = open(path)
	csv_reader = csv.reader(_f)	
	# _data = list(csv_reader)
	out = []
	# print(list(csv_reader))
	# exit()
	header = csv_reader.next()
	for i in csv_reader:
		# print(zip(header, i))
		out.append(dict(zip(header, i)))
		# if i == 0:
		# 	header = j
		# print('i', i)
	print(out)


readFromCSV("/home/mohideen/Desktop/pyDocs/pyModules/sample.csv")
