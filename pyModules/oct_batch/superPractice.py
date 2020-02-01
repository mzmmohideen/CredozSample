class Validator:
   def auth(self, uname, pwd):
     if uname == 'admin' and pwd == '123':
       return {'token': '{}.{}#256'.format('@'.join(uname), '$'.join(pwd))}
 
class Login(object, Validator):
   def auth(self, uname, pwd):
     if uname == 'admin' and pwd == '123':
       return {'token': '{}{}'.format(uname, pwd)}
 
# Login().auth('admin', '123')

class Login(object, Validator):
   def auth(self, uname, pwd):
       return super(Login, self).auth(uname, pwd)
 
# Login().auth('admin', '123')

class Login(object, Validator):
   def auth(self, uname, pwd):
       res = super(Login, self).auth(uname, pwd)
       res['uname'] = uname
       res['pwd'] = pwd
       return res
 
# Login().auth('admin', '123')


try:
	a = 1
	if a == 10:
		print('Yes')
	str(a) + '10'
# except NameError as e:
# except Exception as e:
except (TypeError, NameError) as e:
	print('Something wrong', str(e))
else:
	print('No error')
finally:
	print("I am done")
print("move on")
