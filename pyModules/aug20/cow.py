def method1():
    import random as r
    a=str(r.randint(1000,9999))
    # a = '5005'
    # print(a)
    # def cowbull():
    inp = True
    count = 0
    while inp:
        count += 1
        # count = count + 1
        b=list(raw_input("enter a 4 digit number:").replace(" ", ""))
        for i in range(4):
            if a[i]==b[i]:
                b[i]="cow"
            elif b[i] in a:
                b[i]="bull"
        print b    
        if b.count("cow")==4:
            # return 'success'
            inp = False

    print("Success! You took %s try!"%count)

def method2():
    import random as ran
    x = str(ran.randint(1000,9999))
    inp=True
    counter=0
    while inp:
        y = list(raw_input("Enter the input value:"))
        for i in range(4):
            if x[i] == y[i]:
                y[i] = "cow"
            elif y[i] in x:
                y[i] = "bull"
        print (y)
        counter +=1
        if y.count("cow") == 4:
            inp = False
    print("count", counter)

# 

def fibonacci():
    n=input("enter the number of sequence")
    # n=int(n)
    n1=0
    n2=1
    if n<0:
        print(("enter the positive number"))
    elif n<=1:
        print(n)
    else:
        print(n1)
        print(n2)
        for i in range(2,n):
            nth=n1+n2
            n1=n2
            n2=nth
            print(nth)


def fibo(n=10, met=1):
    out = [0, 1]
    if n < 1:
        print("positive integer required!")
    elif n < 3:
        print(out[:n])

    if met == 1:

        # method 1
        for i in range(n-2):
            out.append(out[-1]+out[-2])
    else:
        # method 2
        counter = 2
        while n:
            counter+=1
            out.append(out[-1]+out[-2])
            if counter == n:
                n = False
    return out

def fiboo(n, m=1):
    return n+m

# print(fiboo(1, 10))
# a = fibo()
# print(a)

def hello(a, b, c, *args, **kwargs):
    print('n is', a, kwargs, args)
    return kwargs

a = 1
def hello1(*args, **kwargs):
    global a, b
    a = 10
    b = 1
    # b,c = 10,20
    print('a is', a)
    return sum(args)

# print('a', a)
# print(hello1(100, 200, 5, 1, 2, 3, 5, 4))
# print('outside a', a, b)
# print(hello(a = 10, b =  20, c =  30, d =  40, e =  50))
# print(hello(10,  20,  40,  50, e=30, d= 40))

def fibo(n=10):
    out =[0,1]
    for i in range(n-2):
        out.append(out[-1] + out[-2])
        print(i, 'length', out)
    return out
# a = fibo(15)
# print(a)
method2()