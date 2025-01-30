# Introduction to Python Tutorials. 400-Level IT class on January 30, 2025

greeting = "Hello dear!"
# print(greeting)


my_name = "Chisom"
my_likes = "fine girls"
my_dislikes = "billing"
age = "21"

# String concatenation
statement = greeting + " I am " + my_name + ". I like " + \
    my_likes + " and dislikes " + my_dislikes + "."
print(statement)

# Conversion of integer to string
number_1 = 30
float_number_1 = float(number_1)
print(float_number_1)

# Conversion of string to uppercase
name = "favour chisom"
uppercase_name = name.upper()
print(uppercase_name)


# Defining a function
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))


def addition(x, y):
    return x + y


print(addition(x, y))
