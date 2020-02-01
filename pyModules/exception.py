a = "credo"
l = list(a)

try:
	b = 0
	b[0]
except (AttributeError, NameError, TypeError) as e:
	print(e.message)
else:
	print("There is no exception")
finally:
	print("Always")



exit()

try:
	print("TRY")
	l.update
	print("END")
# except IndexError, NameError:
except NameError as err:
	print("something wrong!", err.message)
	# print(error.__class__, error.__traceback__.tb_lineno)
	# print("something wrong!", error)
	# try:
	# 	print('some error', e)
	# except Exception as err:
	# 	print(err)
	print("I am here")
else:
	print("no exception!")
finally:
	print("Exception block completed")

print("??")

# print(dir(a))
# try:
# 	print('a', a)
# 	print("No error occured")
# except:
# 	print('some error')
# else:
# 	print('no exception found')
# finally:
# 	print('file ended')

