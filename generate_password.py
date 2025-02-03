import random
#to create a random password
def generate_password():
    n=int(input("enter a number for first two numbers range to be"))  
    l=int(input("enter a number for next two alphbets to be ranged")) 
    #first and second would be determined by n
    first=random.randint(1,n)  
    second=random.randint(1,n)
    #third and fourth would be determined by l
    third=chr(random.randint(97,97 + l-1))
    fourth=chr(random.randint(97,97 + l-1))
    #fifth sould be greater than n so we are gathering >n in valid array
    valid=[]  
    for i in range(1,n+2):  
        if i>first and i>second:
            valid.append(i)
    if valid:  
        fifth=random.choice(valid)  
        print(first,second,third,fourth,fifth)
    else:  
        print("No valid password possible")  

generate_password()