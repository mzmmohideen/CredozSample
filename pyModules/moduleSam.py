__author__ = "sudharson"
import fibo as f
from fibo import *
from sam.folder_size import *


a = 100
b = 200
name = "credo"
# print(dir(f))

def filt(func, iter):
   out = []
   for i in iter:
     if func(i):
       out.append(i)
   return out


def sum():
	pass

# print(f.fib(5))
if __name__ != "__main__":
	print('a',__name__ )
	print(f.fib(5))

