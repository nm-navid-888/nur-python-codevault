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