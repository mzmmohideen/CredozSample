# -*- coding: utf-8 -*-
# @Author: mzmmohideen
# @Date:   2020-01-19 14:17:47
# @Last Modified by:   mzmmohideen
# @Last Modified time: 2020-01-24 09:07:48

class Sample:
	a = 1000
	b = 2
	def sum(self):
		self.c = self.a + self.b

	# def __init__(self, a=10, b=20): # constructor with parameter
	# 	self.d = a
	# 	self.e = b


class Sample1:
	a = 1
	b = 2
	def sum(self):
		self.c = self.a - self.b

	# def __init__(self): # constructor without parameter
	# 	self.sum()


class Calc(Sample1): # derived class
	def mul(self):
		self.c = self.c * 2

class OutputMultilevel(Calc):
	pass


class OutputMultiple(OutputMultilevel, Sample1, Sample):
	pass


print(dir(OutputMultiple))	

cls = OutputMultiple()
cls.sum()
print(cls.c)
# print('before', dir(Sample))
# cls = Sample(10, 20) # instantiating constructor with parameter
# cls = Sample1() # instantiating constructor with parameter
# # cls.sum()
# print(cls.c)
# # print('after', dir(cls))


class A:
	a = 10

class B(A):
	a = a + 10

class C(B):
	a = a + 20

cls = C()
print(cls.a)
