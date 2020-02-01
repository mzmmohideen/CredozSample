# class SampleClass:
#   arg = 100

#   def sum(self, arg):
#       return self.arg + arg
#   """docstring for SampleClass"""
    
#   def __init__(self, arg):
#       # super(SampleClass, self).__init__()
#       print 'sef', self.arg
#       self.arg = arg
#       print 'after', self.arg

# cls = SampleClass(10)
# print dir(cls)
# print cls.sum(20)
import sys

class test:
    n = 11

    def Palindrome(self): 
        # s = raw_input("Enter your name:") 
        print('arb', sys.argv)
        s = sys.argv[1] 
        r = s[::-1]   
        if (s == r):
            return "palindrome"
        else:
            return "Its not a palindrome"

    def factorial(self):
        if self.n == 0:
            return 1
        else:
            return self.n * self.factorial(self.n-1)
            print (factorial)

# a = 10
class B:
    # a = 10
    # b = 20

    # print a, b
    
    def sum(self):
        print(self.a+self.b)

    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b
        # self.sum()


class D(B):
    """
    This is a sample class to demostrate constuctor along with method calling!
    """
    # print B.a, B.b
    def __init__(self):
       self.a = 100
       self.b = 200
    
    def sum1(self):
       """
       Sum is the method which going to add 2 class instance called a and b
       """
       self.c = self.a+self.b
 
    def sub(self):
        # self.sum()
        print(self.e)


if __name__ == "__main__":

    # r = input("Enter String:")

    # if r == r[::-1]:
    #     print("Given String is palindrome")
    # else:
    #     print("Its not a palindrome")
    
    grp1, grp2, grp3, grp4 = [], [], [], []
    for i in [10, 9, 8, 7, 11, 12, 11, 10, 13, 14, 15, 9, 10]:        
        if i == 10:
          grp1.append(i)
        elif 10 <= i < 13:
          grp2.append(i)
        else:
          grp3.append(i)
        # elif i == 10:
        #   grp4.append(i)  
        # else:
        #   grp3.append(i)


    print('grp1', grp1)
    print('grp2', grp2)
    print('grp3', grp3)
    print('grp4', grp4)

    # cls = D()    
    # # setattr(D, 'e', 100)
    # # cls.sub()
    # print dir(cls)
    # print cls.a, cls.b


    # print cls.__doc__
    # e = test()
    # print e.Palindrome()
    # cls = B(20, 50)
    # print cls.sum()
# print e.factorial()


# l = len(string)
# st = [string[i:j+1] for i in range(l) for j in range(i, l)]
# s = sum(map(lambda x: st.count(x), set(f)))
# s = sum([st.count(i) for i in set(st) if i.lower()[0] not in 'aeiou'])
# k = sum([st.count(i) for i in set(st) if i.lower()[0] in 'aeiou'])
# print("Stuart %s"%s if s > k else "Kevin %s"%k)