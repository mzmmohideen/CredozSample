class a():

	def sumadd(self,a,b):
		c=a+b;
		return c;


class b(a):

	def summin(self,a,b):
		c=a-b;
		return c;
x=b()

# print x.sumadd(2,2)
# print x.summin(1,2)



class Add:



 	def __init__(self):
		self.a = 10

	def add(self, loc):
		print self.a, loc
		return self.a+loc

	def __sub__(self, a):
		print 'a', a
		return self.a+a

q = Add()
print q-100

