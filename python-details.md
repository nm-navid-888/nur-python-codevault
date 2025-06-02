# Python Basic

## 1. First Python Code

###
**Code:**
```python
print("Welcome to the Python World")
```

**Output:**
```python
Welcome to the Python World
```


## 2. Python RUNS Line by Line (Top to bottom)

###
**Code:**
```python
print("Welcome to the Python World")

print(3+2)

print('20', 24)
```

**Output:**
```python
Welcome to the Python World
5
20 24
```

## 3. Python Data Type

###
**Code:**
```python
print(type ("Welcome to python"))
print(type(10))

# 1. Basic Data Types

print("### Check Basic Data Types")
print("Hello => type is ", type("Hello"))           # str
print("100 => type is ", type(100))               # int
print("99.99 => type is ", type(99.99))             # float
print("True => type is ", type(True))              # bool
print("None => type is ", type(None))              # NoneType

# 2. List, Tuple, Set, Dictionary

print("###List, Tuple, Set, Dictionary")
print(type([1, 2, 3]))         # list
print(type((1, 2, 3)))         # tuple
print(type({1, 2, 3}))         # set
print(type({"a": 1, "b": 2}))  # dict
# dictionary stores data in key-value pairs. Each key must be unique.

# 3. Check all types in one go

print("### Check all types in one go")
values = ["Hi", 10, 3.14, False, None, [1,2], (3,4), {5,6}, {"a":1}]
for val in values:
    print(f"{val} is of type {type(val)}")

# f"{val} is of type {type(val)}" is an f-string, which allows inserting values directly into the string.
# type(val) returns the data type (e.g., <class 'int'>, <class 'str'>).
# The result is printed in a readable format.

# 4. Check instance type using isinstance()

a = "Python"
print("### Check instance type using isinstance()")
print(isinstance(a, str))     # True
print(isinstance(a, int))     # False
```

**Output:**
```python
<class 'str'>
<class 'int'>
Check Basic Data Types
Hello => type is  <class 'str'>
100 => type is  <class 'int'>
99.99 => type is  <class 'float'>
True => type is  <class 'bool'>
None => type is  <class 'NoneType'>
###List, Tuple, Set, Dictionary
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
### Check all types in one go
Hi is of type <class 'str'>
10 is of type <class 'int'>
3.14 is of type <class 'float'>
False is of type <class 'bool'>
None is of type <class 'NoneType'>
[1, 2] is of type <class 'list'>
(3, 4) is of type <class 'tuple'>
{5, 6} is of type <class 'set'>
{'a': 1} is of type <class 'dict'>
### Check instance type using isinstance()
True
False
```

### 🧠 More Characteristics

| **Feature**        | **List**         | **Tuple**        | **Set**           | **Dictionary**             |
|--------------------|------------------|------------------|-------------------|----------------------------|
| **Mutable**        | ✅ Yes           | ❌ No            | ✅ Yes            | ✅ Yes                     |
| **Indexed**        | ✅ Yes           | ✅ Yes           | ❌ No             | ❌ Keys used instead       |
| **Allows duplicates** | ✅ Yes       | ✅ Yes           | ❌ No             | ❌ No (keys only)          |
| **Syntax**         | `[ ]`            | `( )`            | `{ }` (for values)| `{key: value}`             |

## 4. Type Casting (Conversion)

###
**Code:**
```python
print(int("5"))               # str to int
print(float(10))              # int to float
print(str(3.14))              # float to str
print(bool(""))               # False (empty string is false)
print(bool("Python"))         # True (non-empty string is true)
```

**Output:**
```python
5
10.0
3.14
False
True
```

## 5. Variable
### 🧠 Concept: What is a Variable?

A **variable**:

- Holds/stores a value.
- Can be reused or updated later.
- Has a **name**, a **value**, and uses the `=` **assignment operator**.
---

**Example:**

```python
name = 'Nur Mohammad'   # string value
age = 30               # integer value
```

### 5.1 Assign and Print Variables
**Code:**
```python
# 1. Assign and Print Variables

city = "Dhaka"
temperature = 35

print(city)
print(temperature)
```

**Output:**
```python
Dhaka
35
```

### 5.2 Change the Value of a Variable
**Code:**
```python
# 2. Change the Value of a Variable

language = "Python"
print(language)

language = "JavaScript"
print(language)
```

**Output:**
```python
Python
JavaScript
```

### 5.3 Multiple Variables in One Line
**Code:**
```python
x, y, z = 5, 10, 15
print(x)
print(y)
print(z)
```

**Output:**
```python
5
10
15
```


### 5.4 Assign Same Value to Multiple Variables
**Code:**
```python
a = b = c = "Nur"
print(a, b, c)
```

**Output:**
```python
Nur Nur Nur
```

### 5.5 Combine Variables in Print
**Code:**
```python
first_name = "Nur"
last_name = "Mohammad"
full_name = first_name + " " + last_name

print(full_name)
```

**Output:**
```python
Nur Mohammad
```

### 5.6 Variable Types
**Code:**
```python
x = 100
y = 99.5
z = True
name = "Nur"

print(type(x))
print(type(y))
print(type(z))
print(type(name))
```

**Output:**
```python
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
```


### 5.7 Arithmetic with Variables
**Code:**
```python
price = 100
quantity = 3
total = price * quantity

print("Total price is:", total)
```

**Output:**
```python
Total price is: 300
```

### 5.8 Practice Challenge
**Code:**
```python
# Define your details
my_name = "Nur"
my_age = 25
my_country = "Bangladesh"

# Print a message using those variables
print(f"My name is {my_name}, I am {my_age} years old, and I live in {my_country}.")
```

**Output:**
```python
My name is Nur, I am 25 years old, and I live in Bangladesh.
```

## ✅ Important Features in Python

- [ ] High-level programming language (Like plain English)
- [ ] Dynamically typed language (No need to define data type)
- [ ] Huge popular in task automation (Scripting language)
- [ ] Python is both interpreted and compiled
- [ ] Case sensitive language (Nure and nure are different)

### ✅ Important Features in Python (Explained)

| **Feature**                          | **Description** |
|-------------------------------------|-----------------|
| 🔷 **High-level Programming Language** | Python is designed to be easy to read and write. Its syntax looks like plain English, making it beginner-friendly and suitable for rapid development. |
| 🔷 **Dynamically Typed Language**     | You don't need to declare data types explicitly. Python automatically detects the type of variable during execution. <br>📌 Example: `x = 10` (no need to write `int x = 10`) |
| 🔷 **Popular in Task Automation**     | Python excels in scripting and automation tasks such as file handling, web scraping, data processing, etc. Tools like `os`, `shutil`, `selenium`, and `pandas` help automate workflows. |
| 🔷 **Interpreted and Partially Compiled** | Python is an interpreted language—code is executed line by line. Internally, Python source code is first compiled to bytecode (`.pyc`) and then interpreted by the Python Virtual Machine (PVM). |
| 🔷 **Case Sensitive Language**        | Python treats uppercase and lowercase letters as different.<br>📌 `Name` and `name` are two different variables. |

## 6. Operators in Python

## 📘 Arithmetic Operator Operation

| **Operator** | **Description**         | **Example** | **Result** |
|--------------|-------------------------|-------------|------------|
| `+`          | Addition                | `5 + 2`     | `7`        |
| `-`          | Subtraction             | `5 - 2`     | `3`        |
| `*`          | Multiplication          | `5 * 2`     | `10`       |
| `/`          | Division (float)        | `5 / 2`     | `2.5`      |
| `//`         | Floor Division          | `5 // 2`    | `2`        |
| `%`          | Modulus (remainder)     | `5 % 2`     | `1`        |
| `**`         | Exponentiation          | `5 ** 2`    | `25`       |
"""

### 6.1 Example 1: Try different values
**Code:**
```python
a = 20
b = 6

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Float division
print(a // b)   # Floor division
print(a % b)    # Remainder
print(a ** b)   # Power (20^6)
```

**Output:**
```python
26
14
120
3.3333333333333335
3
2
64000000
```

### 6.2 Example 2: Negative and zero

**Code:**
```python
x = -10
y = 3

print("### Check arithmetic operation with Negative and zero")
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** 2)
```

**Output:**
```python
-7
-13
-30
-3.3333333333333335
-4
2
100
```


### 6.3 Example 3: Practice Challenge – User Input

**Code:**
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Float Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** num2)

```

**Output:**
```python
Enter first number: 100
Enter second number: 3
Sum: 103
Difference: 97
Product: 300
Float Division: 33.333333333333336
Floor Division: 33
Modulus: 1
Power: 1000000
```

## 📘 Comparison Operators Operation

| **Operator** | **Meaning**                | **Example** | **Result**   |
|--------------|----------------------------|-------------|--------------|
| `==`         | Equal to                   | `a == b`    | True/False   |
| `!=`         | Not equal to               | `a != b`    | True/False   |
| `>`          | Greater than               | `a > b`     | True/False   |
| `<`          | Less than                  | `a < b`     | True/False   |
| `>=`         | Greater than or equal to   | `a >= b`    | True/False   |
| `<=`         | Less than or equal to      | `a <= b`    | True/False   |
"""


### 6.4 Example 1: Using integers

**Code:**
```python
# Example 1: Using integers

x = 8
y = 10

print(x == y)    # False
print(x != y)    # True
print(x > y)     # False
print(x < y)     # True
print(x >= 8)    # True
print(y <= 9)    # False
```

**Output:**
```python
False
True
False
True
True
False
```

### 6.5 Example 2: Using strings

**Code:**
```python
name1 = "Nur"
name2 = "nur"

print(name1 == name2)    # False (case-sensitive)
print(name1 != name2)    # True
print(name1 < name2)     # True ('N' comes before 'n' in ASCII)
```

**Output:**
```python
False
True
True
```


### 6.6 Example 3: Mixing types

**Code:**
```python
a = 5
b = "5"

print(a == int(b))  # True
print(str(a) == b)  # True
print(a != b)       # True (without type conversion)

```

**Output:**
```python
True
True
True
```



### 6.7 Practice Challenge

**Code:**
```python
score = 85
passing_mark = 60

print(score >= passing_mark)     # Expected: True
print(score == 100)              # Expected: False
print(passing_mark < 40)         # Expected: False
```

**Output:**
```python
True
False
False
```
## ✅ Python Membership Operators


| **Operator** | **Meaning**                                                     |
|--------------|------------------------------------------------------------------|
| `in`         | Returns `True` if the item exists in a sequence                 |
| `not in`     | Returns `True` if the item does **not** exist in a sequence     |
"""

### 6.8 Example 1: Membership operation With a List

**Code:**
```python
colors = ["red", "green", "blue"]

print("green" in colors)      # True
print("yellow" in colors)     # False
print("black" not in colors)  # True
print("blue" not in colors)   # False

```

**Output:**
```python
True 
False
True 
False
```

### 6.9 Example 2: With a Tuple

**Code:**
```python
items = (10, 20, 30)

print(20 in items)         # True
print(40 in items)         # False
print(10 not in items)     # False
```

**Output:**
```python
True
False
False
```

### 6.10 Example 3: With a String

**Code:**
```python
sentence = "Python is fun"

print("fun" in sentence)       # True
print("java" in sentence)      # False
print("Python" not in sentence)  # False
```

**Output:**
```python
True
False
False
```



### 6.11 Example 4: With a Dictionary (Only checks keys)

**Code:**
```python
person = {"name": "Nur", "age": 25}

print("name" in person)        # True
print("Nur" in person)         # False (value, not key)
print("gender" not in person)  # True
```

**Output:**
```python
True
False
True
```

### 6.12 Challenge

**Code:**
```python
fruits = ["apple", "banana", "cherry"]
print("Apple" in fruits)
print("banana" not in fruits)
```

**Output:**
```python
False
False
```
