class Lion:

	def sound(self):
		return "Roar"

class Dog:

	def sound(self):
		return "Bark"

# for i in [Lion, Dog]:
# 	cls = i()
# 	print(cls.__class__, cls.sound())

#__new__

class New:
	pass

	def __str__(self):
		return "I am new"

	# def __repr__(self):
	# 	return "New"

# print(str(New()))
def exec(cls):
	ins = cls()
	return ins.sound()

# print(exec(Lion))

class A:
	a = 10
	_a = 100
	__a = 1000

	def sum(self):
		return self.__a + self.a + self._a

class B(A):
	a = 1
	_a = 2
	__a = 3

	def sum(self):
		print(self.__a, self._A__a, self._B__a)
		print('a', dir(self))

# print(B().sum())
