class sol(object):
    def array_mul(self,mul):
        a=[1,2,3,4,5,6,7,8,9,10]
        n=len(a)
        b=[0]*n
        for i in range(n):
            b[i]=a[i]*mul
        print(b)

mul=int(input("enter the multiplication: "))
obj=sol()
obj.array_mul(mul)