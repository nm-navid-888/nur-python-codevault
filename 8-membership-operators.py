# Example 1: With a List

colors = ["red", "green", "blue"]

print("green" in colors)      # True
print("yellow" in colors)     # False
print("black" not in colors)  # True
print("blue" not in colors)   # False

# Example 2: With a Tuple

items = (10, 20, 30)

print(20 in items)         # True
print(40 in items)         # False
print(10 not in items)     # False

# Example 3: With a String

sentence = "Python is fun"

print("fun" in sentence)       # True
print("java" in sentence)      # False
print("Python" not in sentence)  # False

# Example 4: With a Dictionary (Only checks keys)

person = {"name": "Nur", "age": 25}

print("name" in person)        # True
print("Nur" in person)         # False (value, not key)
print("gender" not in person)  # True

# Guess the output

fruits = ["apple", "banana", "cherry"]
print("Apple" in fruits)
print("banana" not in fruits)