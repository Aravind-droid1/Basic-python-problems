#Binary search algorithm
def binary_search(a,n):
    #sort the given numbers first
    a.sort()
    low=0
    high=len(a)-1
    while low <= high:
        #mid would be the middle number
        mid=(low + high)//2

        if a[mid]==n:
            return mid
        elif a[mid] < n:
            low=mid+1
        else:
            high=mid-1
    return -1

a=[1,3,2,5,4]
n=4
result=binary_search(a,n)
if result>=0:
    print ("successfully found ",n)
else:
    print("not found",n)