# from sampleclass import Credo

class Eagle:

    def fly(self):
        return "Eagle can Fly!"

class A:
   a = 10
   b = 20

   def __init__(self, a,b):
    self.d = self.a +  self.b
    self.d = self.a +  self.b
    self.e =self.sum()

   def sum(self):
    return self.d
    # self.d = self.a +  self.b
    # print(dir(self))

# c = A
# # print(A.d)
# print(dir(c) , 'before')
# # print(c.sum())
# print(A(10, 20))
# # print(c.e)
# print(dir(c), 'after')
# exit()
class Eagle:

    def fly(self):
        return "Eagle can Fly!"

class Penguin:

    def fly(self):
        return "Penguin can't Fly!"

class Employee:

    def whoami(self):
        return "Am an Employee!"

class Student:

    def whoami(self):
        return "Am a Student!"

# print Employee().whoami()
# print Student().whoami()

# for i in [Employee, Student]:
#   print "%s"%i.__name__, i().whoami()
class ABC(object):

    def sum(self):
        return 100
# ABC = 1

class Base(ABC):
    a = 10
    b = 20
    def sum(self):
        return self.a + self.b

class Der(Base):

    def sum(self):
        print(dir(self))
        res = super(Der, self).sum()
        print('res', res)
        return self.b - self.a

print(Der().sum())

exit()


class A(object):
    a = 1
    b = 2
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b


class B(A, object):
    c = 100
    d = 20
    
    def __init__(self, a, b, c, d):
        super(B, self).__init__(a,b)
        self.c = c
        self.d = d
        #super(B, self).__init__()  

    def sum(self):
        print self.a, self.b, self.c, self.d
        # exit()
        # self.b = 100
        # print dir(self), B.a
        # return super(B, self).sum()
        return self.a-self.b

print

# print dir(B)

# c = B(10, 20, 30, 40)
# print c.sum()




class Temp(object):
    c = 10
    """docstring for Temp"""
    def __init__(self, arg=10):
        super(Temp, self).__init__()
        self.arg = arg
        
class ClassName(Temp):
    a = 10
    """docstring for ClassName"""
    def info(self):
        print 'class dir', dir(self) 
        res = super(ClassName, self).info('credo', 10, 12345)
        print 'original response', res


    def __init__(self):
        print 'info', self.info()
        self.a = 20
        super(ClassName, self).__init__()
        # self.arg = arg
    def myfun(self, val):
        self.a = val
        print 'aaa', self.a

# a = 100
# b = 200

class A:
   # b = 30
   # a = 10

   # print '1', a+b

   def sum(self, a, b):      
      self.a = a
      self.b = b
      print '2', self.a+self.b
      return self.a + self.b

   def sai(nit):
        return nit.a + nit.b

# a = 2
# b = 6

class B:

    def __init__(self):
        print "Constructor initiated without cosntruct anything"


    def sub(self):
        self.a = a
        self.b = b
        self.c = a+b

        print dir(self)
        return self.c-self.b

# f=B()

# print(f.sub())        

#access specifier

class accessA:
    a = 10
    _a = 20
    __a = 30

    def __sum(self):
        print "I am different"

class accessB(accessA):
    a = 100
    _a = 200
    __a = 300

    def __sum(self):
        # print dir(self)
        print 'public', self.a, 'private', self._a, 'protected', self.__a, 'protected of class accessA', self._accessA__a

# c = accessB()
# # print dir(c)
# print c._accessB__sum()
# print c._accessB__a
# print 'running'

# if __name__ == 'class_eg':
#   cls = A()
#   out = cls.sum(1, 2)
#   print '3', out
#   print 'nit', cls.sai()
    # a = ClassName()
    # a.myfun(50)
    # print 'a', dir(a)
class A:

    def sum(self,a,b):

        c=a+b
        return c

class B(A):
    pass

class cal:
    def __init__(self,a,b):
       self.a=a
       self.b=b
       
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# c=cal(a,b)
# i=int(input("""
#         1.add
#         2.mul
#         enter ur choice:"""))
# if i==1:
#     print c.add()
# elif i==2:
#     print c.mul()
# else:
#     print "invalid input" 
# #     
# class A:
#     a= 20
#     b=10
#     def sum(self):
#         self.c=self.a + self.b
#         return self.c
# s=A()
# print s.sum()

# class prime:
#     def pri(self,a):
#         for i in range(2,a):
#             if a%i==0:
#                 return "not a prime number"
            
#         return "prime number"

# p=prime()
# print p.pri(23)
import random as r
a=str(r.randint(1000,9999))
# print(a)
# def cowbull():
inp = True
count = 0
while inp:
    count += 1
    b=list(raw_input("enter a 4 digit number:").replace(" ", ""))
    for i in range(4):
        if a[i]==b[i]:
            b[i]="cow"
        elif b[i] in a:
            b[i]="bull"
    print b    
    if b.count("cow")==4:
        # return 'success'
        inp = False

print("Success! You took %s try!"%count)
    # else:
    #     return cowbull()
# print(cowbull())        

        

