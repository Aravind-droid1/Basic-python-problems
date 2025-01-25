n=list(input())
vowels=['a','e','i','e','o','A','E','I','O','U']
specialCharacter=['!','@','#','$','%','^','&','*','_','.',',',';',':']
v=[]
c=[]
d=[]
s=[]
for i in range(len(n)):
    if n[i] in vowels:
        v.append(n[i])
    elif (48<=ord(n[i])<=57):
        d.append(n[i])
    elif n[i] in specialCharacter:
        s.append(n[i])
    elif((n[i]!=vowels) and (65<=ord(n[i])<=90 or 97<=ord(n[i])<=122)):
        c.append(n[i])
print("vowels:",v)
print("consonants:",c)
print("numbers:",d)
print("special characters:",s)