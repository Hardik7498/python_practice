#Create a function in Python
# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)

#Create a function with variable length of arguments
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

#Return multiple values from a function
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
res = calculation(40, 10)
print(res)

#Create a function with a default argument
# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")

#Create an inner function to calculate the addition in the following way
def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)

#Create a recursive function
def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)

#Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)

#Generate a Python list of all the even numbers between 4 to 30
print(list(range(4, 30, 2)))

#Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
print(max(x))