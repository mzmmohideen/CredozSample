import xlrd
import psutil
import csv

def readfromXL():
	f = xlrd.open_workbook('/home/mohideen/Desktop/sample.xlsx')
	# print(dir(f))
	sh = f.sheet_by_name('Sheet2')
	# for i in sh.get_rows():
	# 	print(i)
	header = sh.row_values(0)
	print('header', header)
	# for i in range(1, sh.nrows):
	# 	print(sh.row_values(i))
	out = []
	for i in range(1, sh.nrows):
		print(sh.row_values(i))
		out.append(dict(zip(header, sh.row_values(i))))

	print(out)


def processCount():
	proc = [i.name() for i in psutil.process_iter()]
	return {i: proc.count(i) for i in set(proc)}

def csvWriter():
	f = open('processCount.csv', 'w')
	writer = csv.writer(f)
	writer.writerow(('Process Name', 'Count'))
	out = processCount()
	for i in out.items():
		writer.writerow(i)
	f.close()
	return "Successfull!"

print(readfromXL())
