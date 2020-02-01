class Sample(object):
	a = 10
	b = 20

	def sum(self):
		return self.a + self.b

class Sample1(object):
	
	c = 20
	d = 30

	def sum(self):
		return self.c + self.d

class Derived(Sample, Sample1):
	
	def sum(self):
		return 100

cls = Derived()
print(dir(cls))
print(cls.sum())
		

		