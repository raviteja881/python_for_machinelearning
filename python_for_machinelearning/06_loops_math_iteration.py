# Loops and Math Iteration


# for loop

for i in range(5):
    print(i)


# range with starting value

for i in range(1, 6):
    print(i)


# range with step

for i in range(2, 11, 2):
    print(i)


# printing numbers

for i in range(1, 6):
    print("Number:", i)


# sum of numbers

total = 0

for i in range(1, 6):
    total = total + i

print("Total:", total)


# multiplication table

number = 5

for i in range(1, 11):
    print(number, "*", i, "=", number * i)


# loop through a list

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# even numbers

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# odd numbers

for i in range(1, 11):
    if i % 2 != 0:
        print(i)


# while loop

i = 1

while i <= 5:
    print(i)
    i = i + 1


# while loop with calculation

i = 1
total = 0

while i <= 5:
    total = total + i
    i = i + 1

print("Total:", total)


# break

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# continue

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# nested loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# nested loop pattern

for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()


# loop else

for i in range(5):
    print(i)
else:
    print("Loop completed")


# break with else

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")


# factorial

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)


# practice

number = 10

for i in range(1, 11):
    print(number * i)