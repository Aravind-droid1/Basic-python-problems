#Question:  Anagram Checker
#Problem Statement: Aman challenged his friend Ravi to check whether two given strings are anagrams or not. 
#(Two given strings are anagrams if both the strings contain the same characters in the same frequency). 
#Your task is to help him by writing an algorithmic solution.

def are_anagrams(s1, s2):
    # Check if lengths of both strings are equal
    if len(s1) != len(s2):
        return False
    # Sort both strings and compare them
    return sorted(s1) == sorted(s2)

# Input strings
s1 = input()
s2 = input()

# Output whether the strings are anagrams
if are_anagrams(s1, s2):
    print("true")
else:
    print("false")
