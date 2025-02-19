#to try the split built-in function with the program for ip address
class solution(object):
    def split(self,s):
        #it splits it up into array whenever it encounters "."
        a=s.split(".")
        for i in range(len(a)):
            num=int(a[i])
            if  num < 255 :
                continue
            else:
                return False
        return True
                                                                      
#fixed numers
obj=solution()
print(obj.split("123.456.789"))
print(obj.split("123.231.213"))
