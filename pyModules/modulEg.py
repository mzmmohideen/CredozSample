#! /usr/bin/python3
import os
# import gener
# import gener
# from gener import *
# print dir(A)
# print 'before override', PowTwoGen(5)

def PowTwoGen(n):
	return n

a = 10


def square(n):
	return n*n

# square(5)
# print 'after override', PowTwoGen(5)
# from generator import PowTwoGen

def add():
	return sum([PowTwoGen(10)])

def sub():
	return 5
print(__name__)

# square(5)
# else:
# 	print("I am here")
# if __name__ == "__main__":
# 	# print add()
# 	print("I am Here!")	
# else:
# 	sub()
# 	print("Your in same instance")

# def function():
# 	pass

# b = input("enter your values:").split(' ')
a = ['121', '111', '2', '3', '15', '51']
b = ['31', '12', '4', '5', '32', '121']
aa, bb = 0, 0
a = list(map(int, a))
b = list(map(int, b))
for i in range(len(a)):
    if a[i] > b[i]:
       aa+=1
    else:
       bb+=1
print(aa, bb)