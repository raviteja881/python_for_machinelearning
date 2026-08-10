# Conditional Logic

age = 20

if age >= 18:
    print("Adult")


# if else

age = 16

if age >= 18:
    print("Adult")
else:
    print("Not Adult")


# if elif else

marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


# comparison operators

a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# logical operators

age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")


age = 20
is_student = False

if age >= 18 or is_student:
    print("Eligible")


age = 15

if not age >= 18:
    print("Minor")


# nested if

marks = 85

if marks >= 50:
    if marks >= 75:
        print("Good marks")
    else:
        print("Passed")
else:
    print("Failed")


# checking even or odd

number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# positive, negative or zero

number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# largest of two numbers

a = 20
b = 15

if a > b:
    print("a is greater")
else:
    print("b is greater")


# simple marks decision

marks = 82

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")


# practice

number = 25

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")