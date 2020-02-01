"""
This is sample modules
"""
print("hi hello")

a = 10
b = 20
def sample():
    """
    this is a sample function
    """
    if True:
        return 5
    
    return "Good moring"
    
print("module name is:", __name__)
if __name__ == "moduleA":
    print("I am executed from moduleA")
    print(sample())
else:
    print("import restrict")