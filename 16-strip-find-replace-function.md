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