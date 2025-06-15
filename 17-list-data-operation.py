#=========Problem 17.1===========#
# Problem 17.1: Create a list of five integers and print it.

nums = [1, 2, 3, 4, 5]
print("List of five intergers: ", nums)

#=========Problem 17.2===========#
# Problem 17.2: Accessing elements using index

my_list = [1, 2, 3, 4, 5]
# elements can be accessed using their index
print("First element:", my_list[0])  # To access the first element.
print("Last element:", my_list[-1]) # To access the last element.
print("Third element:", my_list[2])  # To access the 3rd element.


#=========Problem 17.3===========#
# Problem 17.3: Change the second item to 100.
my_list = [1, 2, 3, 4, 5]
my_list[1] = 100
print("New list:", my_list)  # New list: [1, 100, 3, 4, 5]


#=========Problem 17.4===========#
# Problem 17.4: Appending Elements (number 50) to the list.
# append() is a method used to add an item to the end of a list.
# nums.append(50) adds the number 50 as the last element of the nums list.

my_list = [1, 2, 3, 4, 5]
my_list.append(50)
print("Post append list: ", my_list) # Output: [1, 2, 3, 4, 5, 50]


#=========Problem 17.5===========#
# Problem 17.5: Inserting Elements (200) at index 2.
# insert(index, value) adds a value at a specific position in the list.
# nums.insert(2, 200) inserts 200 at index 2, pushing the rest of the items one position to the right.

my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 200)
print("Post insert list: ", my_list)  # Output: [1, 2, 200, 3, 4, 5]


#=========Problem 17.6===========#
# Problem 17.6: Remove the value (100) from the list.
# .remove() Removes the first occurrence of the value 1.
# If the value is not found, raises ValueError.

my_list = [1, 100, 3, 4, 5]
my_list_1 = [1, 100, 2, 3, 4]
my_list_2 = [1, 1, 100, 2, 3, 4]
my_list.remove(100)
my_list_1.remove(2)
my_list_2.remove(1)
print(my_list)     # Output: [1, 3, 4, 5]
print(my_list_1)   # Output: [1, 100, 3, 4]
print(my_list_2)   # Output: [1, 100, 2, 3, 4]

#=========Problem 17.7===========#
# Problem 17.7: Pop the last element
# Removes the last element and returns it.
# You can also specify an index: pop(0) to remove the first item.

my_list = [1, 100, 3, 4, 5, 200]
popped = my_list.pop()
popped_1 = my_list.pop(1)
print("Popped element: ", popped) # Output: 200
print("Popped a specific element: ", popped_1) # Output: 100
print(my_list)  # Output: [1, 3, 4, 5]


#=========Problem 17.8===========#
# Problem 17.8: Sort the list in ascending order.
# Sorts the list in ascending order.
# It modifies the original list in-place.

my_list = [1, 10, 3, 40, 5, 20]
my_list.sort()
print("Ascending order of list: ", my_list) # Output: [1, 3, 5, 10, 20, 40]

#=========Problem 17.9===========#
# Problem 17.9: Find the length of the list using len().

my_list = [1, 3, 5, 10, 20, 40]
print("Length of the list: ", len(my_list)) # Output: 6


#=========Problem 17.10===========#
# Problem 17.10: Reverse the list using .reverse()

my_list = [1, 3, 5, 10, 20, 40]
my_list.reverse()
print("Reversed list: ", my_list) # Reversed list:  [40, 20, 10, 5, 3, 1]

#=========Problem 17.11===========#
# Problem 17.11: Count how many times "Bangladesh" appears.

country = ["Bangladesh", "Nepal", "Bangladesh", "Japan", "Mali", "Bangladesh"]
print(f"'Bangladesh' appears {country.count("Bangladesh")} times")

#=========Problem 17.12===========#
# Problem 17.12: Finding the Index of an Element
# Returns the index of the first occurrence of the given value.
# Raises ValueError if not found.

my_list = [1, 3, 5, 10, 20, 40]
index = my_list.index(20)
print("Index of element '20' is: ", index)

#=========Problem 17.13==========#
# Problem 17.13: Extending a List .extend()
# Adds elements of another list to the current list.
# [1, 2] extended by [3, 4] becomes [1, 2, 3, 4].

my_list = [1, 3, 5, 10, 20, 40]
my_list.extend([30, 50])
print("Extended list: ", my_list)  # Output: [1, 3, 5, 10, 20, 40, 30, 50]

#=========Problem 17.14==========#
# Problem 17.14: Merging Two Lists
# The + operator combines two lists into one.
# [1, 2] + [3, 4] → [1, 2, 3, 4].

list_1 = [1, 3, 5]
list_2 = [2, 4, 6]
merged_list = list_1 + list_2
print("Merged list: ", merged_list) # Output: [1, 3, 5, 2, 4, 6]

#=========Problem 17.15==========#
# Problem 17.15: Print only even-indexed elements.
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print("Even indexed element: ", nums[::2])
print("Odd indexed element: ", nums[1::2])



#=========Problem 17.16==========#
# Problem 17.16: Slice the last 3 elements from a list.

nums = [10, 20, 30, 40, 50, 60, 70, 80]
print("Last 3 elements: ", nums[-3:]) # Output: Last 3 elements:  [60, 70, 80]

#=========Problem 17.17==========#
# Problem 17.17: Join a list of words into a sentence.
# " " (a space) is the separator. It tells Python to place a space between each word.
# .join(words) joins all elements in the words list into one string, with a space between them.

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Joined list of words:", sentence)


#=========Problem 17.18==========#
# Problem 17.18: Split a sentence into a list of words.

sentence = "Python is awesome"
print("Splited sentence: ", sentence.split()) # Output: ['Python', 'is', 'awesome']


#=========Problem 17.19==========#
# Problem 17.19: Remove duplicates from a list.

nums = [1, 2, 2, 3, 4, 4]
remove_duplicate = set(nums)         # Removes duplicates
print("Remove the duplicates: ", remove_duplicate) # Output: {1, 2, 3, 4}
unique_nums = list(remove_duplicate) # Converts set back to list
# unique_nums = list(set(nums))
print("Unique list: ", unique_nums)  # Output: [1, 2, 3, 4]

# Remove the duplicates:  {1, 2, 3, 4}
# Unique list:  [1, 2, 3, 4]

#=========Problem 17.20==========#
# Problem 17.20: Find the max and min from a list.

nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"Maximum={max(nums)}, Minimum={min(nums)}") # Output: Maximum=80, Minimum=10

#=========Problem 17.21===========#
# Problem 17.21: Return the sum of all items in a list.

nums = [10, 20, 30, 40, 50, 60, 70, 80]
# Defines a function named sum_list that accepts one parameter lst
def sum_list(lst):
    return sum(lst)
# built-in sum() function to add up all elements in lst, then returns that total.
print("Sum of the all items=", sum_list(nums)) # Output: Sum of the all items= 360

#=========Problem 17.22===========#
# Problem 17.22: Replace all occurrences of 5 with 50.

nums = [1, 2, 2, 3, 4, 4, 5, 5, 5]
nums = [50 if x == 5 else x for x in nums]
# 50 if x == 5 else x
# If x equals 5, replace it with 50.
# Otherwise keep x unchanged.
print("Replaced list: ", nums) # Output: Replaced list:  [1, 2, 2, 3, 4, 4, 50, 50, 50]


#=========Problem 17.23==========#
# Problem 17.23: Print each item with its index.

colors = ["red", "blue", "green"]
for i, color in enumerate(colors):
    print(i, color)
# enumerate(colors), Returns an iterator that yields pairs: (index, value)


#=========Problem 17.24==========#
# Problem 17.24: 

nested = [[1, 2], [3, 4], [5], [8, 9, 10]]
flat = [item for sublist in nested for item in sublist]
# One loop to go through each sublist (e.g., [1, 2])
# Another loop to go through each item inside that sublist (e.g., 1, then 2)
print("Flattened nested list: ", flat) # Output: [1, 2, 3, 4, 5, 8, 9, 10]


#=========Problem 17.25===========#
# Problem 17.25: Find the second largest number.

nums = [1, 4, 2, 9, 7]
nums.sort()
print("Second Largest: ", nums[-2])


#=========Problem 17.26===========#
# Problem 17.26: Rotate list right by 2 positions.

nums     = [1, 2, 3, 4, 5]
rotated  = nums[-2:] + nums[:-2]
# nums[-2:]	Slice from index -2 to the end (the last 2 items).	[4, 5]
# nums[:-2]	Slice from start up to (but not including) index -2 (everything except the last 2 items).	[1, 2, 3]
print("Two position rotated list: ", rotated)

#=========Problem 17.27===========#
# Problem 17.27: Check if list is a palindrome.

def is_palindrome(lst):
    return lst == lst[::-1]

print("Palindrom status for is: ", is_palindrome([1, 2, 3, 2, 1]))  # True
