def add(a, b, c = 3, *args, **kwargs):
    print 'a', a, 'b', b, 'c', c, 'args', args, 'kwargs', kwargs

    return sum(list(args)+kwargs.values())

# i = input()
# print add(1,2,5,4,5, d = 3)

# s = sum()
# print "return value is", s
# print s

def RFunc(*args):
	start = 0
	step = 1
	out = []
	if len(args) == 1:
		stop = args[0]
	elif len(args) == 2:
		start,stop = args
	elif len(args) == 3:
		start,stop,step = args
	else: 
		raise ValueError("Kindly enter required input")

	while start < stop:
		# out.append(start)
		yield start
		start = start + step

print(list(RFunc(3,12,4)))

		
