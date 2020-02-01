class A(object): # this is a sample class 
	def sum(self, a, b):
		return a + b

class B(A):
	def sum(self, a, b):
		print(super(B, self).sum(a, b))
		return a - b

# print(B().sum(1, 2))


class Auth(object):
	username = "credo"
	password = "123credo123"
	def login(self, username, password):
		if username == self.username and password == self.password:
			return "Login Succesfull"
		return "Login Failed"

class Student(Auth):	
	def login(self, username, password):
		password = "123{}123".format(password)
		a =  super(Student, self).login(username, password)
		return a
		# if username == self.username and password == self.password:
		# 	return "Login Succesfull"
		# return "Login Failed"

# print(Student().login('credo', 'credo'))

# class Employee:



# try:
#   a  = '100'*'100'
#   if a == 100:
#     pass
# except (TypeError, NameError, AttributeError) as err:
#   print("Error occured", err)
# else:
# 	print("No exception")
# finally:
# 	print("I am done")

a=10
i = input("Enter number between 0-10:")
i = int(i)
d = {
		0: 'zero',
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five'
	}
# print(d.get(i))
# if d.get(i) == 'one':
if i <= 5:
	print(d[i])
else:
	print('Not exist')