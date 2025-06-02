# Example 1: Using integers

x = 8
y = 10

print(x == y)    # False
print(x != y)    # True
print(x > y)     # False
print(x < y)     # True
print(x >= 8)    # True
print(y <= 9)    # False

# Example 2: Using strings

name1 = "Nur"
name2 = "nur"

print(name1 == name2)    # False (case-sensitive)
print(name1 != name2)    # True
print(name1 < name2)     # True ('N' comes before 'n' in ASCII)

# Example 3: Mixing types

a = 5
b = "5"

print(a == int(b))  # True
print(str(a) == b)  # True
print(a != b)       # True (without type conversion)

# Practice Challenge

score = 85
passing_mark = 60

print(score >= passing_mark)     # Expected: True
print(score == 100)              # Expected: False
print(passing_mark < 40)         # Expected: False
