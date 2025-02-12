#to find the unique number using xor from the array
class xor(object):
    def unique_number(self,n):
        unique=0
        for num in n:
            #the xor would keep on the correct difference between and when the repeated numbers comes it would cancels oyt the difference of that number
            unique=unique^num
        return unique
obj=xor()
print(obj.unique_number([1,2,3,5,3,5,1]))
print(obj.unique_number([9,0,1,4,6,2,0,4,9,6,2]))