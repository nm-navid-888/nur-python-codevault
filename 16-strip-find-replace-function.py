#=========Problem 16.1===========#
# Problem 16.1: Removing Whitespace
text = "   Hello, World!   "
trimmed = text.strip()
print("Original text:", text)
print("Trimmed text:", trimmed)

#=========Problem 16.2===========#
# Problem 16.2: Finding a Substring

text = "Hello, World!"
# find() searches for a substring within a string.
# Returns the starting index of the first match. 
position = text.find("World")  
print("Position of the 'World':", position)


#=========Problem 16.3===========#
# Problem 16.3: Replacing a Substring

text = "Hello, World!"
new_text = text.replace("World", "Python")
print("Original text:", text)
print("Replaced text:", new_text) # Replaced text: Hello, Python!


#=========Problem 16.4===========#
# Problem 16.4: Checking for a Substring

text = "Hello, World!"
check = "World" in text
print("Contains 'World':", check)

