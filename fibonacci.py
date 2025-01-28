#to find the fibonacci series
def fibonacci():
    number=int(input("enter the number of times the series to be conducted:"))
    a=0
    b=1
    #for the given number of series the loop will run and gives added values with the previous value
    for i in range(number):
        print(a,end=" ")
        a,b=b,a+b

fibonacci()