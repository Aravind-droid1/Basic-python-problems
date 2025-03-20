#print the list as by getting simutaneously
a=True
b=[]
while a==True:
    print("The number", len(b) + 1, "is: (or press Enter to stop)")
    c=input()
    if(c==""):
        break
    else:
        b.append(c)

for i in b:
    print(b)