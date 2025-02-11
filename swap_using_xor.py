class xor(object):
    def swap(self,a,b):
        #at first time doing xor it would create an common number between two
        #second time doing xor with new a , b would get to a's old value
        #by doing third time xor with new b , a would get the b's old value
        a=a^b
        b=a^b
        a=a^b  
        print("a=",a,"b=",b)

offf=xor()
offf.swap(5,7)