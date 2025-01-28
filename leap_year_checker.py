#to chech if its an leap year or not
def leap_year():
    year=int(input("enter the year to check :"))
    #the condition checks if is it divisible by 4 then it should be divisible by 400
    #if its divisible by 400 it should be divisible by 100 too
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
         print(year,"is a leap year")       
    else:
        print(year,"is not a leap year")

leap_year()