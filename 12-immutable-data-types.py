# Integer (Immutable)

x = 5
print(id(x))  # memory address of x
x += 1
print(id(x))  # different address — new object created

# String (Immutable)

greeting = "Hello"
print(greeting.upper())   # returns new string
print(greeting)           # original string unchanged

# Tuple (Immutable)

my_tuple = (1, 2, 3)
# my_tuple[0] = 9          # Error: Tuples are immutable
#print(my_tuple)


# Frozen Set (Immutable)

vowels = frozenset({"a", "e", "i","o","u"})
vowels.add("y")          # Error: frozenset does not support add()
print(vowels)