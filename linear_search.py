#to implement linear search algorithm
def finds(nums,finding):
    for i in range(len(nums)):
        #it works as the normal for loop method to find value
        if nums[i]==finding:
            return i
    return -1

nums=[0,1,2,3,4,5,6]
finding=5
result=finds(nums,finding)

if result !=-1:
    print("num found at ",result)