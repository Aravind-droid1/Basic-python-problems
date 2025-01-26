def number():
    i=0
    while i<10 :
        f = int(input())
        s = int(input())
        if (f > s):
            print("f is bigger")
        elif (s > f):
            print("s is bigger")
        else:
            break
        i+=1

number()

