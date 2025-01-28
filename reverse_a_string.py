#to reverse a string
def string_reverse():
    string=input("enter the string to be reversed:")
    #create a empty string data type variable tom store reversed strings
    reversed=""
    for i in string:
        #now the string would be reversed 
        reversed=i + reversed
    print("reversed string=",reversed)

string_reverse()