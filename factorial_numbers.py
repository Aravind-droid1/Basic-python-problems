#to find the factorial number
def factorial():
    number = int(input("Enter a number: "))
    result = 1
    #here we are multiplying them as we continue to loop
    for i in range(2, number + 1):
        result *= i

    print(result)

factorial()