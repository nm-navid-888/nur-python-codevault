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
