# Problem 14.1: Print the total number of characters in the string (including spaces).

text = "pyhton programming"
length = len(text)         
print("Text length including spaces = ", length)  

# Problem 14.2: Check String Length Limit 

username = input("Enter the username: ") # input() takes user input as a string.

if len(username) > 10:     # len(username) checks how many characters the username has
    print("Too Long !")
else:
    print("Accepted")

# Problem 14.3: Compare Two String Lengths
# Take two strings and compare their lengths. Print which string is longer or if they are equal in length.

name_1 = "usman abdullah"
name_2 = "arpita paul"

if len(name_1) > len(name_2):
    print("name_1 is longer")
elif len(name_1) < len(name_2):
    print("name_2 is longer")
else:
    print("both string are equal")

# Problem 14.4: Count Letters Without Spaces

text = "Data Science with Python"

# Remove spaces and count remaining characters
count_without_space = len(text.replace(" ", ""))
print("Number of characters with space", len(text))
print("Number of characters without space:", count_without_space)

# Problem 14.5: Word Length List

sentence = "Python is powerful and fun"

# Split the sentence into words
words = sentence.split()
# Loop through each word and print its length
for word in words:
    print(f"{word} → {len(word)}")

# Problem 14.6: Reverse Length Checker

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

# Problem 14.7:Palindrome check

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

#========Problem 14.8==========#
# Problem 14.8: Longest and smallest Word in a Sentence.

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

#========Problem 14.9==========#
# Problem 14.9: Uppercase & Lowercase

text = "Hello World"
print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world

#========Problem 14.10==========#
# Problem 14.10: Count Specific Character

text_1 = "Experience is everything"
print(f"Count of character e is {text_1.count('e')}")  # Output: Count of character e is 5

#========Problem 14.11==========#
# Problem 14.11: Replace Substring

sentence_11 = "This is a bad example"
print(sentence_11.replace("bad", "good"))  # Output: This is a good example
print("Previous Sentence was =", sentence_11)

#========Problem 14.12==========#
# Problem 14.12: Concatenate Strings

a = "Hello"
b = "World"
print(a + " " + b)  # Hello World

#========Problem 14.13==========#
# Problem 14.13: Count Vowels & Consonants

def count_vc(text):
    vowels = "aeiouAEIOU"
    v = sum(1 for c in text if c in vowels)
    c = sum(1 for c in text if c.isalpha() and c not in vowels)
    return v, c

print(f"Vowel & Consonant count is {count_vc("Python")}")  # (1, 5)















