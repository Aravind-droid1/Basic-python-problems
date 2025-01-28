#to remove the special characters from a string using specify
def to_remove():
    string = input()
    non_special_character = ""
    for i in string:
        #we are using ascii values of characters and numbers to specify the non special characters
        if ((65 <= ord(i) <= 90) or (97 <= ord(i) <= 122) or (48 <= ord(i) <= 57) or (i == " ")):
            non_special_character += i
    print(non_special_character)

to_remove()
