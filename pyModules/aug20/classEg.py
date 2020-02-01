# inp = '10 20 30 40'
class calc: # this is the sample class
   # inp = raw_input("Enter your numbers:")
   inp = '10 20 30 40'
   
   @property
   def foo(self):
       return self._foo
   
   @property
   def sum(self):  
      # inp = '100 200 300 400'    
      # return sum([int(i) for i in inp.split()])
      values = self.inp.split()
      values = map(int, values)
      return sum(values)

class Lion:

   def sound(self):
      return "Lion Roar!"

class Dog:

   def sound(self):
      return "Dog Bark!"

# for i in [Lion, Dog]:
#    cls = i()
#    print(cls.sound())
# cls = Lion()
# cls.sound()

# cls1 = Dog()
# cls1.sound()

# for i in [Lion(), Dog()]:
#    print(i.sound())

# c = calc()
# print(c.sum())

class A:
   a = 10

   def sum(self, a, b):
      print(dir(self))
      pass

   def cls8(self):
      pass

   def cls10(self):
      pass

   def __init__(self, b):
      if b <= 13:
         self.b = self.cls8()
      else:
         self.b = self.cls10()

# print(dir(A), "before")
# cls8 = A(13)
# cls1 = A(2)
# # cls.b = 20
# print(dir(A), "after")
# print(dir(cls), "after CLS", cls.b)
# print(dir(cls), "after CLS", cls1.b)
# cls.sum(10, 20)

class A:
   a = 10   


class B:
   b = 20

   def sum(self):
      # print(dir(self))
      return self.a + self.b

class C(A, B):
   pass

# print("CLASS C", dir(C))
# C().sum()
# b = B()
# print('b', b.sum())

class AA(object):
   a = 10
   _a = 100
   __a = 300
   def sum(self):
     return self.a + self._a

s = AA()
# print(s.sum())
# print(s.__a)
class B(AA):
   def sum(self):
      return super(B, self).sum()
      return self.a - self._a

s = B()
print(s.sum())