# List comprehension is a concise way to create lists in Python.

#========Problem-18.1=======#
# Problem-18.1: Create a list of numbers from 1 to 10.
# [expression for item in iterable]
# range(1, 11) means range(start, stop) generates numbers starting from start up to (but not including) stop.


nums = [x for x in range(1, 11)]
## for x in range(1, 11) => This loops over each number in the range from 1 to 10.
# => Each number is temporarily assigned to the variable x.
## x => This is the expression for each item in the new list.
print("List of numbers from 1 to 10 = ", nums) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#========Problem-18.2=======#
# Problem-18.2: Squares of numbers from 1 to 10 and Cubes from 1 to 5

squares = [x**2 for x in range(1, 11)]
cubes = [x**3 for x in range(1, 6)]
print("Square of numbers from 1 to 10 =", squares)
print("Cube of numbers from 1 to 5 =", cubes)



#========Problem-18.3=======#
# Problem-18.3: Even numbers from 0 to 20.
even_nums = [x for x in range(0, 21) if x % 2 == 0]
print("Even numbers from 0 to 20 = ", even_nums)

#========Problem-18.4=======#
# Problem-18.4: Lengths of words and convert all items to uppercase and lowercase

words = ["Engineers", "Grandiloquent", "python", "code", "AI"]
length = [len(word) for word in words]
uppercase_words = [word.upper() for word in words]
lowercase_words = [word.lower() for word in words]
print("Print the word list =", words)
print("Length of the words in the list =", length)
print("Uppercase words = ", uppercase_words)
print("Lowercase words = ", lowercase_words)

#========Problem-18.5=======#
# Problem-18.5: Filter words longer than 4 characters

words = ["Engineers", "Grandiloquent", "python", "code", "AI"]
filtered = [word for word in words if len(word) > 4 ]
print("Words in list longer than 4 char =", filtered) # output: ['Engineers', 'Grandiloquent', 'python']


#========Problem-18.6=======#
# Problem-18.6:Integers to strings

nums = [1, 3, 6, 10, 15, 21]
as_str = [str(num) for num in nums]
print("Integer to string = ", as_str) # output: ['1', '3', '6', '10', '15', '21']


#========Problem-18.7=======#
# Problem-18.7: Numbers divisible by 3

div_by_3 = [num for num in range(1, 31) if num % 3 ==0]
print("Number divisible by 3 from 1 to 30 =", div_by_3) # output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


#========Problem-18.8=======#
# Problem-18.8: Add 10 to each element

nums = [1, 3, 6, 10, 15, 21]
add_10 = [num + 10 for num in nums]
print("List of the numbers = ", nums)
print("Added 10 to each element = ", add_10)


#========Problem-18.9=======#
# Problem-18.9: Tuples of number and square

nums = [1, 3, 6, 10, 15, 21]
pairs = [(num, num**2) for num in nums]
parir_2 = [(x, x**2) for x in range(1, 6)]
print("Tuple of number and square =", pairs) # output: [(1, 1), (3, 9), (6, 36), (10, 100), (15, 225), (21, 441)]
print("Tuple of nubers and square from 1 to 5: ", parir_2) # output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]


#========Problem-18.10=======#
# Problem-18.10: Reversed words

words = ['Python', 'is', 'awesome']
reversed_word = [word[::-1] for word in words]
print("Reversed word list: ", reversed_word) # output: ['nohtyP', 'si', 'emosewa']


#========Problem-18.11=======#
# Problem-18.11: Extract vowels

vowels_count = [v for v in "programming" if v in 'aeiou']
print("Vowel count is: ", vowels_count) # output: ['o', 'a', 'i']


#========Problem-18.12=======#
# Problem-18.12: Extract alphabetic characters

text = "abc123@!"
alpha = [c for c in text if c.isalpha()]
print("Extracted alphabet: ", alpha)
