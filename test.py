# Problem 17.19: Remove duplicates from a list.

nums = [1, 2, 2, 3, 4, 4]
remove_duplicate = set(nums)         # Removes duplicates
print("Remove the duplicates: ", remove_duplicate) # Output: {1, 2, 3, 4}
unique_nums = list(remove_duplicate) # Converts set back to list
print("Unique list: ", unique_nums)  # Output: [1, 2, 3, 4]