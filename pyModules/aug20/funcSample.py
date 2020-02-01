def min(a):
      m = a[0]
      for i in a:
         if i<m:
            m=i
      return m      

# print min([9,3,5,8,7])

def len(s):
    count = 0
    for i in s:
        count+=1

    return count

# print(len("sanjay"))
def list(l):
    # a = []
    # for i in l:
    #   a.append(i)
    # return a
    return [i for i in l]
t = (1,2,3,4,5,6,7)
# print(list("manas"))

def dict(k):
    d = {}
    for i in k:
        if len(i)!=2:
            return "type error:invalid input"
        d[i[0]] = i[1]
    return d
v = dict(((0,"a"), (1,"n"), (2, "w") , (3,"a"), (4, "r")))   
print(v)

def max(a):
    m = a[0]
    for i in a:
        if i>m:
            m=i
    return m
print(max([1,2,3,4]))

