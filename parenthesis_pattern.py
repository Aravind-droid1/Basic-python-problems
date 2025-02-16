#to print the parenthesis pattern number of times
class para(object):
    def parenthesis(self,n):
        for i in range(1,n+1):
            for j in range(i+1):
                print('{'*j,'}'*j,end=" ")
            print()

obj=para()
obj.parenthesis(5)
