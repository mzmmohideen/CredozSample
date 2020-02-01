# #! /usr/bin/python3
# import random
# import fibo

# print (help(random))
# def squre(a):
#     """
#        This is squre function. this will return square value of given integer. formula was n*n
#        Here n represents number (User input)
#     """
#     return a*a


# def fiborec(n, out=[1,2]):
#    print 'working'   
#    if n-2 == 0:     
#      return out
#    out.append(out[-1]+out[-2])
#    return fiborec(n-1, out)


# if __name__ == "__main__":	
# 	print fiborec(5)	
# else:
# 	print squre(1)
# 	print fibo.gcd(10, 20)

"""
x = 10
y = 20
"""

d = {
  "apple": 4,
  "orange": 5,
  "banana": 6
}

inp = raw_input("Enter Fruit Name:")
# inp = input("Enter some Number:")

# if inp.isdigit() and int(inp) < 50:
#   print(int(inp) * int(inp))

if inp.isalpha() or 'p' in inp:
  print("exist", d[inp])
# else:
# print(inp)
# inp = "apple"

# if inp in d:
#   print("value is", d[inp])
# else:
#   print("Not Found!")
# if d.get(inp):
#   print( inp + " count is= " + str(d[inp]))
# else:
#   print("Given fruit is Not Found!")