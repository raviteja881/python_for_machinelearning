# Lists, Tuples and Sequences

# list
numbers = [10, 20, 30, 40]
print(numbers)


# different data types
student = ["Ravi", 20, 85.5, True]
print(student)


# indexing
numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[2])
print(numbers[-1])


# slicing
print(numbers[0:2])
print(numbers[1:])
print(numbers[:3])
print(numbers[::2])


# changing list values
numbers[0] = 100
print(numbers)


# adding values
numbers.append(50)
print(numbers)
numbers.insert(1, 15)
print(numbers)


# removing values
numbers.remove(30)
print(numbers)
numbers.pop()
print(numbers)


# list length
print(len(numbers))


# checking value
print(20 in numbers)
print(500 not in numbers)


# sorting
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)


# copying a list
numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(new_numbers)


# joining lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


# list repetition
numbers = [1, 2]
print(numbers * 3)


# nested list
students = [
    ["Ravi", 20],
    ["Teja", 21]
]
print(students)
print(students[0])
print(students[0][0])


# tuple
numbers = (10, 20, 30, 40)
print(numbers)


# tuple indexin
print(numbers[0])
print(numbers[-1])


# tuple slicing
print(numbers[1:3])


# tuple length
print(len(numbers))


# tuple methods
numbers = (10, 20, 10, 30)
print(numbers.count(10))
print(numbers.index(30))


# checking tuple
print(20 in numbers)


# tuple packing
student = "Ravi", 20, 85.5
print(student)


# tuple unpacking
name, age, marks = student
print(name)
print(age)
print(marks)


# list unpacking
numbers = [10, 20, 30]
a, b, c = numbers
print(a)
print(b)
print(c)


# sequence
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(len(numbers))
print(30 in numbers)


# practice
marks = [80, 75, 90, 85, 70]
print("Marks:", marks)
print("First mark:", marks[0])
print("Total marks:", sum(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))


# tuple practice
student = ("Ravi", 20, "CSE")
print("Name:", student[0])
print("Age:", student[1])
print("Branch:", student[2])