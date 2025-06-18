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

# List comprehension is a concise way to create lists in Python.


### Problem-18.1: Create a list of numbers from 1 to 10.

- [expression for item in iterable]
- range(1, 11) means range(start, stop) generates numbers starting from start up to (but not including) stop.


**Code:**
```python



nums = [x for x in range(1, 11)]
## for x in range(1, 11) => This loops over each number in the range from 1 to 10.
# => Each number is temporarily assigned to the variable x.
## x => This is the expression for each item in the new list.
print("List of numbers from 1 to 10 = ", nums) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Output:**
```python
List of numbers from 1 to 10 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Problem-18.2: Squares of numbers from 1 to 10 and Cubes from 1 to 5


**Code:**
```python
squares = [x**2 for x in range(1, 11)]
cubes = [x**3 for x in range(1, 6)]
print("Square of numbers from 1 to 10 =", squares)
print("Cube of numbers from 1 to 5 =", cubes)
```

**Output:**
```python
Square of numbers from 1 to 10 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube of numbers from 1 to 5 = [1, 8, 27, 64, 125]
```

### Problem-18.3: Even numbers from 0 to 20.


**Code:**
```python
even_nums = [x for x in range(0, 21) if x % 2 == 0]
print("Even numbers from 0 to 20 = ", even_nums)
```

**Output:**
```python
Even numbers from 0 to 20 =  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

### Problem-18.4: Lengths of words and convert all items to uppercase and lowercase


**Code:**
```python
words = ["Engineers", "Grandiloquent", "python", "code", "AI"]
length = [len(word) for word in words]
uppercase_words = [word.upper() for word in words]
lowercase_words = [word.lower() for word in words]
print("Print the word list =", words)
print("Length of the words in the list =", length)
print("Uppercase words = ", uppercase_words)
print("Lowercase words = ", lowercase_words)
```

**Output:**
```python
Print the word list = ['Engineers', 'Grandiloquent', 'python', 'code', 'AI']
Length of the words in the list = [9, 13, 6, 4, 2]
Uppercase words =  ['ENGINEERS', 'GRANDILOQUENT', 'PYTHON', 'CODE', 'AI']
Lowercase words =  ['engineers', 'grandiloquent', 'python', 'code', 'ai']
```

### Problem-18.5: Filter words longer than 4 characters


**Code:**
```python
words = ["Engineers", "Grandiloquent", "python", "code", "AI"]
filtered = [word for word in words if len(word) > 4 ]
print("Words in list longer than 4 char =", filtered) # output: ['Engineers', 'Grandiloquent', 'python']
```

**Output:**
```python
Words in list longer than 4 char = ['Engineers', 'Grandiloquent', 'python']
```


### Problem-18.6:Integers to strings


**Code:**
```python
nums = [1, 3, 6, 10, 15, 21]
as_str = [str(num) for num in nums]
print("Integer to string = ", as_str) # output: ['1', '3', '6', '10', '15', '21']
```

**Output:**
```python
Integer to string =  ['1', '3', '6', '10', '15', '21']
```


### Problem-18.7: Numbers divisible by 3


**Code:**
```python
div_by_3 = [num for num in range(1, 31) if num % 3 ==0]
print("Number divisible by 3 from 1 to 30 =", div_by_3) # output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

**Output:**
```python
Number divisible by 3 from 1 to 30 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```


### Problem-18.8: Add 10 to each element


**Code:**
```python
nums = [1, 3, 6, 10, 15, 21]
add_10 = [num + 10 for num in nums]
print("List of the numbers = ", nums)
print("Added 10 to each element = ", add_10)
```

**Output:**
```python
List of the numbers =  [1, 3, 6, 10, 15, 21]
Added 10 to each element =  [11, 13, 16, 20, 25, 31]
```

### Problem-18.9: Tuples of number and square


**Code:**
```python
nums = [1, 3, 6, 10, 15, 21]
pairs = [(num, num**2) for num in nums]
parir_2 = [(x, x**2) for x in range(1, 6)]
print("Tuple of number and square =", pairs) # output: [(1, 1), (3, 9), (6, 36), (10, 100), (15, 225), (21, 441)]
print("Tuple of nubers and square from 1 to 5: ", parir_2) # output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

**Output:**
```python
Tuple of number and square = [(1, 1), (3, 9), (6, 36), (10, 100), (15, 225), (21, 441)]
Tuple of nubers and square from 1 to 5:  [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```


### Problem-18.10: Reversed words


**Code:**
```python
words = ['Python', 'is', 'awesome']
reversed_word = [word[::-1] for word in words]
print("Reversed word list: ", reversed_word) # output: ['nohtyP', 'si', 'emosewa']
```

**Output:**
```python
Reversed word list:  ['nohtyP', 'si', 'emosewa']
```


### Problem-18.11: Extract vowels


**Code:**
```python
vowels_count = [v for v in "programming" if v in 'aeiou']
print("Vowel count is: ", vowels_count) # output: ['o', 'a', 'i']
```

**Output:**
```python
Vowel count is:  ['o', 'a', 'i']
```


### Problem-18.12: Extract alphabetic characters


**Code:**
```python
text = "abc123@!"
alpha = [c for c in text if c.isalpha()]
print("Extracted alphabet: ", alpha)
```

**Output:**
```python
Extracted alphabet:  ['a', 'b', 'c']
```