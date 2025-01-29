#.You have a number to examine, and your mission is to write a program that checks 
#whether this number can be divided evenly by 27. Can you find out if it‟s a multiple of 27?
def is_multiple_of_27():
    num = int(input("Enter a number: "))
    #here checks if its divisible by 27 or not
    if num % 27 == 0:
        print(num,"is a multiple of 27.")
    else:
        print(num,"is not a multiple of 27.")

is_multiple_of_27()