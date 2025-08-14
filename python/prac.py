import math

# Area of rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area_rectangle = length * breadth
print("Area of Rectangle =", area_rectangle)

# Area of square
side = float(input("\nEnter side of square: "))
area_square = side * side
print("Area of Square =", area_square)

# Area of circle
radius = float(input("\nEnter radius of circle: "))
area_circle = math.pi * radius * radius
print("Area of Circle =", area_circle)



# Program to find first 5 multiples of a number

# Input from user
num = int(input("Enter a number: "))

# Printing first 5 multiples
print("The first 5 multiples of", num, "are:")
for i in range(1, 6):
    print(num * i)


# Program to show the working of escape sequences

print("Demonstrating Escape Sequences in Python\n")

# \n - New line
print("Hello\nWorld")  

# \t - Tab space
print("Name:\tPriya")

# \\ - Backslash
print("This is a backslash: \\")

# \' - Single quote
print('It\'s a sunny day')

# \" - Double quote
print("She said, \"Python is fun!\"")

# \b - Backspace
print("Helloo\b World")  

# \r - Carriage return
print("Python\rJava")  

# \f - Form feed (may vary in output depending on environment)
print("Hello\fWorld")



print("Temperature Conversion Program")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    # Fahrenheit to Celsius
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius =", c)

elif choice == 2:
    # Celsius to Fahrenheit
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit =", f)

else:
    print("Invalid choice! Please select 1 or 2.")


# 1. Swapping using a temporary variable

# Swapping numbers using a temporary variable

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swap using temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)


#  Swapping without using a temporary variable
# python

# Swapping numbers without a temporary variable

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swap without variable (using arithmetic)
a = a + b
b = a - b
a = a - b

print("\nAfter swapping:")
print("a =", a)
print("b =", b)



# Input height in centimeters
cm = float(input("Enter height in centimeters: "))

# 1 inch = 2.54 cm, 1 foot = 12 inches
inches_total = cm / 2.54

# Calculate feet and inches
feet = int(inches_total // 12)  # Whole feet
inches = inches_total % 12      # Remaining inches

# Output
print("Height in feet and inches = ", feet, "feet and", round(inches, 2), "inches")



# Program to calculate Simple Interest and Compound Interest

# Input values
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Calculate Compound Interest
# Formula: CI = P * (1 + R/100)^T - P
compound_amount = principal * (1 + rate / 100) ** time
compound_interest = compound_amount - principal

# Display results
print("Simple Interest =", simple_interest)
print("Compound Interest =", compound_interest)



# Input number of days
days = int(input("Enter number of days: "))

# 1 year = 365 days, 1 month = 30 days, 1 week = 7 days
years = days // 365
remaining_days = days % 365

months = remaining_days // 30
remaining_days = remaining_days % 30

weeks = remaining_days // 7
remaining_days = remaining_days % 7

# Output the results
print("Years:", years)
print("Months:", months)
print("Weeks:", weeks)
print("Days:", remaining_days)



# Program to enter n and print n^2, n^3, n^4

# Taking input from user
n = int(input("Enter a number: "))

# Calculating powers
n2 = n ** 2   # Square
n3 = n ** 3   # Cube
n4 = n ** 4   # Fourth power

# Displaying results
print("n^2 =", n2)
print("n^3 =", n3)
print("n^4 =", n4)



# Program to show the working of sep and end arguments in print()

# Using 'sep' (separator)
print("Apple", "Banana", "Cherry", sep=", ")
print("10", "20", "30", sep="-")
print("Python", "Java", "C++", sep=" | ")

print()  # Empty line for clarity

# Using 'end'
print("Hello", end=" ")
print("World!")  # Both will be on the same line
print("Good", end="***")
print("Morning")

print()  # Empty line for clarity

# Using both 'sep' and 'end'
print("A", "B", "C", sep=":", end=" - ")
print("X", "Y", "Z", sep=":")



# Program to find quotient and remainder

# Input two numbers
num1 = int(input("Enter the first number (dividend): "))
num2 = int(input("Enter the second number (divisor): "))

# Calculate quotient and remainder
quotient = num1 // num2    # Integer division
remainder = num1 % num2    # Modulus operator

# Display the results
print("Quotient =", quotient)
print("Remainder =", remainder)


# Program to declare different types of variables 
# and print their values, types, and ids

# Integer variable
a = 10

# Float variable
b = 3.14

# String variable
c = "Hello"

# Boolean variable
d = True

# Complex number
e = 2 + 3j

# Printing values, types and ids
print("Value of a:", a, " Type:", type(a), " ID:", id(a))
print("Value of b:", b, " Type:", type(b), " ID:", id(b))
print("Value of c:", c, " Type:", type(c), " ID:", id(c))
print("Value of d:", d, " Type:", type(d), " ID:", id(d))
print("Value of e:", e, " Type:", type(e), " ID:", id(e))



# Program to convert days into years, months, weeks and remaining days

# Input from user
days = int(input("Enter the number of days: "))

# Converting days
years = days // 365
remaining_days_after_years = days % 365

months = remaining_days_after_years // 30
remaining_days_after_months = remaining_days_after_years % 30

weeks = remaining_days_after_months // 7
remaining_days = remaining_days_after_months % 7

# Output
print("Years:", years)
print("Months:", months)
print("Weeks:", weeks)
print("Days:", remaining_days)