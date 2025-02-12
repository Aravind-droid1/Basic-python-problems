#to convert to opposite signed number using multiple functions
class number(object):
    def find(self,n):
        if(n<0):
            self.negative_to_positive(n)
        else:
            self.positive_to_negative(n)

    def negative_to_positive(self,n):
        #not symbol would change the sign and to one number less than the current number so we add 1
        n=~n+1
        print(n)

    def positive_to_negative(self,n):
        #for negative it would give number extra so we add one to less it i negative sign
        n=(~n+1)
        print(n)

obj=number()
obj.find(-5)
obj.find(5)