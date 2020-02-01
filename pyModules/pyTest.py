# comments
"""
	Palindrome 
"""
print
def a():
	# comemnt
	"""
		vowels
	"""
	a="credo"
	out=[]
	# out=[i for i in a if i in "a,e,i,o,u"]
	for i in a:
		if i in "a,e,i,o,u":
			out.append(i)
	print out
		
																	
		
	return out


def fib(start,count):
	a=[start,start+1]
	for i in range(count-len(a)):
		a.append(a[-1]+a[-2])	

	return a

# print fib(0,10)

#print help(a)

def abc(w=10):
	if w == 10:
		print 'w', w
		return 'Loop terminated'
	else:
		print 'w is not equal to 10', w
		if w < 10:
			i = w+1
			print 'w incremented by 1', i
			abc(i)
		else:
			i = w-1
			print 'w decremented by 1', i
			abc(i)

print abc(13)


def ab(w=10):
	while w:

		# if w == 10:
			# print 'w', w
			# return 'Loop terminated'

		w=w+1 if w<10 else w-1 if w>10 else 0 
		# else:
			# print 'w is not equal to 10', w
			# if w < 10:
			# 	w = w+1
			# 	print 'w incremented by 1', w
			# else:
			# 	w = w-1
			# 	print 'w decremented by 1', w
			

print ab(12)


def palin(a):
   if a == a[::-1]:
      return '%s is palindrome'%a
   else:
      return "%s is not a palindrome"%a

def palinSim(a):
    return "Its is Empty!" if not a or a == "" else "%s is palindrome"%a if a == a[::-1] else "%s is not a palindrome"%a
print palinSim('')


def gcd1(a,b):
    print 'a', a, 'b', b
    return a if not b else gcd1(b, a%b)

# using while,

def gcd(a,b):
  while b:
    print 'b', b, 'a', a
    a,b = b, a%b
  return a

# using lambda,

# gcd2 = lambda a,b : b, gcd(a%b)


print gcd1(111,222)

if __name__ == "pyTest":
	print "name", __name__
else:
	print "nn", __name__
