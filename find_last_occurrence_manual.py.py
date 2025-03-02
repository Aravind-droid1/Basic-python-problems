#Given two strings A and B, you need to find the last occurrence ( 1 based indexing) of string B in string A.

def findLastOccurrence(A: str, B: str) -> int:
    last_index = -1  # Initialize last occurrence index as -1
    len_A = len(A)
    len_B = len(B)

    # Traverse through string A
    for i in range(len_A - len_B + 1):  # Ensure B can fit within A
        # Check if substring A[i:i+len_B] matches B
        if A[i:i+len_B] == B:
            last_index = i  # Update last occurrence

    # Convert to 1-based index if found
    return last_index + 1 if last_index != -1 else -1

print(findLastOccurrence("abcdefghijklghifghsd", "ghi"))  
print(findLastOccurrence("abdbccaeab", "abc"))           



