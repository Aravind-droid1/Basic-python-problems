#creating a calculator

#creating a function calculator with first number , second number and operator to assign 
# which calculation to be done when it calls the assigned function
def calculator(number1,number2,operator):
    return operator(number1,number2)
#create multiple functions to calculating the function can be called by calculator
def addition(number1,number2):
    return number1+number2

def subtraction(number1,number2):
    return number1-number2

def multiplication(number1,number2):
    return number1*number2

def division(number1,number2):
    return number1/number2
#calling the calculator function
calculator(1,2,addition)