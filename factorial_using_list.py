def factorial():
    num=int(input("give a number to be factorized"))
    #creating number of list space needed with(num+1) and filled all with 1
    fact=[1]*(num+1)
    for i in range(2,num+1):
        #now the previous and current values are multiplied and filled inside by over writting that 1
        fact[i]=i*fact[i-1]
    print(fact[num])

factorial()

#optimized method
def factorials():
    num=int(input("give another number or give same number to check"))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)

factorials()