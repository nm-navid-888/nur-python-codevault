#=========Problem 15.1========#
# Problem 15.1: string slicing

text = "Hello World!"
# text[:5] means start from index 0 up to but not including index 5
first_five = text [:5]

# start at index -5 and go to the end.
last_five = text [-5:]

print("First five: ", first_five)
print("Last five: ", last_five)

#=========Problem 15.2========#
# Problem 15.2: Extract Substring. Extract the word "Programming" using slicing from text = "PythonProgramming"
text_2 = "PythonProgramming"
print("Extracted substring: ", text_2[6:])  # Output: Programming

#=========Problem 15.3========#
# Problem 15.3: Get Every Second Character
text_3 = "ABCDEFGHIJK"
print(text_3)
print("Extracted every second char is: ", text_3[::2]) # ACEGIK

#=========Problem 15.4========#
# Problem 15.4: Reverse a String Using Slicing

text = "DataScience"
print(text)
print(text[::-1]) # Output: ecneicSataD


#=========Problem 15.5========#
# Problem 15.5: First Half and Second Half
text = "PythonIsFun"
mid = len(text) // 2 
print("First Half: ", text[:mid])    # First Half:  Pytho
print("Second Half: ", text[mid:])   # Second Half:  nIsFun

#=========Problem 15.6========#
# Problem 15.6: Remove First and Last Character

text = "SlicingExample"
print(text[1:-1])      # Output: licingExampl

#=========Problem 15.7========#
# Problem 15.7: Last 3 Characters

text = "MachineLearning"
print("Full String is: ", text)
print("Last three character is: ", text[-3:]) # Output: ing

#=========Problem 15.8========#
# Problem 15.8: Slice From Middle

text = "Artificial"
print("Full string: ", text)
print(text[4:8])              # Output:fici

#=========Problem 15.9========#
# Problem 15.9: Odd and Even Indexed Characters

text = "IndexingExample"
print("Full string: ", text)
print("Even Index: ", text[::2]) # Output: Idxnxml
print("Odd Index: ", text[1::2]) # Output: neigxml


