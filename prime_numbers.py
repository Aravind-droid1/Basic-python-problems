#to find if a number is prime or not
def prime_number():
    num = int(input("enter the number to be checked if prime number or not:"))
    count = 0
    #if prime number it should only be divisible by only two numbers(1 and by itself)
    for i in range(1, num + 1):
        #if divided it takes adds one to count
        if num % i == 0: 
            count += 1
    #if count exceeds 2 its not an prime number
    if count == 2:
        print(True)  
    else:
        print(False)

prime_number()