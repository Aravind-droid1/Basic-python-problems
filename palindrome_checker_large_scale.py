'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
   removing all non-alphanumeric characters, it reads the same forward and backward. 
   Alphanumeric characters include letters and numbers. Given a string s, return true
   if it is a palindrome, or false otherwise.''' 

def isPalindrome(s):
    filtered_str = ""
    #to take in string and filtered out
    for char in s:
        if ('a' <= char.lower() <= 'z'):
            filtered_str += char.lower()
    
    left = 0
    right = len(filtered_str) - 1
    while left < right:
        if (filtered_str[left] != filtered_str[right]):
            return False
        left += 1
        right -= 1
    
    return True

input_string = input("Enter a string: ")

result = isPalindrome(input_string)

print(result)
