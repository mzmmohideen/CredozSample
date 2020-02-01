import os

class Myclass(object):
	"""
		Hi This is sample class which shows how its structured
	"""
	
	def __init__(self):
		"""
			I am a sample instance of a class
		"""
		print "initiated"

	def doAny(self):
		"""
			I am a sample function of a class
		"""
		print "I am Done"


class Temp(object):

	def __init__(self):
		self.a = 10

	def add(self, a, b):
		self.a = a+b

q = Temp()
q.add(10,20)
print q.a

class Check(Temp):

	def add(self, a, b):
		w = super(Check, self).add(a, b)
		print 'w', self.a

c = Check()
print c.add(10, 20)