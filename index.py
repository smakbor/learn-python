print("hello world")

thislist = ["apple", "banana", "cherry"]
# print(thislist)
# print(thislist[2])
# print(len(thislist))
# for x in thislist:
    # print(x)


def printName(name):
    # print("My name is"+" " +name)


# printName("Akbor")

# def sum(a,b):
#     sum =a+b
    # print(sum)

# sum(2,3)

# mylist =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(mylist)
""""
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
Note: The search will start at index 1 (included) and end at index 2 (not included).
"""
# newList = mylist[1:2]
# print(newList)

"""
mylist =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
By leaving out the start value, the range will start at the first item:
"""
# print(mylist[:3])
# print(mylist)
# mylist[1]="hello"
# print(mylist)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
# print(car.values())
# print(car["model"])
# print(car.items())

class Student:
    name="SM Akbor"
    age=24
    def __init__(self,firstName,lastName):
        self.fullName = firstName +" "+ lastName
    # def printName():
    #     print(name)

s1= Student("SM","Akbor")
print(s1)
