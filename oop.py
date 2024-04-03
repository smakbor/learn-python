
#sharda didi class oop
class Student:
    # class attributes 
    university="Rajshahi University"
    def __init__(self,firstName,lastName,age):
        # object attributes
        self.name = firstName +" "+ lastName
        self.lastName = lastName
        self.age = age
    def printName(self,name):
        self.fName = name
        print("Hello",name)
        print(self.university)

    def eating(self):
        print(self.fName,"is eating!")

s1= Student("SM","Akbor",24)
# print(s1.university)
# s1.printName("Shamim Reza")
# print(s1.eating())

## freecodecamp class oop
class Device:
    def calculate_total_price(self,x,y):
        # print(self.price * self.qty)
        print(x*y)

laptop = Device()
laptop.name = "Microsoft Surface"
laptop.price = 50000
laptop.qty = 5

laptop.calculate_total_price(laptop.price,laptop.qty)

variant_color = "Black" #this is equivalent to Str("Black")
variant_name = str("surface laptop 3")

print(variant_name.upper())


