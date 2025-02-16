
a=[1,10,23,10,5]
b=[]
count=0
for i in range(len(a)):
    if (a[i]%10 != 0):
        b.append(a[i])
    else:
        count+=1
for i in range(count):
    b.append(0)

print(b)