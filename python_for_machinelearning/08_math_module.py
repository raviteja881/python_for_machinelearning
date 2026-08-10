# Math Module

import math


# constants

print(math.pi)
print(math.e)


# square root

print(math.sqrt(25))
print(math.sqrt(49))


# power

print(math.pow(2, 3))
print(math.pow(5, 2))


# floor and ceil

print(math.floor(5.8))
print(math.ceil(5.2))


# absolute value

print(math.fabs(-10))
print(math.fabs(10))


# factorial

print(math.factorial(5))
print(math.factorial(6))


# gcd and lcm

print(math.gcd(12, 18))
print(math.lcm(4, 6))


# exponential

print(math.exp(2))


# logarithm

print(math.log(10))
print(math.log10(100))


# trigonometric functions

print(math.sin(0))
print(math.cos(0))
print(math.tan(0))


# degrees and radians

angle = 90

radian = math.radians(angle)

print(radian)
print(math.sin(radian))

print(math.degrees(math.pi))


# distance between two values

print(math.dist((0, 0), (3, 4)))


# hypotenuse

print(math.hypot(3, 4))


# checking numbers

print(math.isfinite(10))
print(math.isinf(10))
print(math.isnan(10))


# simple calculation

radius = 5

area = math.pi * radius ** 2

print("Area:", area)


# practice

number = 64

print("Square root:", math.sqrt(number))

number = 5

print("Factorial:", math.factorial(number))

angle = 30

print("Sin:", math.sin(math.radians(angle)))
print("Cos:", math.cos(math.radians(angle)))
print("Tan:", math.tan(math.radians(angle)))