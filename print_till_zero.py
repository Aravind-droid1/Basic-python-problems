#this code prints values till 0 regardless of the position of the number either positive or negative
def zero_converter():
    def negative(n):
        while n <= 0:
            print(n, end=" ")
            n += 1
        #for positive numbers to be printed
    def positive(n):
        while n >= 0:
            print(n, end=" ")
            n -= 1

    n = int(input("Enter a number (positive or negative): "))
    if(n<0):
        negative(n)
    else:
        positive(n)

zero_converter()