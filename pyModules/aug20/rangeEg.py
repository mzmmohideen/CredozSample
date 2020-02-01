
def getlen(inp):
    count = 0
    for i in inp:
        count +=1
    return count

def range(*a):
    start, step = 0, 1
    out = []
    if getlen(a) == 1:
        stop = a[0]
    elif getlen(a) == 2:
        start, stop = a
    elif getlen(a) == 3:
        start, stop, step = a
    else:
        # "range function required atmost 3 arguments!"    
        raise TypeError('range function required atmost 3 arguments!')
    while start < stop:
        print('start', start, stop, step, out)
        out.append(start)
        start = start + step
    return out

print(range(20))

def mapping(func, iter):
    out = []
    for i in iter:
        out.append(func(i))
    return out

def filtering(func, iter):
    out = []
    for i in iter:
        if func(i):
            out.append(i)
    return out

def reducing(func, iter):
    out = ''
    for i,v in enumerate(iter):
        if i == 0:
            out = func(v, iter[1])
        elif len(iter) != (i+1):
            out = func(out, iter[i+1])
        else:
            return out

# print(reducing(lambda x,y: x * y, [1,2,3,4,5,6, 7, 8]))

# print(map(lambda x: x*x, [1,2,3]))
# print(filtering(lambda x: x%2, [1,2,3,4,5]))
# print(filter(lambda x: x%2, [1,2,3,4,5]))


# def p(*args):
#     if args.__len__()==1:
#         count=0
#         while count<args[0]:
#             print(count)
#             count+=1
#     elif args.__len__()==2:
#         print(args)
#         count=args[0]
#         while args[0]<=count<args[1]:
#             print(count)
#             count+=1
#     elif args.__len__()==3:
#         count=args[0]
#         while args[0]<count<args[1]:
#             print(count)
#             count+=args[2]
# # print(p(1,5))            
# def l(*args):
#     i=1
#     for i in range(args[-i]):
#         print(i)
#         i+=1
# print(l(1,2))        
