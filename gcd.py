def gcd():
    num1=int(input())
    num2=int(input())
    if(num1<num2):
        num1,num2=num2,num1
    for i in range(num2,0,-1):
        if (num1%i==0 and num2%i==0):
            break

    print(i)

gcd()