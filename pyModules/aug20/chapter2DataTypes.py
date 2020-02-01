# Variable Declarations

age = 20 # int

name = "Credo System" # str

# Integer
age = 10
print(dir(age))
print(age.denominator)
print(age.numerator)
print(age.numerator)
print(age)
print(age.__add__(10))
print(age)
age = age.__add__(10)
print(age)

# Float
height = 5.5
print(height)
print((1.0).is_integer())

#string
name = 'manas'
name.capitalize()
'Manas'
print(name.center(15))
'     manas     '
print(name.center(15, '*'))
'*****manas*****'
print(name.center(15, '#'))
'#####manas#####'
print(name.center(15))
'     manas     '

s = 'hi hello how are you! I am good'
s[len(s)-1]
'd'
s[0]
'h'
s[-1]
'd'
s[-2]
'o'
s
'hi hello how are you! I am good'
s[-3]
'o'
s.index('h')
0
s[0]
'h'
s[-1]
'd'
s
'hi hello how are you! I am good'
s[0:9]
'hi hello '
s[0:9]
'hi hello '
s
'hi hello how are you! I am good'
s.capitalize()
'Hi hello how are you! i am good'
help(s.capitalize())
s[0:9]
'hi hello '
dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(s.join)

''.join(s)
'hi hello how are you! I am good'
'*'.join(s)
'h*i* *h*e*l*l*o* *h*o*w* *a*r*e* *y*o*u*!* *I* *a*m* *g*o*o*d'
''.join(s)
'hi hello how are you! I am good'
'-'.join(s)
'h-i- -h-e-l-l-o- -h-o-w- -a-r-e- -y-o-u-!- -I- -a-m- -g-o-o-d'
s.islower()
False
s.index('h')
0
help(s.index)

s[0]
'h'
s.index('a')
13
s[13]
'a'
s.upper()
'HI HELLO HOW ARE YOU! I AM GOOD'
s
'hi hello how are you! I am good'
s
'hi hello how are you! I am good'
s.split()
s.split()
['hi', 'hello', 'how', 'are', 'you!', 'I', 'am', 'good']
s
'hi hello how are you! I am good'
s.split('e')
['hi h', 'llo how ar', ' you! I am good']
s.split()
['hi', 'hello', 'how', 'are', 'you!', 'I', 'am', 'good']
s.split(' ')
['hi', 'hello', 'how', 'are', 'you!', 'I', 'am', 'good']
s.split(' ', 3)
['hi', 'hello', 'how', 'are you! I am good']
s.split(' ')
['hi', 'hello', 'how', 'are', 'you!', 'I', 'am', 'good']
s.split()
['hi', 'hello', 'how', 'are', 'you!', 'I', 'am', 'good']
s.split('o')
['hi hell', ' h', 'w are y', 'u! I am g', '', 'd']
s
'hi hello how are you! I am good'
dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


