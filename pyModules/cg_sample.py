#!/usr/bin/python
# Importing the 'cgi' module 
# import cgi 
  
  
# print("Content-type: text/html\r\n\r\n") 
# print("<html><body>") 
# print("<h1> Hello Program! </h1>") 
# # Using the inbuilt methods 
  
# form = cgi.FieldStorage() 
# if form.getvalue("name"): 
#     name = form.getvalue("name") 
#     print("<h1>Hello" +name+"! Thanks for using my script!</h1><br />") 
# if form.getvalue("happy"): 
#     print("<p> Yayy! I'm happy too! </p>") 
# if form.getvalue("sad"): 
#     print("<p> Oh no! Why are you sad? </p>") 
  
# # Using HTML input and forms method 
# print("<form method='post' action='hello2.py'>") 
# print("<p>Name: <input type='text' name='name' /></p>") 
# print("<input type='checkbox' name='happy' /> Happy") 
# print("<input type='checkbox' name='sad' /> Sad") 
# print("<input type='submit' value='Submit' />") 
# print("</form") 
# print("</body></html>") 


# decorators


def hello_decorator(abc): 
    def inner1(*args, **kwargs): 
          
        print("before Execution", abc, args, kwargs) 
          
        # getting the returned value 
        returned_value = abc(*args, **kwargs) 
        print("after Execution", returned_value) 
          
        # returning the value to the original frame 
        return returned_value
    return inner1 
  
  
# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
    print("Inside the function") 
    return a + b 
  
a, b = 1, 2
  
# getting the value through return of the function 
print  sum_two_numbers(a, b)