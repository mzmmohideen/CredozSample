# # #print "Hello World!"
# # import session

# # print help(session.ab)
# # def a():
# # 	print 5

a = 100
c = 0

def add(b):
   global c  #"it will simply print what present inside"
   print 'a is,', a 
   c=a+b

print 'before', a

def sub():	
	print 'print c', c



add(200)
sub()
# a = 10
# b = 100
# fun1(b)