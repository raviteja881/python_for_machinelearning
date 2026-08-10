# Dictionaries and Sets


# dictionary
student = {
    "name": "Ravi",
    "age": 20,
    "branch": "CSE"
}
print(student)


# accessing values
print(student["name"])
print(student["age"])


# get()
print(student.get("branch"))
print(student.get("marks"))


# adding a new item
student["marks"] = 85
print(student)


# changing a value
student["age"] = 21
print(student)


# removing an item
student.pop("marks")
print(student)


# dictionary length
print(len(student))


# checking keys
print("name" in student)
print("marks" not in student)


# keys and values
print(student.keys())
print(student.values())
print(student.items())


# looping through dictionary
for key in student:
    print(key)
for value in student.values():
    print(value)


# key and value together
for key, value in student.items():
    print(key, value)


# nested dictionary
students = {
    "student1": {
        "name": "Ravi",
        "age": 20
    },
    "student2": {
        "name": "Teja",
        "age": 21
    }
}
print(students["student1"]["name"])


# set
numbers = {10, 20, 30, 40}
print(numbers)


# duplicate values are removed
numbers = {10, 20, 20, 30, 30}
print(numbers)


# adding values
numbers.add(40)
print(numbers)


# adding multiple values
numbers.update([50, 60])
print(numbers)


# removing values
numbers.remove(20)
print(numbers)


# discard()
numbers.discard(100)
print(numbers)


# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)    # union
print(a & b)    # intersection
print(a - b)    # difference
print(a ^ b)    # symmetric difference


# checking values
print(3 in a)
print(10 not in a)


# set length
print(len(a))


# practice
student = {
    "name": "Ravi",
    "marks": 85,
    "branch": "CSE"
}
print(student["name"])
print(student["marks"])
student["marks"] = 90
print(student)


# set practice
subjects = {"Python", "C++", "Java", "Python"}
print(subjects)
print(len(subjects))