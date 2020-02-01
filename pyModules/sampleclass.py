# #    import    test.first
# from    test.first    import    map

# #  print    'my    custom    map',    map([1,2,3,4,5])
# class    Credo():    
#         #    name    =    raw_input()
#         #    age        =    input()
#         #    mobile    =    input()
#         name    =    'credo'
#         age        =    10
#         mobile    =    9884412345

#         def    __init__(me):
#                 me.name    =    'system'
#                 me.age    =    20

#         def    info(self,    name,    age,    mobile):
#                 print    'name:    ',    name
#                 print    'age:    ',    age
#                 print    'mobile:    ',    mobile


# class    Test(Credo):
#         #  def    __init__(self,    arg=10):
#         #          super(Test,    self).__init__()
#         #          self.arg    =    arg

#         def    info(self,  name,  age,  mobile):
#                 super(Test,    self).info(name,  age,  mobile)

# #  w    =    Test()
# #  print    'parameterized',    w.info('credo',  10,  988413)
# [Finished in 0.0s]

val = 0
class calculator:  
  a = 100
  # print a
  me = 10

  def add(self, a, b):
    print 'before', self.a
    self.a = 20
    print 'after', self.a
    print 'add started'

  def sub(self):
    pass

  def __init__(self):
    print 'self', self.a
    self.a = 10
    print 'i have started', self.a
    # self.add()

def function():
  pass

def sub():
  print 'i can subtract'

# print val
# e = calculator()
# # print e.sub()
# # print type(e), dir(e)
# e.add(10, 20)


class class1(object):
  """docstring for class1"""
  def __init__(self, arg):
    self.arg = arg

  def add(self, a, b):
    print 'a+b'
    return a+b

class class2(class1):
  """docstring for class2"""
  def __init__(self, arg=10):
    # super(class2, self).__init__()
    # self.arg = arg
    print 'self', dir(self)
    self.add(10, 20)

  def add(self, a, b):
    res = super(class2, self).add(a, b)
    print 'res', res
    # return a-b
    
# clscall = class2()


# class ClassName(object, class2):
#   """docstring for ClassName"""
#   a = 10
#   def __init__(self, arg=10):
#     print 'a', self.a
#     super(ClassName, self).__init__()
#     self.a = arg
#     print 'after',self.a
#     pal = self.palindrome(self.a)
#     print pal


#   def palindrome(self, val=12321):
#     if str(val) == str(val)[::-1]:
#       return "its palindrome!"
#     return "No its Not!"
    
# class B(ClassName):
#   """docstring for B"""
  
#   def palindrome(self, arg):
#     pal = super(B, self).palindrome(arg)
#     return "palindrome for %s is %s"%(arg, pal)

    
# w = B()
# for i in [ClassName(), B()]:
#   output = i.palindrome('madam')
#   print 'output', output
# w.palindrome('madam')
# pal = w.palindrome('madaras')
# print pal

def palindrome(val=12321):
    if str(val) == str(val)[::-1]:
      return "its palindrome!"
    return "No its Not!"


# w = palindrome()
# print 'w', w


# class login:
#   pass

#   def check(self, uname, pwd):
#     pass

# class auth(object, login):
#   def check(self, uname, pwd):
#     pwd = pwd into encrypt
#     super(auth, self).check(uname, pwd)


class Employee:
  a = 10
  b = 20

  def add(self):
    print 'addtion'
    return self.a+self.b


  # def __init__(self, arg):
  #   print "Hi this is employee"


# class Student:

#   def __init__(self):
#     self.a = 10
#     self.b = 20
#     # print super(Student, self).add(10, 20)
#     # print 'Hi this is Student'

#   def add(self):
#     print 'subtract'
#     return self.a-self.b
#     # print super(Student, self).add(self.a, self.b)

class Employee:
  __a = 100

  def __init__(self):
    self._a = 10
    self.__a = 10
    # self.details()

  def details(self):
    print "Penguin Cant fly!"


class Student(Employee):
  __a = 20

  def __init__(self):
    self._a = 20
    print dir(self), self._a
    print self._Employee__a, self._Student__a
    self._a = 20    
    self.details()

  # self.__a _ will be replace with _Student_

  def details(self):
    print "Eagle can fly!" 

w = Student()


# class Add