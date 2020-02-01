import random
x = str(random.randint(1000,9999))
a = True
z = 0
print('x', x)
while a:
    y = list(raw_input('enter the no: '))
    for i in range(0,4):
      if x[i]==y[i]:
        y[i]= 'cow'
      elif x[i] in y:
        y[i]= 'bull'
    print(y)
    z+= 1
    if y.count('cow')== 4:
        print(z)
        a= False

# if True:
#     print(1)
#     pass
#     print(2)

# def function():
#     pass