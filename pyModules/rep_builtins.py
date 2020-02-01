# -*- coding: utf-8 -*-
# @Author: mzmmohideen
# @Date:   2019-11-27 08:41:37
# @Last Modified by:   mzmmohideen
# @Last Modified time: 2019-11-27 09:50:09
def map(a,b):
	print(a)
	out = []
	for i in b:
		out.append(a(i))
	return out	
# print(map(lambda x:x*x,range(10)))

def r(w):
	out = w*w
	print(out)
	return out
# print(map(r,range(10)))

	

def reduce(a,b):
	# b = list(b)
	out = a(b[0], b[1])
	# out = a(b.__next__(), b.__next__())
	for i in b[2:]:
		out = a(out, i)		
	return out

# print(reduce(lambda a,b:a+b, ['a', 'b', 'c', 'd', 'e']))


def sumofchar(a,b):
	out = a+b
	print(out)
	return out

print('output', reduce(sumofchar, range(10)))

def filter(a,b):
	# out = []
	for i in b:
		if a(i):
			# out.append(i)
			yield i
# print(list(filter(lambda X:X%2,range(10))))