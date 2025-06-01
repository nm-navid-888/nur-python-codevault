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
