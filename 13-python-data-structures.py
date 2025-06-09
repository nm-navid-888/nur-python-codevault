# 13.1  Python Data Structures (list) 

fruits = ["apple", "banana", "cherry", "banana"]
fruits.append("mango")     # .append() method adds an element to the end of the list.
fruits.remove("banana")    # .remove() method removes the first occurrence of "banana" from the list.
print(fruits)
# Count how many times "banana" appears
print(fruits.count("banana"))

# 13.2  Python Data Structures (tuple) 

coordinates = (10.0, 20.5)
print(coordinates[0])          # 10.0

# Convert to list, modify, then back to tuple
mod_tuple = list(coordinates)  
print(mod_tuple)               # mod_tuple = [10.0, 20.5]
mod_tuple.append(30.0)         # adds an element to the end of the list.
print(mod_tuple)               # mod_tuple =  [10.0, 20.5, 30.0]
coordinates = tuple(mod_tuple) # convert list to tuple
print(coordinates)             # (10.0, 20.5, 30.0)

# 13.2  Python Data Structures (Dictionary) 

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

# 13.6  Python Data Structures (counter)

from collections import Counter

votes = ["A", "B", "A", "C", "B", "A"] # representing votes for different candidates.
# Counter(votes) counts each unique element and returns a dictionary-like object
tally = Counter(votes)                 
print(tally)                           # Counter({'A': 3, 'B': 2, 'C': 1})
print(tally["A"])                      # 3
print(tally["D"])                      # 0 (does not raise an error)

# 13.7  Python Data Structures (Heap)

import heapq

tasks = [3, 1, 4, 2]
heapq.heapify(tasks)         # Rearranges the list in-place to satisfy heap properties.
print(tasks)                 # [1, 2, 4, 3]
heapq.heappush(tasks, 0)     # Adds 0 to the heap and maintains the min-heap structure.
print(tasks)                 # [0, 1, 4, 3, 2]
print(heapq.heappop(tasks))  # 0 (lowest priority)



