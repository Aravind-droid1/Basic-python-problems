#to find the sum of digits using recursion method
def sum_of_digits(n,result=0):
    if n == 0:
        return result
    #result+remainder then the before numbers to be in n
    return sum_of_digits(n//10,result+(n%10))

n = int(input("Enter number: "))
print("Sum of digits:",sum_of_digits(n))