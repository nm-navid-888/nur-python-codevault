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


## Python String Operations

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

### 13.1  Python Data Structures (list) 

**Code:**
```python

```

**Output:**
```python

```