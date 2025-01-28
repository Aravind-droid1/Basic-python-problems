#to print every possibilities of substrings of a main string 
def substrings_of_a_string():
    string=input()
    #here i is taken as initial to start from
    for i in range(len(string)):
        #then j is taken as the limit of the substring to be printed
        for j in range(i+1,len(string)+1):
            print(string[i:j])
            
substrings_of_a_string()