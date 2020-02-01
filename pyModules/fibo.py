"""
help doc about module fibo.py
"""
a = 10
b = 20
c = 30

def fibo(start, count):
    a = [start, start+1]
    for i in range(count-len(a)):
        a.append(a[-1]+a[-2])
    return a

# a = fibo(0, 10)
# print 'a', " ".join([str(i) for i in a])

def squre(a):
    """
       This is squre function. this will return square value of given integer. formula was n*n
       Here n represents number (User input)
    """
    return a*a

# fibo in rec func 20190701
def fiborec(n, out=[1,2]):   
   if n-2 == 0:     
     return out
   out.append(out[-1]+out[-2])
   return fiborec(n-1, out)

#fibo in generator 20190701
def fibo(n):
   out = [0, 1]
   for i in range(n-2):
     out.append(out[-1]+out[-2])
     yield out


#fibo in generator 20190701
def fibo(n):
   out = [0, 1]
   for i in range(n-2):
     out.append(out[-1]+out[-2])
   return out

# print fibo(10)
z = 10
def gcd(a, b):
    return a if b==0 else gcd(b, a%b)

print gcd(10, 20)

# print Reverse of string using recursion 
def strReverseRec(s, out=[]):
    if len(s) == len(out):
        return "".join(out)
    out.insert(0, s[len(out) if out else 0])
    print (out)
    return strReverseRec(s, out)

# print strReverseRec("Credo")


def strReverse(s):
    out = ""
    for i in s:
       out = i+out
    return out 

# print strReverse("Credo10")

def is_power(n):
   if not n == int(n):
      return "Not power of 2"
   n = int(n)
   if n == 1:
      return "power of 2"
   elif n >= 2:
      print (n)
      return is_power(n/2.0)
   else:
      return "Not power of 2"

# print is_power(1)is_power(1)

# def is_power(n):
    # if n & (n-1)


def is_power(n):
    if n & (n-1) == False:
        return "Power of 2"
    else:
        return "Not power of 2"
# print is_power(8)



# g = []
# h = []
# j = []
# i = []
# for a in [5,6,7,10,11,12,10,13,10,8,7, 15, 16, 14]:
#     if a < 10 and 7 > a or a == 8:
#        g.append(a)
#     elif a == 10:
#        h.append(a)
#     elif 10 < a < 14:
#        i.append(a)
#     else:
#        j.append(a)

# print 'g', g
# print 'h', h
# print 'i', i
# print 'j', j



    




# print gcd(17, 25)
# print map(lambda x: x*x, [1,2,3,4,5])

# print ' '.join((str(i) for i in fib))


# m = 10

# def squre():
#   global m
#   m = 20
#   print 'm', m

# def my():
#   print m
# squre()
# my()

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


def fib(n):
    n1=0
    n2=1
    out='{} {}'.format(n1,n2)
    for i in range(n-2):
        n3=n1+n2
        n1=n2
        n2=n3
        out+=' {}'.format(n3)
        yield out

    # for i in range(10):
    #   yield i

#func call 20190718
# a = fib(5)
# print a
# # print a.next()
# # print a.next()
# # print a.next()
# # print a.next()
# # print a.next()
# for i in a:
#   print "i=", i


def fib(n):
   i, j = 0, 1
   out = "{} {}".format(i, j)
   for k in range(n-2):
      m = i + j
      i = j
      j = m      
      print('out',out, m)
      out = "{} {}".format(out, m)

   return out

# print(fib(5))
