# Composite types


### Lists
my_list = ["a","b","c","d"]

# print(my_list)
# access value by index
# print(my_list[1])
# print(my_list[4]) THIS WILL ERROR OUT
# insert to the end
my_list.append('m')
# GET THE LAST ELEMENT OF LIST
# print(my_list[-1])

# print(len(my_list))
# Insert to a specific location or index
my_list.insert(1,"aa")
# print(my_list)

# print(my_list.pop())
# print(my_list.pop(2))
# print(my_list.remove("aa"))
# print(my_list)

print(my_list[1:5:3])
print(my_list)

my_list[0] = "test"
print(my_list)

### Dictionary
# Key value pair
# (key:value)
person = {
    "user_name":"mahmoud",
    "email":"m@m.com",
    "age":9999,
    "is_instructor":True,
    "stacks":["MERN","Python"]
}

person["user_name"] = "Test"
print(person["user_name"])
print(person.get("user_name"))

person.update({"age":"-1"})
person.update({"new_key":"-1"})
print(person)
print(person["age"])
person.pop("new_key")
print(person)


### loops
print("Hello")
print("Hello")
print("Hello")
print("Hello")

for i in range(0,4):
    print("Hello")

# looping through lists

for char in my_list:
    print(char)

for i in range(0,len(my_list)):
    print(i,my_list[i])
# default start at 0
for i in range(len(my_list)):
    print(i,my_list[i])
# default step = 1
for i in range(0,len(my_list),2):
    print(i,my_list[i])

# looping through dictionaries

for key in person:
    print(key,person[key])

for key,value in person.items():
    print(key,value)

# While loop only with lists
i = len(my_list)
while i > 0 :
    # i-- THIS WILL NOT WORK
    i-=1 # you need this
    print(i,my_list[i])


### Tuples

my_tuple = ('a','b','c')
print(my_tuple[0])
for value in my_tuple:
    print(value)
# THIS WILL NOT WORK
# my_tuple[0] = "m"
# THIS WILL NOT WORK
# my_tuple.append("s")