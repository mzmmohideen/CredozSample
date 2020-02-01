import string
def toupper(inp):
   l = string.ascii_lowercase
   u = string.ascii_uppercase
   d = dict(zip(l, u))
   out = d.get(inp)
   return out if out else inp

print(''.join(map(toupper, 'credo@system')))

# map will return equal with different values for each and ecery element of your iterables

def map(func, iter):
	# python 2 map
	out = []
	for a in iter:
		out.append(func(a))
	return out

def map(func, iter):
	# python 3 map
	for a in iter:
		yield func(a)

import sys
output = map(toupper, 'credo')
print(sys.getsizeof(output))

print('using comprehension', [toupper(a) for a in 'credo'])


def vowels(i):
	return i.lower() in 'aeiou'

print('using filter function', filter(vowels, 'credo'))
print('vowels using comprehension', [i for i in 'aeiou' if i.lower() in 'aeiou'])


def fact(inp):
	if not inp:
		return 1
	else:
		return inp * fact(inp-1)

print(fact(5))

def gcd(a, b):
	print('a', a, 'b', b)
	if not b:
		return a
	else:
		return gcd(b, a%b)

print(gcd(13, 260))