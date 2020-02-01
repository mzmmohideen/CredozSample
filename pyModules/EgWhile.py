# import random
# loop = 1

# while loop:
#     print loop, "Dice faces are, {} {}".format(random.randint(1, 6), random.randint(1, 6))
#     loop += 1
#     if loop == 1000:
#     	break
#     # import randominp = raw_input("Are sure you want roll dice again? Y/N")
#     # if inp.lower() != 'y':
#     # 	loop = False

import random

num = str(random.randint(1000, 9999))
print("random number", num)
loop = 1

while loop:
	inp = list(input("Enter your Number:").replace(" ",''))

	print("before", inp)

	if len(inp) != 4:
		print("Input should be 4 Digit!")
		break

	for i in range(4):
		if inp[i] == num[i]:
			inp[i] = 'cow'
		elif inp[i] in num:
			inp[i] = 'bull'

	loop+=1

	print("after", inp)
	if inp.count('cow') == 4:
		print("You won! you took %s times to Solve!"%loop)
		loop = 0



