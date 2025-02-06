def countOdds():
    low=int(input("enter low number:"))
    high=int(input("enter high number:"))
    arr = []
    for i in range(low,high+1):
        if (i%2 != 0):
            arr.append(i)
    print(len(arr))

countOdds()