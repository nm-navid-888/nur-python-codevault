# Python List Comprehension

## What is List Comprehension?
List comprehension is a concise way to create lists in Python using a single line of code.\
Basic Syntax: [expression for item in iterable if condition]\
**Parts Breakdown:**
- **expression:** The value to store in the new list (usually uses item)\
- **for item in iterable:** Iterates over each element in an iterable (like a list, range, etc.)\
- **if condition:** Optional. Filters items based on a condition (only if True)

### Equivalent to for loop

**Code:**
```python
squares = [x**2 for x in range(5)]
```
Is the same as:

**Code:**
```python
squares = []
for x in range(5):
    squares.append(x**2)
```