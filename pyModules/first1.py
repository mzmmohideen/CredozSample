""" Hi sample """
# a = 1
# print 100
# for i in range(10):
#     a = i # i write 
# print 'a is=', a
l = []
for i in range(10):
	if i%2 == 0:
		l.append(i)
# print l
# a = 0
# for i in []:
# 	a = 10

# def credo(a,b):
# 	print 'something', a, b

# print credo(1, b=20)

# def func(a, b=5, c=10):
# 	print('a is', a, 'and b is', b, 'and c is', c)

def squre(a):
	# print 'l is', l
	global l
	l = 10
	print 'l', l
	if a %2 == 0:
		print "even number"
	else:
		print "odd number"

s = squre(11)
print 's', s
print 'final l is', l

def oddeven(v): # here is odd even function will check input is odd or even and return boolean
	if v % 2 == 0:
		return True
	else:
		return False

def map(b): # this is custom made function
	output = []
	for i in b:		
		_v = oddeven(i)
		print 'i', i, 'is', _v
		output.append(_v) #oddeven is itself function which declarted above
	return output

# print map([1,2,3,4,5])


# print map(lambda a: a%2==0,[1,2,3,4,5]) # this is inbuilt function