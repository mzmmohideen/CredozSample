class A:
    b = 0
    def PowTwoGen(max = 0):
      n = 0
      while n < max:
        yield 2 ** n
        n += 1

    if __name__ == "gener":
        a = PowTwoGen(10)
        print 'a', a

    # else:
    #   a = 10


# is power of 2 number?

counter = 0
def powoftwo(n):
    global counter
    counter+=1
    if n%2 != 0:
      return "Given Number %s is not Power of 2!"%g
    else:      
      if n==2:
        return "yes give number %s = 2**%s is power of 2!"%(g, counter)
      return powoftwo(n/2)

g = 1024
print powoftwo(g)