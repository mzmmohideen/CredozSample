class Sample:
    def auth(self, uname, pwd):       
       return "Nothing happened!"

class Login:
    def auth(self, uname, pwd):
       if uname == 'user' and pwd == '123':
           return "Login Successful!"
       return "Login Failed"
 
 
class Auth(Login, Sample):
    pass
    def auth(self, uname, pwd):     
        if not isinstance(uname, str):
           uname = str(uname)
        if not isinstance(pwd, str):
           pwd = str(pwd)
        # return "Nothing happened"
        # if uname == 'user' and pwd == '123':
        #    return "Login Successful!"
        # return "Login Failed"
        return super(Auth, self).auth(uname, pwd)

cls = Auth()
print(cls.auth('user', 123))


def exceptionEg():
    try:
        inp = input("Enter your Age:")
        print(int(inp))
    except NameError:
        print("soemthing wrong")
    else:
        print("No Exception occurs")
    finally:
        print("I am done")

# exceptionEg()
