class bitwise_operators(object):
    def and_operator(self,a,b):
        #gives 1 if both have 1
        print("and operator",a,",",b,"=",a & b)

    def or_operator(self,a,b):
        #gives 1 if even one of them has 1
        print("or operator",a,",",b,"=",a | b)
    
    def xor_operator(self,a,b):
        #gives 1 if both are different
        #gives 0 if both of them has same
        print("xor operator",a,",",b,"=",a ^ b)
    
    def not_operator(self,a,b):
        #gives opposite signed number and if + is given then it gives - value plus one number(5 -> -6)
        #then for - is given it gives + value minus one number (-5 -> 4)
        print("not operator",a,"=",~a)
        print("not operator",b,"=",~b)

    def left_shift(self,a):
        #it multiplies by 2 (nx2)
        print("left shift operator",a,"=",a << 1)

    def right_shift(self,b):
        #it divides by 2 (n//2)
        print("right shift operator",b,"=",b >> 1)

obj=bitwise_operators()
obj.and_operator(3,6)
obj.or_operator(3,7)
obj.xor_operator(3,6)
obj.not_operator(5,-5)
obj.left_shift(6)
obj.right_shift(7)