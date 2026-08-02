# # # ====================== Part 1 =========================

# # # Print something in python
# print("Hello Mustafa!");
# print("Hello!");

# # # Arthmetic operations
# print(2 + 5)
# print(2 * 5)
# print(2 * 5 + 3)

# # # It take below line as string
# print("2+4")

# # # Taking Input from user
# name = input("what is your name?")
# print("Hello!, Mr/Ms " + name)

# # # Variable referencing (a single variable reference to many times in the program)
# name = input("Please enter your name: ")
# print("Hello!, " + name)
# print("Hello!, " + name)

# # # Task
# name = input("Please enter name: ")
# year = input("Please enter year: ")
# print(
#     name
#     + " is a valiant knight, born in the year"
#     + year
#     + "."
#     + " One morning "
#     + name
#     + " woke up to an awful racket: a dragon was approaching the village. Only "
#     + name
#     + " could save the village's residents."
# )

# # # integer
# name = "ali"
# int = 6000
# print(
#     "This is new no " + str(int)
# )  # Here str convert the integer value (6000) to an string so we combine it with another string other wise it is not possible to add string and integer

# # Another method:
# print(f"Hello {name}, your marks are {int}.")

# ---------------------------------
# # # Floating point numbers
# number1 = 2.5
# number2 = -1.25
# number3 = 3.62

# mean = (number1 + number2 + number3) / 3
# print(f"Mean: {mean}")

# ---------------------------------
# # # Arthemetic Operations:
# height = 172.5
# weight = 68.55


# print(f"+ Operator {height+weight}")
# print(f"- Operator {height-weight}")
# print(f"* Operator {height*weight}")
# print(f"/ Operator {height/weight}")
# print(f"// Operator {height//weight}")
# print(f"** Operator {height**weight}")

# # sum and equal operator, subtractand equal
# height += weight
# height -= weight

# ---------------------------------
# # # Conditional statements
# age = int(input("Please enter your age : "))

# if age < 10:
#     print("Your age is between 0 and 10.")
# if age > 10:
#     print("age is greater than 10")
# if age == 10:
#     print("age is equal to 10")
# if age != 10:
#     print("age is not equal to 10")
# if age <= 10:
#     print("age is not equal to 10 and less than 10")

# ---------------------------------
# # Another example
# condition = True
# if condition:
#     print("This is printed every time.")

# ---------------------------------
# # Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is. Please have a look at the examples of expected behaviour below.
# num = int(input("Please give any number: "))
# if num < 0:
#     print(num * -1)
# if num > 0:
#     print(num)

# ---------------------------------
# # Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.
# num = int(input("enter any number: "))
# if num < 100:
#     print("number is less than 100")
# if num < 1000:
#     print("number is less than 1000")
# if num < 100000:
#     print("number is less than 10000")

# ---------------------------------
# # Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# operation = input("Choose operation (add, subtract, multipy, divide): ")

# if operation == "add":
#     print(num1 + num2)
# if operation == "subtract":
#     print(num1 - num2)
# if operation == "multiply":
#     print(num1 * num2)
# if operation == "divide":
#     print(num1 / num2)

# In the Python math module there is the function sqrt, which calculates the square root of a number. You can use it like so:

# from math import sqrt

# print(sqrt(25))
