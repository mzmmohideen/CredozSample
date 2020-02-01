# 2019-03-09
# function and its argument mode
# how map works
# function calling methods
# how range works
a = 10
b = 20
c = 0

def add(q, w, x):
    print 'w', w
    print 'q', q
    c = q+w
    return c

def sub(a, b):
    global c
    c = a-b
    return c

# print add(*[20, 10, 20])

def mapping(func, li):
   out = []
   for i in li:
     print 'loop started'
     sqr = func(i)
     print 'sqr number', sqr
     out.append(sqr)
   return out

def cube(var):
    return var*var*var

def mapp(func, li):
    print func
    return [func(x) for x in li]

def convert(arg):
    out = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }
    if arg in out.keys():       
        return out[arg] 
    # return out.get(arg, "Not availble")
    return "not implemented"


# print mapp(convert, [1, 2, 3])

def square_func(a):
    return a*a

def square_gen(a):
    yield a*a

# print square_func(10)
a = square_gen(10)

def ran(*a):
    print 'a', a
    step = 1
    start = 1
    if len(a) == 0:
        return "0 arguments given"
    if len(a) == 1:
        stop = a[0]        
    elif len(a) == 2:
        stop = a[1]
        start = a[0]
    else:
        start = a[0]
        stop = a[1]        
        step = a[2]
    out = []
    bol = 1
    while bol:
        if start < stop:       
           out.append(start)
           start+=step
        else:
           bol = 0
    return out
a = ran(10)
print 'ran', a