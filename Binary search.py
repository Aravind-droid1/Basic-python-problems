
#Question: Given a sorted array arr and an integer k, find the position(0-based indexing) at which k is present in the array using binary search.

def binarySearch(arr, k):
    left, right = 0, len(arr) - 1
    result = -1  # To store the smallest index of k
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == k:
            result = mid  # Store the index
            right = mid - 1  # Continue searching on the left side for the first occurrence
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

arr1 = [1, 2, 3, 4, 5]
k1 = 4
print(binarySearch(arr1, k1))  

arr2 = [11, 22, 33, 44, 55]
k2 = 445
print(binarySearch(arr2, k2))  

arr3 = [1, 1, 1, 1, 2]
k3 = 1
print(binarySearch(arr3, k3))  
