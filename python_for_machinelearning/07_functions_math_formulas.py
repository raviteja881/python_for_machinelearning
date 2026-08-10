# Functions and Math Formulas


# simple function

def greet():
    print("Hello")


greet()
greet()


# function with parameter

def greet(name):
    print("Hello", name)


greet("Ravi")
greet("Teja")


# two parameters

def add(a, b):
    print(a + b)


add(10, 20)
add(5, 3)


# return value

def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# return can be used directly

print(add(5, 10))


# multiple values

def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference


result = calculate(10, 5)

print(result)


# default parameter

def greet(name="Ravi"):
    print("Hello", name)


greet()
greet("Teja")


# keyword arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student(age=20, name="Ravi")


# local variable

def test():
    number = 10
    print(number)


test()


# global variable

number = 20

def test():
    print(number)


test()


# function for square

def square(number):
    return number * number


print(square(5))
print(square(10))


# function for average

def average(a, b, c):
    return (a + b + c) / 3


print(average(80, 70, 90))


# function for factorial

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


print(factorial(5))


# function for checking even or odd

def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_number(10))
print(check_number(7))


# function for area of rectangle

def rectangle_area(length, breadth):
    return length * breadth


print(rectangle_area(10, 5))


# function for area of circle

def circle_area(radius):
    return 3.14 * radius * radius


print(circle_area(5))


# function with *args

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))


# function with **kwargs

def student_details(**details):
    print(details)


student_details(name="Ravi", age=20, branch="CSE")


# practice

def percentage(total, marks):
    return (marks / total) * 100


print(percentage(500, 425))