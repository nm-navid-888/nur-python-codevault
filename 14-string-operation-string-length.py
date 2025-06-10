# Problem 1: Print the total number of characters in the string (including spaces).

text = "pyhton programming"
length = len(text)         
print("Text length including spaces = ", length)  

# Problem 2: Check String Length Limit 

username = input("Enter the username: ") # input() takes user input as a string.

if len(username) > 10:     # len(username) checks how many characters the username has
    print("Too Long !")
else:
    print("Accepted")

# Problem 3: Compare Two String Lengths
# Take two strings and compare their lengths. Print which string is longer or if they are equal in length.

name_1 = "usman abdullah"
name_2 = "arpita paul"

if len(name_1) > len(name_2):
    print("name_1 is longer")
elif len(name_1) < len(name_2):
    print("name_2 is longer")
else:
    print("both string are equal")

# Problem 4: Count Letters Without Spaces

text = "Data Science with Python"

# Remove spaces and count remaining characters
count_without_space = len(text.replace(" ", ""))
print("Number of characters with space", len(text))
print("Number of characters without space:", count_without_space)








