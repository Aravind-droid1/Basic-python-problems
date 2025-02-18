#class and objects
class laptop:
    price=0
    processor=""
    ram=""
    def greet(self): 
        print("welcome!,have a look at the new model")
#creating objects from a class
hp=laptop()
lenovo=laptop()
#setting values for the variables for that objects individually
hp.price=20000
hp.processor="i7"
hp.ram="8GB"

lenovo.price=30000
lenovo.processor="i8"
lenovo.ram="16Gb"
#now calling
hp.greet()
print("price:",hp.price,"processor:",hp.processor,"ram:",hp.ram)
lenovo.greet()
print("price:",lenovo.price,"processor:",lenovo.processor,"ram:",lenovo.ram)
