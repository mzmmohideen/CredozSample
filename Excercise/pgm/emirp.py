"""
	__author__ = "mohideen"
	__created__ = "2019-11-05"
	__lastupdated__ = "2019-11-05"
"""
from __future__ import print_function

def isprime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


def findEmirp(count):
	a = 1
	emirp = []
	while a:
		rev = int(str(a)[::-1])
		if isprime(a) and rev != a and isprime(rev):
			# print("It is emirp", a)
			emirp.append(a)
		a+=1
		if len(emirp) == count:
			a = 0
	return emirp

# for i in findEmirp(20):
# 	print("Emirp = ", i)

def readFile():
	inp = raw_input("Enter File Path:")
	words = open(inp).read().split()
	for i in set(words):
		print("Words = ", i)

readFile()


