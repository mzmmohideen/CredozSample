def iam_decorator(func): 
    print 'func', func # first
    def subfunc(*args, **kwargs): 
        print 'args before modification', args   #second
        args = [i*2 for i in args] 
        print 'args after modification', args #thrid
          
        # getting the returned value 
        returned_value = func(*args, **kwargs) 
        print("after Execution", returned_value) #fifth
          
        # returning the value to the original frame 
        return returned_value 
    
    print 'before execution'
    return subfunc 
  
  
# adding decorator to the function 
@iam_decorator
def sum_two_numbers(a, b): 
    print("Inside the function") #fourth
    return a + b 
  
a, b = 1, 2
  
# getting the value through return of the function 
print("Sum = %s"%sum_two_numbers(a, b)) #sixth last