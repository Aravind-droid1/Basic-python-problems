def compare(a,b):
    #use string format method to make the int to taken as string till 3 floating points
    rounded_number1 = "{:.3f}".format(a)
    rounded_number2 = "{:.3f}".format(b)
    #the it checks for same strings 
    if rounded_number1 == rounded_number2:
        return True
    else:
        return False
    
print(compare(1.221,1.222))