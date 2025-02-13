#to finf the unque and duplicate values in an array
def singleNumber(nums):
    u=[]
    d=[]
    v=[]
    for i in range(len(nums)):
        count = 0
        if nums[i] in v:
            continue
        for j in range(len(nums)): 
            if nums[i] == nums[j]:
                count += 1
                v.append(nums[i])
                #if count exceeds 1 its an repeat
        if count == 1:
            u.append(nums[i])
        else:
            d.append(nums[i])
    print(u)
    print(d)
    
nums = list(input("enter the numbers: "))#2 3 4 2 4 5
singleNumber(nums)