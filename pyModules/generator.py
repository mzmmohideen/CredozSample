def PowTwoGen(max = 0):
    n = 0
    while n < max:
        # print 'n', n
        yield 2 ** n
        n += 1
a = PowTwoGen(10)
print a, 'generators'
for i in a:
    print i

def iter(): 
    # a = 0
    for i in range(100):
        yield i
    # while a:
    #     yield a
    #     a+=2

# a = iter()
# print 'a', a

# for i in a:
#     print i, 'i'

# fill in this function
def fib():
    a = 1
    b = 1
    yield(a)
    yield(b)
    for i in range(2, 10):
        c = a+b
        a, b = b, c
        yield(c)
    #pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
# if type(fib()) == types.GeneratorType:
#     print("Good, The fib function is a generator.")

#     counter = 0
#     for n in fib():
#         print n, 'n'
#         counter += 1
#         if counter == 10:
#             break


def name():
    n = raw_input("Your Name:")
    try:
      print "My name is {1} I am {0} years old".format(10, n)
    except IndexError:
        print "Something wrong"
    finally:
        print "I am also here"
# name()