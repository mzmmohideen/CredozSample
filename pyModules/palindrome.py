# print(1)
a=raw_input("enter the string")
# a=a.reverse()
if a==a[::-1]:
	print('is a palindrome')
else:
	print('not a palindrome')


# a = { 1 : 'one' , 2 : 'two' , 3 : 'three' , 4 : 'four' , 5 : 'five'}
# U = raw_input('enter the value')
# for i in a.items():
# 	#print i
# 	if U==i[1]:
# 		print i[0] 

# SO question
# prefetch = range(100)
# stride=0
# sub1=0
# sub2=0
# for i, v in enumerate(prefetch):
#     if prefetch[1]==0:
#         prefetch[1]=prefetch[i]
#     for j in range(1,len(prefetch)):
#         sub1=prefetch[i]
#         sub2=prefetch[j]
#         if prefetch[i]==prefetch[j]:
#             confidence+=1
#         else:
#             stride=sub1-sub2
#             if i+stride < len(prefetch):
#             	newaddr=prefetch[i+stride]
#             confidence=0
# print('prefetch', prefetch)
# print('confidence', confidence)
# print('sub1', sub1)
# print('sub2', sub2)
# print('newaddr', newaddr)