# Example 1: Age Category Checker

age = int(input("Enter the age ="))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 2: Grading System

marks = int(input("Enter the mark ="))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade F")

# Example 3: Number Checker (Positive, Negative, Zero)

num = int(input("Enter the number = "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Example 4: Even or Odd Checker

number = int(input("Enter the number = "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 5: Login Simulation


username = input("Enter the username = ")
password = input("Enter the password = ")

if username == "admin" and password == "1234":
    print("Login Successful")
elif username != "admin" and password == "1234":
    print("Invalid Username")
elif username == "admin" and password != "1234":
    print("Invalid Credentials")
else:
    print("Invalid Username and Password")

# Example 6: Password Strength Checker

password = input("Enter the password = ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")



