#Question:Remove Spaces and Concatenate Strings
#Problem Statement: Kajal wants to write a program to concatenate the words of a given statement.
#more formally, she wants to remove the spaces from the string and give the resultant string.

def remove_spaces(s):
    # Initialize an empty result string
    result = ""
    # Loop through each character in the string
    for char in s:
        # If the character is not a space, append it to the result string
        if char != " ":
            result += char
    # Return the concatenated result without spaces
    return result

# Input string
s = input()

# Output the string with spaces removed
print(remove_spaces(s))
