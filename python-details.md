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

### 📘 Arithmetic Operator Operation

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

### 📘 Comparison Operators Operation

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
### ✅ Python Membership Operators


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
## 7. Conditions / Logics in Python

### 7.1 Example 1: Age Category Checker

**Code:**
```python
age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

```

**Output:** Sample
```python
Enter the age =10
You are a minor.

Enter the age =18
You are an adult.

Enter the age =20
You are an adult.
```
### 7.2 Example 2: Grading System

**Code:**
```python
marks = int(input("Enter the mark ="))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade F")
```

**Output:**
```python
Enter the mark =94
Grade A
```
### 7.3 Example 3: Number Checker (Positive, Negative, Zero)

**Code:**
```python
num = int(input("Enter the number = "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
```

**Output:**
```python
Enter the number = -12
Negative Number
```


### 7.4 Example 4: Even or Odd Checker

**Code:**
```python
number = int(input("Enter the number = "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output:**
```python
Enter the number = 33
Odd
```
### 7.5 Example 5: Login Simulation

**Code:**
```python
username = input("Enter the username = ")
password = input("Enter the password = ")

if username == "admin" and password == "1234":
    print("Login Successful")
elif username != "admin" and password == "1234":
    print("Invalid Username")
elif username == "admin" and password != "1234":
    print("Invalid Credentials")
else:
    print("Invalid Username and Password")
```

**Output:** Sample
```python
Enter the username = nur
Enter the password = 1234
Invalid Username

Enter the username = admin
Enter the password = 1234
Login Successful
```

### 7.6 Example 6: Password Strength Checker

**Code:**
```python
password = input("Enter the password = ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
```

**Output:**
```python
Enter the password = navid
Weak Password
```

### 7.7 Python Calculator with Conditions

Write a calculator program that takes three inputs from the user:

Input1: A number (float or integer).
Input2: A number (float or integer).
Operator: A character representing a mathematical operation.
Valid operators: +, -, *, /, %

Validate that Input1 and Input2 are numbers.

Validate that the operator is one of +, -, *, /, %.

Use conditional statements to perform:

+ → Sum

- → Difference

* → Product

* / → Quotient (Handle divide by zero)

* % → Remainder (Handle divide by zero)

Display the result or an appropriate error.

**Code:**
```python
# Take inputs
try:
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /, %): ")

    # Perform calculation
    if operator == "+":
        result = input1 + input2
        print("The result is", result)
    elif operator == "-":
        result = input1 - input2
        print("The result is", result)
    elif operator == "*":
        result = input1 * input2
        print("The result is", result)
    elif operator == "/":
        if input2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = input1 / input2
            print("The result is", result)
    elif operator == "%":
        if input2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = input1 % input2
            print("The result is", result)
    else:
        print("Invalid operator. Please use one of +, -, *, /, %.")

except ValueError:
    print("Error: Please enter valid numbers.")

```

**Output:**
```python
Enter the first number: 5
Enter the second number: 6
Enter the operator (+, -, *, /, %): +
The result is 11.0
```


## 8. Understanding mutable vs. immutable data type

### 8.1 Mutable Data Types (List)


**Code:**
```python
# List (Mutable)
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']
```

**Output:**
```python
['apple', 'banana', 'cherry']
```

### 8.2 Mutable Data Types (Dictionary)


**Code:**
```python
# Dictionary (Mutable)
student = {"name": "Nur", "age": 22}
student["grade"] = "A"
print(student)  # {'name': 'Nur', 'age': 22, 'grade': 'A'}
```

**Output:**
```python
{'name': 'Nur', 'age': 22, 'grade': 'A'}
```

### 8.3 Mutable Data Types (Set)


**Code:**
```python
# Set (Mutable)

colors = {"red", "blue"}
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}
```

**Output:**
```python
{'blue', 'red', 'green'}
```

### 8.4 Immutable Data Types (Integer)


**Code:**
```python
# Integer (Immutable)

x = 5
print(id(x))  # memory address of x
x += 1
print(id(x))  # different address — new object created
```

**Output:**
```python
11754024
11754056
```

### 8.5 Immutable Data Types (String)


**Code:**
```python
# String (Immutable)

greeting = "Hello"
print(greeting.upper())   # returns new string
print(greeting)           # original string unchanged
```

**Output:**
```python
HELLO
Hello
```

### 8.6 Immutable Data Types (Tuple)


**Code:**
```python
# String (Immutable)

greeting = "Hello"
print(greeting.upper())   # returns new string
print(greeting)           # original string unchanged
```

**Output:**
```python
TypeError: 'tuple' object does not support item assignment
```


### 8.7 Immutable Data Types (Frozen Set)

**Code:**
```python
# Frozen Set (Immutable)

vowels = frozenset({"a", "e", "i","o","u"})
vowels.add("y") # Error: frozenset does not support add()
```

**Output:**
```python
AttributeError: 'frozenset' object has no attribute 'add'
```

## 🧾 Summary Table: Mutable vs Immutable Data Types

| **Data Type**   | **Mutable** | **Immutable** |
|------------------|-------------|----------------|
| List             | ✅ Yes      | ❌ No          |
| Dictionary       | ✅ Yes      | ❌ No          |
| Set              | ✅ Yes      | ❌ No          |
| Integer          | ❌ No       | ✅ Yes         |
| Float            | ❌ No       | ✅ Yes         |
| String           | ❌ No       | ✅ Yes         |
| Tuple            | ❌ No       | ✅ Yes         |
| Frozen Set       | ❌ No       | ✅ Yes         |

## 13. Data Structures

Python offers several built-in data structures to store and manage data effectively.  
A data structure is a way of organizing, storing, and managing data in a way that makes it efficient to access and modify.  
They help you write efficient programs that logically and systematically manipulate and analyze data.

---


### 🟨 When to Use Which Data Structure?

- **List**: Use when you need a sequence of elements where duplicates are allowed and order matters.
- **Tuple**: Choose when you need an ordered, immutable collection, like coordinates.
- **Dictionary**: Ideal for key-value pairs where fast lookups by key are necessary.
- **Set**: Best for collections where duplicates need to be removed automatically.
- **Deque**: Useful when you need to add or remove items from both ends quickly.
- **Counter**: Perfect for frequency counting or tallying elements.
- **Heap**: Ideal for priority-based tasks, like scheduling or finding minimum/maximum values.

### 13.1  Python Data Structures (list) 

- **List:** Use when you need a sequence of elements where duplicates are allowed and order matters.

**Code:**
```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.append("mango")     # .append() method adds an element to the end of the list.
fruits.remove("banana")    # .remove() method removes the first occurrence of "banana" from the list.
print(fruits)
# Count how many times "banana" appears
print(fruits.count("banana"))
```

**Output:**
```python
['apple', 'cherry', 'banana', 'mango']
1
```

### 13.2  Python Data Structures (tuple) 

- **Tuple:** Choose when you need an ordered, immutable collection, like
coordinates.

**Code:**
```python

coordinates = (10.0, 20.5)
print(coordinates[0])          # 10.0

# Convert to list, modify, then back to tuple
mod_tuple = list(coordinates)  
print(mod_tuple)               # mod_tuple = [10.0, 20.5]
mod_tuple.append(30.0)         # adds an element to the end of the list.
print(mod_tuple)               # mod_tuple =  [10.0, 20.5, 30.0]
coordinates = tuple(mod_tuple) # convert list to tuple
print(coordinates)             # (10.0, 20.5, 30.0)
```

**Output:**
```python
10.0
[10.0, 20.5]
[10.0, 20.5, 30.0]
(10.0, 20.5, 30.0)
```


### 13.3  Python Data Structures (dictionary) 

- **Dictionary:** Ideal for key-value pairs where fast lookups by key are necessary.

**Code:**
```python
person = {"name": "Alice", "age": 25}
person["city"] = "Dhaka"
print(person)                  # {'name': 'Alice', 'age': 25, 'city': 'Dhaka'}

# Remove a key
person.pop("age")
print(person)                  # {'name': 'Alice', 'city': 'Dhaka'}

# Convert to list
mod_person = list(person)
print(mod_person)              # ['name', 'city']

# Get list of values
values_list = list(person.values())
print(values_list)             # ['Alice', 'Dhaka']
```

**Output:**
```python
{'name': 'Alice', 'age': 25, 'city': 'Dhaka'}
{'name': 'Alice', 'city': 'Dhaka'}
['name', 'city']
['Alice', 'Dhaka']
```


### 13.4  Python Data Structures (set) 

- **Set:** Best for collections where duplicates need to be removed automatically.

A set is:

- **Unordered:** No guaranteed order of elements.
- **Unique:** Duplicate values are automatically removed.

**Code:**
```python
# 13.4  Python Data Structures (set)

nums = {1, 2, 2, 3}            # Created a set named nums
nums.add(4)
print(nums)                    # {1, 2, 3, 4}

# set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))              # {1, 2, 3, 4, 5}
print(a.intersection(b))       # {3}

# Convert Set to List or Tuple

fruits = {"apple", "banana", "mango"}

fruit_list = list(fruits)
print(fruit_list)  # ['apple', 'banana', 'mango']

fruit_tuple = tuple(fruits)
print(fruit_tuple)  # ('apple', 'banana', 'mango')

# Convert List to Set and set to list

items = ["pen", "pencil", "pen", "eraser"]
unique_items = set(items)
print(unique_items)             # {'pen', 'pencil', 'eraser'}
print(list(unique_items))       # Convert back to list

# Check Membership

cities = {"Dhaka", "Chittagong", "Sylhet"}
print("Dhaka" in cities)     # True
print("Rajshahi" in cities)  # False
```

**Output:**
```python
{1, 2, 3, 4}

{1, 2, 3, 4, 5}
{3}

['banana', 'mango', 'apple']
('banana', 'mango', 'apple')

{'pencil', 'pen', 'eraser'}
['pencil', 'pen', 'eraser']

True
False
```

### 13.5  Python Data Structures (Deque) 

- **Deque:** Useful when you need to add or remove items from both ends quickly.
- **Deque** deque stands for double-ended queue.
- **Property** It allows fast appends and pops from both ends (left and right).

**Code:**
```python
# 13.5  Python Data Structures (Deque)

from collections import deque

dq = deque([1, 2, 3])        # Creates a deque
dq.appendleft(0)             # Inserts 0 at the left end.
dq.append(4)                 # Appends 4 at the right end.
print(dq)                    # deque([0, 1, 2, 3, 4])
mod_dq = dq.pop()            # Removes the last element (right end), which is 4.
print(dq)                    # deque([0, 1, 2, 3])
print(mod_dq)                # 4

dq_ext = deque([1, 2])
dq_ext.extend([3, 4])        # Adds to the right end
dq_ext.extendleft([0, -1])   # Adds to the left in reverse order
print(dq_ext)                # deque([-1, 0, 1, 2, 3, 4])

```

**Output:**
```python
deque([0, 1, 2, 3, 4])
deque([0, 1, 2, 3])
4
deque([-1, 0, 1, 2, 3, 4])
```

### 📘 Summary of Common `deque` Methods

| **Method**         | **Action**                                       |
|--------------------|--------------------------------------------------|
| `append(x)`        | Add `x` to the **right** end                     |
| `appendleft(x)`    | Add `x` to the **left** end                      |
| `pop()`            | Remove and return element from **right** end     |
| `popleft()`        | Remove and return element from **left** end      |

---

### 13.6  Python Data Structures (counter) 

- **Counter:** Perfect for frequency counting or tallying elements.
- Imports the Counter class from the collections module.
- Counter is a special dictionary subclass for counting hashable objects.


**Code:**
```python
# 13.6  Python Data Structures (counter)

from collections import Counter

votes = ["A", "B", "A", "C", "B", "A"] # representing votes for different candidates.
# Counter(votes) counts each unique element and returns a dictionary-like object
tally = Counter(votes)                 
print(tally)                           # Counter({'A': 3, 'B': 2, 'C': 1})
print(tally["A"])                      # 3
print(tally["D"])                      # 0 (does not raise an error)
```

**Output:**
```python
Counter({'A': 3, 'B': 2, 'C': 1})
3
0
```


### 13.7  Python Data Structures (Heap) 

- **Heap:** Ideal for priority-based tasks, like scheduling or finding
minimum/maximum values.
- heapq provides functions to create and manage heaps (priority queues).
- In Python, it's always a min-heap (smallest item comes first).

**Code:**
```python
# 13.7  Python Data Structures (Heap)

import heapq

tasks = [3, 1, 4, 2]
heapq.heapify(tasks)         # Rearranges the list in-place to satisfy heap properties.
print(tasks)                 # [1, 2, 4, 3]
heapq.heappush(tasks, 0)     # Adds 0 to the heap and maintains the min-heap structure.
print(tasks)                 # [0, 1, 4, 3, 2]
print(heapq.heappop(tasks))  # 0 (lowest priority)
```

**Output:**
```python
[1, 2, 4, 3]
[0, 1, 4, 3, 2]
0
```

### 📘 Summary of `heapq` Operations

| **Function**               | **Description**                                            |
|----------------------------|------------------------------------------------------------|
| `heapify(list)`            | Turns a list into a heap in-place                          |
| `heappush(heap, x)`        | Push item `x` into the heap                                |
| `heappop(heap)`            | Pop and return the smallest item                           |
| `heappushpop(h, x)`        | Push then pop smallest (faster than both steps)            |
| `heapreplace(h, x)`        | Pop then push (always removes smallest)                    |


## 14. Python String Operations

### Problem 14.1: Print the total number of characters in the string (including spaces).


**Code:**
```python
text = "pyhton programming"
length = len(text)         
print("Text length including spaces = ", length)  
```

**Output:**
```python
Text length including spaces =  18
```


### Problem 14.2: Check String Length Limit 

**Code:**
```python
username = input("Enter the username: ") # input() takes user input as a string.

if len(username) > 10:     # len(username) checks how many characters the username has
    print("Too Long !")
else:
    print("Accepted")
```

**Output:**
```python
Enter the username: Nur Mohammad
Too Long !
```

### Problem 14.3: Compare Two String Lengths
Take two strings and compare their lengths. Print which string is longer or if they are equal in length. 

**Code:**
```python
name_1 = "usman abdullah"
name_2 = "arpita paul"

if len(name_1) > len(name_2):
    print("name_1 is longer")
elif len(name_1) < len(name_2):
    print("name_2 is longer")
else:
    print("both string are equal")
```

**Output:**
```python
name_1 is longer
```

### Problem 14.4: Count Letters Without Spaces 

**Code:**
```python
text = "Data Science with Python"

# Remove spaces and count remaining characters
count_without_space = len(text.replace(" ", ""))
print("Number of characters with space", len(text))
print("Number of characters without space:", count_without_space)
```

**Output:**
```python
Number of characters with space 24
Number of characters without space: 21
```

### Problem 14.5: Word Length List 

**Code:**
```python
sentence = "Python is powerful and fun"

# Split the sentence into words
words = sentence.split()
# Loop through each word and print its length
for word in words:
    print(f"{word} → {len(word)}")
```

**Output:**
```python
Python → 6
is → 2
powerful → 8
and → 3
fun → 3
```

### Problem 14.6: Reverse Length Checker 

**Code:**
```python
string = "python"
reverse_string = string[::-1]
if len(string) == len(reverse_string):
    print("True")
else:
    print("false")

# Alternative

def reverse_length_checker(text):
    reversed_text = text[::-1]
    return len(text) == len(reversed_text)

# Example usage
input_text = "Python"
print(reverse_length_checker(input_text))  # Output: True
```

**Output:**
```python
True
True
```

### Problem 14.7:Palindrome check 

**Code:**
```python
def is_palindrome(text):
    # Normalize the text by lowering case and removing spaces
    clean_text = text.replace(" ", "").lower()
    
    # Reverse the cleaned text
    reversed_text = clean_text[::-1]
    
    # Check if content matches
    return clean_text == reversed_text

# Example usage
print("Madam is palindrome: ", is_palindrome("Madam"))                # True
print("Python is palindrome: ", is_palindrome("Python"))               # False
print("A man a plan a canal Panama is palindrome: ", is_palindrome("A man a plan a canal Panama"))  # True
```

**Output:**
```python
Madam is palindrome:  True
Python is palindrome:  False
A man a plan a canal Panama is palindrome:  True
```

### Problem 14.8: Longest and smallest Word in a Sentence. 

**Code:**
```python
sentence = "Write clean and readable code"

# Split the sentence into words
# .split() breaks the sentence into individual words.
words = sentence.split()   # words = ['Write', 'clean', 'and', 'readable', 'code']

# Find the longest word using max() with key = len
# max() normally finds the maximum value in a list.
# key=len tells Python to compare items by their length, not their default order (e.g., alphabetical).
longest_word = max(words, key=len)

# Find the smallest word using min() with key = len
smallest_word = min(words, key=len)

# Print the result
print(f"Longest word: {longest_word} (length: {len(longest_word)})")
print(f"Smallest word: {smallest_word} (length: {len(smallest_word)})")
```

**Output:**
```python
Longest word: readable (length: 8)
Smallest word: and (length: 3)
```

### Problem 14.9: Uppercase & Lowercase 

**Code:**
```python
text = "Hello World"
print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world
```

**Output:**
```python
HELLO WORLD
hello world
```

### Problem 14.10: Count Specific Character

**Code:**
```python
text_1 = "Experience is everything"
print(f"Count of character e is {text_1.count('e')}")  # Output: Count of character e is 5
```

**Output:**
```python
Count of character e is 5
```

### Problem 14.11: Replace Substring

**Code:**
```python
sentence_11 = "This is a bad example"
print(sentence_11.replace("bad", "good"))  # Output: This is a good example
print("Previous Sentence was =", sentence_11)
```

**Output:**
```python
This is a good example
Previous Sentence was = This is a bad example
```

### Problem 14.12: Concatenate Strings
**Code:**
```python
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World
```

**Output:**
```python
Hello World
```

### Problem 14.13: Count Vowels & Consonants
**Code:**
```python
def count_vc(text):
    vowels = "aeiouAEIOU"
    v = sum(1 for c in text if c in vowels)
    c = sum(1 for c in text if c.isalpha() and c not in vowels)
    return v, c

print(f"Vowel & Consonant count is {count_vc("Python")}")  # (1, 5)
```

**Output:**
```python
Vowel & Consonant count is (1, 5)
```

## 15. Python String Operations: String Slicing

### Problem 15.1: string slicing


**Code:**
```python
text = "Hello World!"
# text[:5] means start from index 0 up to but not including index 5
first_five = text [:5]

# start at index -5 and go to the end.
last_five = text [-5:]

print("First five: ", first_five)
print("Last five: ", last_five)
```

**Output:**
```python
First five:  Hello
Last five:  orld!
```

### Problem 15.2: Extract Substring. Extract the word "Programming" using slicing from text = "PythonProgramming" 


**Code:**
```python
text_2 = "PythonProgramming"
print("Extracted substring: ", text_2[6:])  # Output: Programming
```

**Output:**
```python
Extracted substring:  Programming
```

### Problem 15.3: Get Every Second Character 


**Code:**
```python
text_3 = "ABCDEFGHIJK"
print(text_3)
print("Extracted every second char is: ", text_3[::2]) # ACEGIK
```

**Output:**
```python
ABCDEFGHIJK
Extracted every second char is:  ACEGIK
```


### Problem 15.4: Reverse a String Using Slicing 


**Code:**
```python
text = "DataScience"
print(text)
print(text[::-1]) # Output: ecneicSataD
```

**Output:**
```python
DataScience
ecneicSataD
```


### Problem 15.5: First Half and Second Half 


**Code:**
```python
text = "PythonIsFun"
mid = len(text) // 2 
print("First Half: ", text[:mid])    # First Half:  Pytho
print("Second Half: ", text[mid:])   # Second Half:  nIsFun
```

**Output:**
```python
First Half:  Pytho
Second Half:  nIsFun
```

### Problem 15.6: Remove First and Last Character


**Code:**
```python
text = "SlicingExample"
print(text[1:-1])      # Output: licingExampl
```

**Output:**
```python
licingExampl
```

### Problem 15.7: Last 3 Characters 


**Code:**
```python
text = "MachineLearning"
print("Full String is: ", text)
print("Last three character is: ", text[-3:]) # Output: ing
```

**Output:**
```python
Full String is:  MachineLearning
Last three character is:  ing
```

### Problem 15.8: Slice From Middle 


**Code:**
```python
text = "Artificial"
print("Full string: ", text)
print(text[4:8])              # Output:fici
```

**Output:**
```python
Full string:  Artificial
fici
```

### Problem 15.9: Odd and Even Indexed Characters 


**Code:**
```python
text = "IndexingExample"
print("Full string: ", text)
print("Even Index: ", text[::2]) # Output: Idxnxml
print("Odd Index: ", text[1::2]) # Output: neigxml
```

**Output:**
```python
Full string:  IndexingExample
Even Index:  IdxnEape
Odd Index:  neigxml
```

## 16. Python String Operations: .strip(), .find(), .replace(), .split() function 

### Problem 16.1: Removing Whitespace

- strip() removes leading and trailing whitespace (spaces, tabs, etc.).
- text.strip() returns "Hello, World!" with no spaces at the beginning or end.
- This does not remove spaces inside the string.

**Code:**
```python
text = "   Hello, World!   "
trimmed = text.strip()
print("Original text:", text)
print("Trimmed text:", trimmed)
```

**Output:**
```python
Original text:    Hello, World!   
Trimmed text: Hello, World!
```

### Problem 16.2: Finding a Substring
- find() searches for a substring within a string.
- Returns the starting index of the first match. In this case, "World" starts at 7.
- If the substring is not found, it returns -1.

**Code:**
```python
text = "Hello, World!"
# find() searches for a substring within a string.
# Returns the starting index of the first match. 
position = text.find("World")  
print("Position of the 'World':", position)
```

**Output:**
```python
Position of the 'World': 7
```

### Problem 16.3: Replacing a Substring

- replace() swaps every occurrence of the first substring with the second.
- "World" is replaced by "Python" → "Hello, Python!"
- It is case-sensitive: "world" wouldn’t match "World".

**Code:**
```python
text = "Hello, World!"
new_text = text.replace("World", "Python")
print("Original text:", text)
print("Replaced text:", new_text) # Replaced text: Hello, Python!
```

**Output:**
```python
Original text: Hello, World!
Replaced text: Hello, Python!
```

### Problem 16.4: Checking for a Substring

- The in keyword checks if a substring exists inside another string.
- Returns True if found, False if not.
- "World" in text evaluates to True because the string contains "World".

**Code:**
```python
text = "Hello, World!"
check = "World" in text
print("Contains 'World':", check)
```

**Output:**
```python
Contains 'World': True
```




### Problem 16.5: Splitting a String

- The split() function splits the string into parts wherever the given delimiter (,) occurs.
- It returns a list of substrings.
- The delimiter in split(delimiter) can be: comma(,), space(" "), colon(:) or any custom string
- If no delimiter is passed, it defaults to whitespace.

**Code:**
```python
text = "apple,banana,cherry"
fruits = text.split(",")
print("Split list:", fruits) # Output: Split list: ['apple', 'banana', 'cherry']
```

**Output:**
```python
Split list: ['apple', 'banana', 'cherry']
```

## 17. Python list data operation

- Best Practice: Avoid naming your variables after Python built-ins like: **list**, **set**, **dict**, **str**, **int**, **input**, **print**, etc.

### Problem 17.1: Create a list of five integers and print it.

**Code:**
```python
nums = [1, 2, 3, 4, 5]
print("List of five intergers: ", nums)
```

**Output:**
```python
List of five intergers:  [1, 2, 3, 4, 5]
```

### Problem 17.2: Accessing elements using index


**Code:**
```python
my_list = [1, 2, 3, 4, 5]
# elements can be accessed using their index
print("First element:", my_list[0])  # To access the first element.
print("Last element:", my_list[-1]) # To access the last element.
print("Third element:", my_list[2])  # To access the 3rd element.
```

**Output:**
```python
First element: 1
Last element: 5
Third element: 3
```

### Problem 17.3: Change the second item to 100.


**Code:**
```python
my_list = [1, 2, 3, 4, 5]
my_list[1] = 100
print("New list:", my_list)  # New list: [1, 100, 3, 4, 5]
```

**Output:**
```python
New list: [1, 100, 3, 4, 5]
```

### Problem 17.4: Appending Elements (number 50) to the list.
- append() is a method used to add an item to the end of a list.
- nums.append(50) adds the number 50 as the last element of the nums list.


**Code:**
```python
my_list = [1, 2, 3, 4, 5]
my_list.append(50)
print("Post append list: ", my_list) # Output: [1, 2, 3, 4, 5, 50]
```

**Output:**
```python
Post append list:  [1, 2, 3, 4, 5, 50]
```


### Problem 17.5: Inserting Elements (200) at index 2.
- insert(index, value) adds a value at a specific position in the list.
- nums.insert(2, 200) inserts 200 at index 2, pushing the rest of the items one position to the right.


**Code:**
```python
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 200)
print("Post insert list: ", my_list)  # Output: [1, 2, 200, 3, 4, 5]
```

**Output:**
```python
Post insert list:  [1, 2, 200, 3, 4, 5]
```

### Problem 17.6: Remove the value (100) from the list.
- .remove() Removes the first occurrence of the value 1.
- If the value is not found, raises ValueError.


**Code:**
```python
my_list = [1, 100, 3, 4, 5]
my_list_1 = [1, 100, 2, 3, 4]
my_list_2 = [1, 1, 100, 2, 3, 4]
my_list.remove(100)
my_list_1.remove(2)
my_list_2.remove(1)
print(my_list)     # Output: [1, 3, 4, 5]
print(my_list_1)   # Output: [1, 100, 3, 4]
print(my_list_2)   # Output: [1, 100, 2, 3, 4]
```

**Output:**
```python
[1, 3, 4, 5]
[1, 100, 3, 4]
[1, 100, 2, 3, 4]
```

### Problem 17.7: Pop the last element
- Removes the last element and returns it.
- You can also specify an index: pop(0) to remove the first item.


**Code:**
```python
my_list = [1, 100, 3, 4, 5, 200]
popped = my_list.pop()
popped_1 = my_list.pop(1)
print("Popped element: ", popped) # Output: 200
print("Popped a specific element: ", popped_1) # Output: 100
print(my_list)  # Output: [1, 3, 4, 5]
```

**Output:**
```python
Popped element:  200
Popped a specific element:  100
[1, 3, 4, 5]
```

### Problem 17.8: Sort the list in ascending order.
- Sorts the list in ascending order.
- It modifies the original list in-place.


**Code:**
```python
my_list = [1, 10, 3, 40, 5, 20]
my_list.sort()
print("Ascending order of list: ", my_list) # Output: [1, 3, 5, 10, 20, 40]
```

**Output:**
```python
Ascending order of list:  [1, 3, 5, 10, 20, 40]
```

### Problem 17.9: Find the length of the list using len().


**Code:**
```python
my_list = [1, 3, 5, 10, 20, 40]
print("Length of the list: ", len(my_list)) # Output: 6
```

**Output:**
```python
Length of the list:  6
```

### Problem 17.10: Reverse the list using .reverse()


**Code:**
```python
my_list = [1, 3, 5, 10, 20, 40]
my_list.reverse()
print("Reversed list: ", my_list) # Reversed list:  [40, 20, 10, 5, 3, 1]
```

**Output:**
```python
Reversed list:  [40, 20, 10, 5, 3, 1]
```


### Problem 17.11: Count how many times "Bangladesh" appears.


**Code:**
```python
country = ["Bangladesh", "Nepal", "Bangladesh", "Japan", "Mali", "Bangladesh"]
print(f"'Bangladesh' appears {country.count("Bangladesh")} times")
```

**Output:**
```python
'Bangladesh' appears 3 times
```

### Problem 17.12: Finding the Index of an Element
- Returns the index of the first occurrence of the given value.
- Raises ValueError if not found.


**Code:**
```python
my_list = [1, 3, 5, 10, 20, 40]
index = my_list.index(20)
print("Index of element '20' is: ", index)
```

**Output:**
```python
Index of element '20' is:  4
```


### Problem 17.13: Extending a List .extend()
- Adds elements of another list to the current list.
- [1, 2] extended by [3, 4] becomes [1, 2, 3, 4].


**Code:**
```python
my_list = [1, 3, 5, 10, 20, 40]
my_list.extend([30, 50])
print("Extended list: ", my_list)  # Output: [1, 3, 5, 10, 20, 40, 30, 50]
```

**Output:**
```python
Extended list:  [1, 3, 5, 10, 20, 40, 30, 50]
```

### Problem 17.14: Merging Two Lists
- The + operator combines two lists into one.
- [1, 2] + [3, 4] → [1, 2, 3, 4].


**Code:**
```python
list_1 = [1, 3, 5]
list_2 = [2, 4, 6]
merged_list = list_1 + list_2
print("Merged list: ", merged_list) # Output: [1, 3, 5, 2, 4, 6]
```

**Output:**
```python
Merged list:  [1, 3, 5, 2, 4, 6]
```


### Problem 17.15: Print only even-indexed elements.


**Code:**
```python
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print("Even indexed element: ", nums[::2])
print("Odd indexed element: ", nums[1::2])
```

**Output:**
```python
Even indexed element:  [10, 30, 50, 70]
Odd indexed element:  [20, 40, 60, 80]
```

### Problem 17.16: Slice the last 3 elements from a list.


**Code:**
```python
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print("Last 3 elements: ", nums[-3:]) # Output: Last 3 elements:  [60, 70, 80]
```

**Output:**
```python
Last 3 elements:  [60, 70, 80]
```

### Problem 17.17: Join a list of words into a sentence.
- " " (a space) is the separator. It tells Python to place a space between each word.
- .join(words) joins all elements in the words list into one string, with a space between them.

**Code:**
```python
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Joined list of words:", sentence)
```

**Output:**
```python
Joined list of words: Python is awesome
```

### Problem 17.18: Split a sentence into a list of words.


**Code:**
```python
sentence = "Python is awesome"
print("Splited sentence: ", sentence.split()) # Output: ['Python', 'is', 'awesome']
```

**Output:**
```python
Splited sentence:  ['Python', 'is', 'awesome']
```

### Problem 17.19: Remove duplicates from a list.


**Code:**
```python
nums = [1, 2, 2, 3, 4, 4]
remove_duplicate = set(nums)         # Removes duplicates
print("Remove the duplicates: ", remove_duplicate) # Output: {1, 2, 3, 4}
unique_nums = list(remove_duplicate) # Converts set back to list
# unique_nums = list(set(nums))
print("Unique list: ", unique_nums)  # Output: [1, 2, 3, 4]
```

**Output:**
```python
Remove the duplicates:  {1, 2, 3, 4}
Unique list:  [1, 2, 3, 4]
```

### Problem 17.20: Find the max and min from a list.


**Code:**
```python
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"Maximum={max(nums)}, Minimum={min(nums)}") # Output: Maximum=80, Minimum=10
```

**Output:**
```python
Maximum=80, Minimum=10
```

### Problem 17.21: Return the sum of all items in a list.


**Code:**
```python
nums = [10, 20, 30, 40, 50, 60, 70, 80]
# Defines a function named sum_list that accepts one parameter lst
def sum_list(lst):
    return sum(lst)
# built-in sum() function to add up all elements in lst, then returns that total.
print("Sum of the all items=", sum_list(nums)) # Output: Sum of the all items= 360
```

**Output:**
```python
Sum of the all items= 360
```

### Problem 17.22: Replace all occurrences of 5 with 50.


**Code:**
```python
nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]
nums = [50 if x == 5 else x for x in nums]
# 50 if x == 5 else x
# If x equals 5, replace it with 50.
# Otherwise keep x unchanged.
print("Replaced list: ", nums) # Output: Replaced list:  [1, 2, 2, 3, 4, 4, 50, 50, 50]
```

**Output:**
```python
Replaced list:  [1, 2, 2, 3, 4, 4, 50, 50, 50]
```

### Problem 17.23: Print each item with its index.


**Code:**
```python
colors = ["red", "blue", "green"]
for i, color in enumerate(colors):
    print(i, color)
# enumerate(colors), Returns an iterator that yields pairs: (index, value)
```

**Output:**
```python
0 red
1 blue
2 green
```

### Problem 17.24: Flatten a nested list.


**Code:**
```python
nested = [[1, 2], [3, 4], [5], [8, 9, 10]]
flat = [item for sublist in nested for item in sublist]
# One loop to go through each sublist (e.g., [1, 2])
# Another loop to go through each item inside that sublist (e.g., 1, then 2)
print("Flattened nested list: ", flat) # Output: [1, 2, 3, 4, 5, 8, 9, 10]
```

**Output:**
```python
Flattened nested list:  [1, 2, 3, 4, 5, 8, 9, 10]
```


### Problem 17.25: Find the second largest number.


**Code:**
```python
nums = [1, 4, 2, 9, 7]
nums.sort()
print("Second Largest: ", nums[-2])
```

**Output:**
```python
Second Largest:  7
```


### Problem 17.26: Rotate list right by 2 positions.


**Code:**
```python
nums     = [1, 2, 3, 4, 5]
rotated  = nums[-2:] + nums[:-2]
# nums[-2:]	Slice from index -2 to the end (the last 2 items).	[4, 5]
# nums[:-2]	Slice from start up to (but not including) index -2 (everything except the last 2 items).	[1, 2, 3]
print("Two position rotated list: ", rotated)
```

**Output:**
```python
Two position rotated list:  [4, 5, 1, 2, 3]
```


### Problem 17.27: Check if list is a palindrome.


**Code:**
```python
def is_palindrome(lst):
    return lst == lst[::-1]

print("Palindrom status is: ", is_palindrome([1, 2, 3, 2, 1]))  # True
```

**Output:**
```python
Palindrom status is:  True
```



### 18.1  Python 



**Code:**
```python

```

**Output:**
```python

```