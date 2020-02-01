import sys

print(sys.argv)
# inp = 
a,b = sys.argv[1:]
# a = 10
# b = 20

def sum():
	return a + b

class A:
   a = 10
   b = 20
   def sum(self):
   		return self.a + self.b

   def __init__(self, a, b):
   		self.a = a
   		self.b = b



# a = int(input("Enter a:"))
# b = int(input("Enter b:"))

print('class definiton', A(a,b).sum())

print('module definition', sum())