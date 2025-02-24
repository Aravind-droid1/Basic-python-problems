#character sequence
#to find the highest word used in a string given
class sol(object):
    def sequence(self,n):
        s=n.split(" ")
        maxi=0
        selected=0
        for i in range(len(s)):
            count=0
            for j in range(i+1,len(s)):
                #if i and i+1 are equal it would count +1 and decides which is max
                if (s[i] == s[j]):
                    count+=1
            if (count > selected):
                    selected = count
                    maxi = i
        return s[maxi]

n=input("enter a sequence of words:")
obj=sol()
print(obj.sequence(n))