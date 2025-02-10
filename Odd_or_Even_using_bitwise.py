#finding odd or even using bit operator
class number(object):
    def odd_or_even(self,n):
        #checks last bit of the number n
        if (n&1):
            print("odd number")
        else:
            print("even number")

obj=number()
obj.odd_or_even(3)
obj.odd_or_even(4)
num1=number()
n=int(input("enter a number:"))
num1.odd_or_even(n)
