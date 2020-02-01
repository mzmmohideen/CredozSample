from class_eg import ClassName

# print '>>>>', dir(ClassName)
class largest(ClassName):
	"""docstring for largest"""
	def __init__(self, arg=10):
		print '>>>>', dir(self)
		super(largest, self).__init__()
		self.arg = arg

a = largest()
print 'done'