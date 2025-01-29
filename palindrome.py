#to check the palindrome

def palindrome():
    char=input("enter the name to be checked if it is palindrome or not:")
    j=(len(char)-1)
    count=0
    #we are assigning the length to be half here
    for i in range(len(char)//2):
        #where i checks from start and j starts from end to check for the same characters
        if (char[i]!=char[j]):
            count+=1
            break
        #if not then j decrements
        j-=1
    if count==0:
        print("palindrome")
    else:
        print("not a palindrome")

palindrome()