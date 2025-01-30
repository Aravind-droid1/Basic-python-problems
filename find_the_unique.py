'''Given a non-empty array of integers nums, every element appears twice except for one.
   Find that single one.''' 
def singleNumber(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)): 
            if nums[i] == nums[j]:
                count += 1
                #if count exceeds 1 its an repeat
        if count == 1: 
            return nums[i]

nums = list(input("enter the numbers: "))#2 3 4 2 4
output = singleNumber(nums)
print(output)
