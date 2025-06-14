## 15. Python String Operations: String Slicing

### Problem 16.1: Removing Whitespace


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