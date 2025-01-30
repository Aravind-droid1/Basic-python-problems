#here its an game where its ruled by divisibility of 3 and 5
def fizz_buzz():
    n=int(input("enter the number to create fizz buzz:"))

    if n <= 0:
        print("Please enter a positive number")
        return

    for i in range(1,n+1):
        if( i % 3 == 0 and i % 5 == 0 ):
            print("fizzbuzz",end=" ")
        elif( i % 3 == 0 ):
            print("fizz",end=" ")
        elif( i % 5 == 0 ):
            print("buzz",end=" ")
        else :
            print(i,end=" ")

fizz_buzz()