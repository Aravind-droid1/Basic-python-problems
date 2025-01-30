#defanging the ip address where show cases the dot
def defangIPaddr():
    address=input("enter the ip address in only using numbers and dot: ")#123.345.567.789
    res = ""
    for i in address:
        if (i == "."):
            res = res + "[.]"
        else:
            res = res + i
    return res

defangIPaddr()