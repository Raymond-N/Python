def my_func():
    print("Hello World!!")

my_func()

def func_with_params(name):
    print("Hello",name)

def func_with_params2(name,age):
    print("Hello",name,age)

func_with_params2(name="test",age=2)
func_with_params2(age=2, name="mahmoud")
func_with_params2(2, "mahmoud")

def func_with_default_params(name="John"):
    print("Hello",name)

func_with_params("test")
func_with_default_params()

def func_with_args(*args):
    print("WHAT ARE ARGS?",args)

def func_with_kwargs(**kwargs):
    print("WHAT ARE kwargs?",kwargs)

func_with_args(1,2,3,4,5,6,7,8)
func_with_kwargs(age=10,is_active=True)

def func_with_return(a,b):
    x = a + b
    print("THIS IS X",x)
    return x
    print("YOU CAN'T DO ANYTHING AFTER RETURN",x)

# print("THIS IS OUT!!!!",x)
result = func_with_return(3,4)
print(result)
print(func_with_return(2,2))

z = result + 3
print(z)

def can_drive(age):
    if age > 80:
        print("stay at home",age)
    elif age >= 18:
        print("good to go",age)
    else:
        print("too young to drive",age)

can_drive(88)
can_drive(50)
can_drive(22)
can_drive(18)
can_drive(16)

#HW: create a function that take list of dicts and output a list with all the first names of the users who can drive
# Hint can_drive([{"first_name":"","last_name","age":0},{},{}])