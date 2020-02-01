#! /usr/bin/python2
import psutil
# from itertools import groupby
process = [i.name() for i in psutil.process_iter()]
u_items = set(process)
out = {}
for i in u_items:
	print("Process = %s count = %s"%(i, process.count(i)))

# print out
# print([i.name() for i in psutil.process_iter() if 'skype' in i.name()])

