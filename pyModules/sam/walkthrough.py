import os
out=[]
# print(os.getcwd())
def walk(a):
	for i in os.listdir(a):
		if i.startswith('__') or i.endswith('.pyc'):
			continue
		if os.path.isfile(i):
			out.append(i)
		else:
			print(i)
			walk(i)
a=input("enter path:")
# print(type(a))
walk(a)			
print(out)
