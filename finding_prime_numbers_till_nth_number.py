#to find the prime number till the nth num
def prime(n):
    for num in range(2,n):
        flag=True
        #only to search till half the number
        for i in range(2,int(num/2)+1):
            if(num%i==0):
                flag=False
                break
        if flag==True:
            print(num,end=",")
n=100
prime(n)