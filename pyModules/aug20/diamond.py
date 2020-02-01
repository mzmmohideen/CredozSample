def diamond():
   #start, counter = input().split() # enable incase of python 3
   start, counter = raw_input().split() # disable incase of python 3 
   l = []
   for i in range(1, int(counter)+1):
    l.append(i*start)
    start = str(int(start)+1)
   l = l+l[:-1][::-1]
   # to print
   for j in l:
       print(j)
   return l

# diamond()

def diamondSameNum():
   #start, counter = input().split() # enable incase of python 3
   val = raw_input() # disable incase of python 3 
   l = []
   for i in range(1, int(val)+1):
    l.append('*'.join(str(i)*i))
   l = l+l[::-1]
   # to print
   for j in l:
       print(j)
   return l

diamondSameNum()