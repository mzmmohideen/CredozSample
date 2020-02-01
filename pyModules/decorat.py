def permission(func): #decorator function
    print 'func', func
    def nested_func(*args, **kwargs): #wrapper function
       print 'args',args
       perm = args[2]
       # args = [i*i for i in args if isinstance(i, int)]
       # print 'args',args
       if "mohideen" == perm:
          val = func(*args, **kwargs)
          return val
       # a = [i*i for i in args[:-1]]   
       # return func(*a)
       return "Access Restricted!"
    print "step 2"
    return nested_func
 
# def sum(a, b, perm="allow"):
#     return a+b

@permission
def sum(a, b, perm="None"):
    print 'a', a, 'b', b
    # print "is Execution started?"
    return a+b
# sundar = sum
print sum(10, 20, 'mohideen')


class Add:

   @staticmethod
   def sum():
     # print self
     return 1+2

   @classmethod
   def sumofnum(cls):
    print 'cls', cls
    return 1+3

# cls = Add()
# print(Add.sumofnum())
# print(Add.sum())
# print Add.sumofnum()/home/mohideen/Desktop/sam.txt
# print 'output', Add().sum()

class A:
  
  @classmethod
  def sum(cls):
    print cls
    return 1+2
  
  @staticmethod
  def sub():
    return 5

class A:
  def sum(self):
    return 1+2
  
  def __enter__(self):
    return self.sum()
  
  def __exit__(self, type, value, traceback):
      self.sum()

# with A() as s:
#   print 'context manager', s

