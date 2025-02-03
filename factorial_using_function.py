def factorial(num):
    #here the code would iterate with the number keep decreasing till it reaches 0 or 1
    if num==0 or num==1:
        return 1
    #the here it keeps on calling functions aand multiplies with them
    return num * factorial(num-1)

num=int(input())
print(factorial(num))


#optimized version using python package
import math
def factorials():
    nums=int(input())
    print(math.factorial(nums))

factorials()