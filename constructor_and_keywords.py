#constructor
class laptop:
    #initializes first as soon as called
    def __init__(self):
        print("welcome!,have a look")
        #here we are creating a variable with an object of its own
        self.name=""
        self.processor=""
    def display(self):
        print("name:",self.name)
        print("processor:",self.processor)
#first gets to creates objects from a class
dell=laptop()

dell.name="dell"
dell.processor="i7"

dell.display()
#second gets to creates objects from a class
asus=laptop()

asus.name="asus"
asus.processor="i8"

asus.display()

#or

print("or it could print continuosly print")

dell.display()
asus.display()