# import moduleA
from sample.moduleA import *

print('started')
print("My module is", __name__)

def sample():
	return 5


def sum(n):
	return n*n	


def misc():
	sum(10)

	# print(dir(moduleA))

	# a = 100
	print('a is', a)
	print('b is', b)
	print(a)
	print("Hello World")


def drawPattern(i):
	for kishan in range(i+1):
		kishan = kishan+1 if kishan%2 != 0 else kishan
		star = kishan*"*"
		print(star.center(i))
# print(sample())
# print(__name__)
if __name__ == "__main__":
	print("I am executed")
	drawPattern(6)
	
	# sample()