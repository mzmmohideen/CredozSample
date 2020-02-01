# # import classSample as c
# from classSample import D
# print dir(D)

# # print "before instantiate", D.a, D.b

# print "after instantiate", D().a, D().b


# class E(D):

#   def ad(self):
#       print 'after inherit', dir(self)

# E().ad()
x = 100
y = 200
z = 300

# def sum():
#   return x+y+z

class SampleClass:
    x = 10
    y = 20
    z = 30
    # print x+y+z
    # def sum(a):
    #   x = 10
    #   y = 20
    #   z = 30
    #   return x+y+z

    def sum(self):
        return self.x+self.y+self.z

# cls = SampleClass()
# # print type(cls)
# print cls.sum()

# class className(object):
   
   # def sum(self, c, d):
   #    self.c  = 100
   #    return self.a+self.b

   # def __init__(self, a, b):  
   #  self.b = b
   #  self.a = a
   #  print "I am"




# cls = className(20, 30)
# print "before", dir(cls)
# print cls.sum(1,2)
# print "after", dir(cls)
# print cls.a
# print cls.sum(2, 3), a, b

a = 1
b = 2
class A:
  a = 10
  b = 20
  def sum(self, a ,b):
    return a + b
    # print(dir(self))

  def sub(self):
    return self.c - self.a
  
  def __init__(self, c, d):
    self.c = c
    self.d = d

  def __del__(self):
    pass

# s = A(50, 40)
# print(s.c)
# print(dir(s))
# t = A(10, 20)
# print(t.c)
# s = A
print('before', dir(A))

n = input("Enter Variable Name")
setattr(A, n, 100)
print('after', dir(A))
# print(A.e)