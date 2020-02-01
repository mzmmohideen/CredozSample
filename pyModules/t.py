import sys
# a = input("Enter your number a:")
# b = input("Enter your number b:")
print(sys.argv)
# exit()
# a = int(sys.argv[1])
# b = int(sys.argv[2])
# print "Addition of a+b is:", a+b, "and the type is: ", type(a+b)

# inp = 

def palidrome(inp):
	if len(inp) <= 1:
		return "Insufficient Input!"
	inp = inp[1]
	if inp == inp[::-1]:
		return "It is a Palindrome!"
	return "Its not a Palindrome!"

print(palidrome(sys.argv))


# import random
# loop = 1

# while loop:
#     print loop, "Dice faces are ", random.randint(1, 6)
#     loop += 1
#     # loop = loop +1 
#     if loop == 1000:
#     	loop = 0
    # import randominp = raw_input("Are sure you want roll dice again? Y/N")
    # if inp.lower() != 'y':
    # 	loop = False

# import random

# num = str(random.randint(1000, 9999))
# # print "random number", num
# loop = 1

# while loop:
# 	inp = list(raw_input("Enter your Number:").replace(" ",''))

# 	print "before", inp

# 	if len(inp) != 4:
# 		print "Input should be 4 Digit!"
# 		break

# 	for i in range(4):
# 		if inp[i] == num[i]:
# 			inp[i] = 'cow'
# 		elif inp[i] in num:
# 			inp[i] = 'bull'

# 	loop+=1

# 	print "after", inp
# 	if inp.count('cow') == 4:
# 		print "You won! you took %s times to Solve!"%loop
# 		loop = 0



