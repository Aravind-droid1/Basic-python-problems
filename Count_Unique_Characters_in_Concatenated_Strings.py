#Question: Count Unique Characters in Concatenated Strings
#Problem Statement: Kajal wants to write a program to find the count of unique characters by joining two strings.
#Your task is to help Kajal by writing the program.

def count_unique_characters(s1, s2):
    # Concatenate both strings
    concatenated_string = s1 + s2
    # Convert the concatenated string to a set to get unique characters
    unique_characters = set(concatenated_string)
    # Return the count of unique characters
    return len(unique_characters)

# Input strings
s1 = input()
s2 = input()

# Output the count of unique characters
print(count_unique_characters(s1, s2))
