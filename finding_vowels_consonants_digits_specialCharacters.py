
n=list(input())
vowels=['a','e','i','e','o','A','E','I','O','U']
specialCharacter=['!','@','#','$','%','^','&','*','_']
digits=['0','1','2','3','4','5','6','7','8','9']
v=[]
c=[]
d=[]
s=[]
for i in range(len(n)):
    if n[i] in vowels:
        v.append(n[i])
    elif n[i] in digits:
        d.append(n[i])
    elif n[i] in specialCharacter:
        s.append(n[i])
    else:
        c.append(n[i])
print("vowels:",v)
print("consonants:",c)
print("numbers:",d)
print("special characters:",s)