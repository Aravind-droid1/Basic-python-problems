# it prints the * in square type
n=int(input())
for i in range(n*n):
    print("*",end=" ")
    if ((i+1)%n==0):
        print()