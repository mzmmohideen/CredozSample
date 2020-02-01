class UserChoice:
    def odd_or_even(self,num):
        if (num%2==0):
            print ("Even")
        else:
            print ("Odd")
    def divisible_or_not(self,a,b):
        if(a%b==0):
            print ("Divisible")
        else:
            print ("Non Divisible")
    def fib(self,num):
        f=0
        s=1
        b = [f,s]
        if num<=0:
           return ("Invalid Sequence")
        else:
            for x in range(2,num):
                temp=f+s
                f=s
                s=temp
                b.append(temp)
        print b
    def upperlower(self,name):
        l = []
        for i in name:
            if i.islower():
                 a =  i.upper()
                 l.append(a)
            else:
                 b = i.lower()
                 l.append(b)
        s = ''.join(l)
        print (s)
    def palin(self,a):
        rev = a[::-1]
        if (a == rev):
            print ("Palindrome")
        else:
            print ("Not a Palindrome")


class inp:
    def user(self):
        a = int(input("select 0 for fibbinocci, 1 for prime, 2 for palin: "))
        terms = int(input("how many terms u need me to generate: "))
        nums = int(input("Enter the number"))
        if a == 0:
            return terms
        elif a == 1 or a == 2:
            return nums

class fibbinocci:
    def fibbi(self,terms):
        b = 0
        c = 1
        f = -1
        if (terms == 1):
            print(b)
        elif (terms == 0):
            print("You have no sense")
        elif (terms < 0):
            print ("FIBONACCI HERE IT GOES")
            print(b)
            print(f)
            for i in range(1, -terms):
                g = b + f
                b = f
                f = g
                print (f)
        else:
            print ("FIBONACCI HERE IT GOES")
            print (b)
            print (c)
            for i in range(1, terms):
                d = b + c
                b = c
                c = d
                print (d)
class prime:
    def prm(self,nums):
        for i in range(2,nums):
            if nums % i == 0:
                print ("Its not a prime number")
                break
        else:
            print ("Its prime")

class palindrome:
    def palindrome1(self, nums):
        if nums[::-1] == nums:
            print ("it is a palindrome")
        else:
            print ("it is not a palindrome")


if __name__ == "__main__":
    user = "nivetha"
    if user == "nivetha":        
        cls = UserChoice()
        choice = int(input("""
                Enter your Choice :
                    1. Odd/Even
                    2. Divisible/Not Divisible
                    3. Fibonacci
                    4. Upper/Lower
                    5. Palindrome/Not Palindrome

        """))

        if choice == 1 or choice == 2 or choice == 3:
            number = int(input(("Enter a number : ")))

        if choice == 1:
            cls.odd_or_even(number)
        elif choice == 2:
            num2 = int(input("Enter number to divide"))
            cls.divisible_or_not(number,num2)
        elif choice == 3:
            cls.fib(number)
        elif choice == 4:
            n = input("Enter a string to change its case : ")
            cls.upperlower(n)
        elif choice == 5:
            ispal = input("Enter a string to check whether its Palindrome or not : ")
            cls.palin(ispal)
        else:
            raise ValueError ("Wrong Choice Program Terminated")
    elif user == "siva":
        cls_inp = inp.user(self)
        cls1 = fibbinocci.fibbi(terms)
        cls2 = prime.prm(nums)
        cls3 = palindrome.palindrome1(nums)
