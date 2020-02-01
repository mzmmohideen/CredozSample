# -*- coding: utf-8 -*-
# @Author: mzmmohideen
# @Date:   2019-12-01 14:11:52
# @Last Modified by:   mzmmohideen
# @Last Modified time: 2019-12-09 18:39:21

def fib():
	a = 0
	b = 1
	c = int(input("Enter the number of terms "))
	if c == 0:
		print ("Learn numbers")
	elif c == 1:
		print (a)
	elif c == 2:
		print (a,b)
	else:
		print (a,b)
		for i in range(2,c):
			i = a+b
			a = b
			b = i
			print (i)

def fibo(n):
	output = [0,1]
	if n == 0:
		return "Invalid Sequence!"
	elif n == 1:
		return output[0]
	elif n == 2:
		return output
	else:
		for i in range(2, n):
			output.append(output[-1] + output[-2])
	return output

# fibo(10)

def sub(a, b):
	print(a, b)
	return a - b

# print(sub(**{'a':100,'b': 3, 'c':20}))
# print(sub(a=100, b=3, c=20))
# print(sub(*[10, 209, 30]))
# print(sub(10, 209, 30))

def sub(a=1, b=10, *args, **kwargs):
	print(a, b, args, kwargs)

def square(a):
	return (a*a)

print(square(10))

def range(a,b):
	start,step=a,1
	out=[]
	while a<b:
		out.append(a)
	a+=1
	return out

print(range(10,20))		



# print(sub(1,2,3,4))
