#You have two numbers, and your challenge is to write a program that performs both 
#addition and subtraction with them. However, if any subtraction results in a negative 
#number, display it as a positive value. How will you tackle this and show the final results?

def add_and_subtract():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    addition= num1 + num2
    #if the second number is greater we are swapping number one and two to avoid getting the negative number
    if num1 < num2:
        num1, num2 = num2, num1
    #it results the same as we get other than the negative sign
    subtraction= num1 - num2

    print("Addition result:",addition)
    print("Subtraction result:",subtraction)

add_and_subtract()
