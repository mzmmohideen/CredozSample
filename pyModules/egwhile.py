# a = 1
# while a:	
# 	a+=1
# 	print 'a', a
# 	if a == 100:
# 		a = 0

# print "final value", a


"""
Hi this is sample Doc about my module egwhile
"""
import random as r
min, max = 1, 6
r_again = 'y'
while r_again == 'y':
	print "Rolling the dices... \n the values are..."
	print r.randint(min, max), r.randint(min, max)
	# r_again+=1
	# if r_again > 100:
	# 	r_again = 0
	r_again = raw_input("Roll the dices again? (y/n)")