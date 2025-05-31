print(type ("Welcome to python"))
print(type(10))
\
# 1. Basic Data Types

print("### Check Basic Data Types")
print("Hello => type is ", type("Hello"))           # str
print("100 => type is ", type(100))               # int
print("99.99 => type is ", type(99.99))             # float
print("True => type is ", type(True))              # bool
print("None => type is ", type(None))              # NoneType
\
# 2. List, Tuple, Set, Dictionary

print("###List, Tuple, Set, Dictionary")
print(type([1, 2, 3]))         # list
print(type((1, 2, 3)))         # tuple
print(type({1, 2, 3}))         # set
print(type({"a": 1, "b": 2}))  # dict
# dictionary stores data in key-value pairs. Each key must be unique.
\
# 3. Check all types in one go

print("### Check all types in one go")
values = ["Hi", 10, 3.14, False, None, [1,2], (3,4), {5,6}, {"a":1}]
for val in values:
    print(f"{val} is of type {type(val)}")

# f"{val} is of type {type(val)}" is an f-string, which allows inserting values directly into the string.
# type(val) returns the data type (e.g., <class 'int'>, <class 'str'>).
# The result is printed in a readable format.
\
# 4. Check instance type using isinstance()

a = "Python"
print("### Check instance type using isinstance()")
print(isinstance(a, str))     # True
print(isinstance(a, int))     # False