class solution(object):
    def vowels(self,s):
        r=""
        for i in s:
            if i in vowels:
                continue
            else:
                r=r+i
        print(r)

vowels=['a','A','e','E','i','I','o','O','u','U']
s="vowels"
obj=solution()
obj.vowels(s)
obj.vowels("aravind")