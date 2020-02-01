# base definition 20190727
b = 20
a = 10
class A(object):
  a = 20
  b = 30
  def sum(self, a, b):
  	print (dir(self))
  	a = 10
  	b = 30
  	return a + b
  
  def add(self):
  	return self.a

# print A.sum()


# print setattr(A, 'c', 1)
# s = A()
# print type(A)
# print(dir(s))
# print(s.a)
# print('add', s.add())
# print(s, A)
# print(s.a)


#contructor __init__

class B:
	a = 10
	b = 20

	def sum(self):
		self.c = self.a + self.b

	def __init__(self):
		self.sum()

# cls = B()
# print(dir(cls))
# print(cls.c)
# setattr()
# cls.sum()
# print('after', dir(cls))
# print(cls.c)
# print('property', dir(B))
# print('property', dir(cls))
# print(B.a + B.b)

# constructor with Parameter

class Base1:
	fruits  = ['apple', 'orange', 'mango']
	a = 1

class Base2:
	animals  = ['dog', 'cat', 'monkey']
	b = 2

class Sample:
	a = 10
	b = 20
	c = 30

	def sum(self):
		return self.a + self.b + self.c

	def __init__(self, c):
		print('c is', self.c)
		# self.c = c

# cls = B(6)
# print(cls.sum())
# print('before', B.d)
# setattr(Sample, 'd', 100)
# print('after', B.d)

#Inheritance
# single Inheritance one base into one derived
# print ("Base class", dir(B))
class D(B):
	pass
# print(D.a)
# print("single Inh", dir(D))

class Sample1(Sample):
	pass

# print(dir(Sample1))
# print(Sample1.a)

class A:
	a = 1

class B:
	b = 2

class C(A, B):
	def sum(self):
		print(dir(self))
		return self.a + self.b
# print(C().sum())

# Multiple Inheritance Many to One
class D(Base1, Base2):
	pass

# print(dir(D))
# print(D.animals)


#multi level inheritance - Deriving Derived instance into Derived Class
class E(C):
	pass

print("E", dir(E))