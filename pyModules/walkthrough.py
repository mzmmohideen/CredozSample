import os
out=[]
# print(os.getcwd())
def walk(a):
	# print('first', out)
	# out = out
	for i in os.listdir(a):		
		file_path = a+'/'+i
		if i.startswith('__') or i.endswith('.pyc'):
			continue
		if os.path.isfile(file_path):
			out.append(file_path)
		elif os.path.isdir(file_path):
			print(i, 'i')
			walk(file_path)
		else:
			print("wrong", i)
		# return out
a=input("enter path:")
# print(type(a))
print(walk(a))
print(out)
