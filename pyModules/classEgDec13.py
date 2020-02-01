class Calc2:
    def sum(self):
      return 1 + 2000
 

class Calc:
   def sum(self):
     print('Initiated')
     return 10 + 2


# class Calc1(Calc, Calc2, object):
#    def sum(self):
#       out = super(Calc1, self).sum()
#       print('done')
#       return 1 + 2000
 
class Calc1(Calc, Calc2, object):
   def sum(self):
      out = super(Calc2, self).sum()
      print('done')
      return out - 2


print(Calc1().sum())
