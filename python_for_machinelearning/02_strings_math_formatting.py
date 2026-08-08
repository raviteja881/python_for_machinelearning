# Strings and Math Formatting
name = "Ravi"
college = 'BVRIT'
print(name)
print(college)


# multiline string
message = """Hello
I am learning Python
Python is easy"""
print(message)


# length
text = "Python"
print(len(text))


# indexing
text = "Python"
print(text[0])
print(text[1])
print(text[-1])


# slicing
print(text[0:3])
print(text[2:6])
print(text[:4])
print(text[2:])
print(text[::2])


# concatenation
first_name = "Ravi"
last_name = "Teja"
full_name = first_name + " " + last_name
print(full_name)


# repetition
print("Python " * 3)


# checking string
text = "Python programming"
print("Python" in text)
print("Java" not in text)


# string methods
name = "ravi teja"
print(name.upper())
print(name.lower())
print(name.title())


text = "  Python  "
print(text.strip())


text = "I like Java"
print(text.replace("Java", "Python"))


# split
text = "Python is easy"
words = text.split()
print(words)


# join
words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)


# find
text = "I am learning Python"
print(text.find("Python"))


# count
text = "banana"
print(text.count("a"))


# startswith and endswith
text = "Python.py"
print(text.startswith("Python"))
print(text.endswith(".py"))


# escape characters
print("Hello\nPython")
print("Name:\tRavi")
print("He said \"Hello\"")


# f-string
name = "Ravi"
age = 20
print(f"My name is {name}")
print(f"I am {age} years old")


# calculations in f-string
a = 10
b = 3
print(f"Sum = {a + b}")
print(f"Division = {a / b:.2f}")


# number formatting
price = 99.5678
print(f"{price:.2f}")


# practice
name = "Ravi"
course = "Python"
days = 30
print(f"My name is {name}")
print(f"I am learning {course}")
print(f"I will learn it for {days} days")