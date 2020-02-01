# # a

a  = 10

# print "a", a
# a = 10
# print "credo"+" System"
# # "" + ""
# # "%s"%val
# # "{}".format(1, 2)
# # print "My Number is : %s %s"%(10,20)
# # print "My Number is : {} {} {}".format(*[10, 20, 30]).split()

# def sqaure(a=10, b=20):
#     return a-b
#     # if a == 10 or isinstance(a, str):
#     #     print "Yes"
#     # elif a == 5:
#     #     print "Its %s"%a
#     # else:
#     #     print "No"
# print "i am done"
# outout = sqaure(10, 20)
# print 'outout', outout



# # print range(20)

# # example - Break
# # for i in range(20):
# #     if i == 15:
# #         pass #
# #     if i%2 == 0:
# #         print "%s is Even"%i
# #     else:
# #         print "%s is Odd"%i
# # a = 0
# # a = []
# # while a:
# #     print 'a', a
# #     # a=0
# #     print 'a', a
# #     if a == 100:
# #         a = 0


# class A:
#     def __init__(self):
#         self.a = 10
#         self.b = 20

#     def add(se, a, b):
#         return a + b


# class B(A, object):

#     def add(se):
#         # pass
#         return super(B, se).add(10, 20)

# instance = A()
# # print dir(instance)
# try:
#     w = instance.add(10, 'system')
#     print 'before super', w
# except Exception as e:
#     print 'error', e


# class Penguin:

#     def __fly(self):
#         return "Penguin cant fly"

# class Eagle(Penguin):

#     def __fly(self): # single _ will replace with _ClassName_ eg: __fly will became _Eagle__fly
#         return "Eagle cant fly"

# for i in [Penguin(), Eagle()]:
#     print dir(i)

# a = 1
# try:
#     if a:
#         pass
#     # if b:
#     #     pass

# except NameError:
#     print "some error"

# # finally:
# #     print 'Exception caught'

# else:
#     print 'i am done'

# print dict(zip(['a','b'], [1,2]))
# print dir(__builtins__)

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return "({0},{1})".format(self.x,self.y)
    
#     def __add__(self,other):
#         print 'other', other, self.x, self.y
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x,y)
# p2 = Point(2,3)
# p1 = Point(-1,2)
# print(p1 + p2)

# import threading
from threading import Thread
# print dir(threading) 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    a = 1
    while a:
        a+=1
        print('a', a)
        if a == 1000:
            a = 0
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
# if __name__ == "__main__":
#     print 'session started'
#     t1 = Thread(target=print_square, args=(10,))
#     t2 = Thread(target=print_cube, args=(10,))
#     t1.start() 
#     t1.join()       
#     t2.start()
#     # t2.join()

#     print "DONE"
# else:
#     print "here it will work"
#     print_square(10)
#     print_cube(10)


#     # creating thread 
#     # t1 = threading.Thread(target=print_square, args=(10,)) 
#     # t2 = threading.Thread(target=print_cube, args=(10,)) 
  
#     # # starting thread 1 
#     # t1.start() 
#     # # starting thread 2 
#     # t2.start() 
  
#     # # wait until thread 1 is completely executed 
#     t1.join() 
#     # # wait until thread 2 is completely executed 
#     t2.join()
#     # both threads completely executed 
#     print("Done!") 

# import os

# def child():
#    print('\nA new child ',  os.getpid())
#    os._exit(0)  

# def parent():
#    while True:
#       newpid = os.fork()
#       if newpid == 0:
#          child()
#       else:
#          pids = (os.getpid(), newpid)
#          print("parent: %d, child: %d\n" % pids)
#       reply = raw_input("q for quit / c for new fork")
#       if reply == 'c': 
#           continue
#       else:
#           break

# parent()

### fork

import os, sys

print("The child will write text to a pipe and ")
print("the parent will read the text written by child...")

# file descriptors r, w for reading and writing
r, w = os.pipe() 

processid = os.fork()
print('processid', processid)
# if processid:
#   print("I am parent")

# else:
#   print("I am child")
if processid:
   # This is the parent process 
   # Closes file descriptor w
   os.close(w)
   r = os.fdopen(r)
   print("Parent reading")
   str = r.read()
   print("text =", str   )
   sys.exit(0)
else:
   # This is the child process
   os.close(r)
   w = os.fdopen(w, 'w')
   print("Child writing")
   w.write("Text written by child...")
   w.close()
   print("Child closing")
   sys.exit(0)