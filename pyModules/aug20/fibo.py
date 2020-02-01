def fib(n):
     a,b = 0,1
     l =[a,b]
     # print(a,b)
     
     	
     	
     for i in range(n-2):
          # c= a+b
          # a = b
          # b = c
          l.append(l[-1]+l[-2])
          # print(c)
     return l
# print(fib(10))

def myList(inp):
	out = []
	iter, comp = inp
	for i in iter:
		out.extend([[i, l] for l in comp if i in l])
	return out

val = [["yes","no"],["ifyes","ifyes2","ifno"]]
print(myList(val))

