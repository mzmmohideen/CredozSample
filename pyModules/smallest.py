a = 10
print 'a', a
class Smallest(object):
	_name = 'sundar'
	__names = '123'

	# def __del__()

	def func():
		_mohi = '1'
	print _name
	"""docstring for Smallest"""
	# def __init__(self, arg=1):
	# 	print 'args'
	# 	self.name = 'credo'
	# 	print self.name
	# 	self.func()
	# 	super(Smallest, self).__init__()
	# 	self.arg = arg

	def func(self):
		name = 'credo'
		print 'checking'

a = Smallest()
print 'a', dir(a)
print a._Smallest__names

class Encapsulation(Smallest, object):
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c
        self.__names = '12345'

x = Encapsulation(11,13,17)
print x._Encapsulation__private
print dir(x)