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