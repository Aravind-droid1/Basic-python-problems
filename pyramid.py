#for building a pyramid
#type1
def pyramid_type1():
    n = int(input("number of rows to be printed"))
    for i in range(n):
        print(" "*(n-i-1),"* "*(i+1))
#type2
def pyramid_type2():
    n = int(input("number of rows to be printed"))
    k=1
    m=n-1
    for i in range(1,n+1):
        print(" "*m,"*"*(k))
        k+=2
        m-=1

pyramid_types = {1: pyramid_type1, 2: pyramid_type2}

choice = int(input("Enter 1 for Pyramid Type 1 or 2 for Pyramid Type 2: "))
if choice in pyramid_types:
    pyramid_types[choice]()
else:
    print("Invalid choice")