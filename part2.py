# # # ====================== Part 2 =========================

# # Statement
# # A statement is a part of the program which executes something. It often, but not always, refers to a single command.
# name = "Anna"
# if name == "Anna":
#     print("Hi!")
#     number = 2
# # In the above case there are two statements (a print statement and an assignment statement) within a conditional statement.

# ---------------------------------
# # # Block
# name = "ali"
# if name == "ali":
#     # begining of conditional block
#     print("hello ali")
#     print(2 + 6)
#     # end of conditional block

# print("This is from new block start")

# ---------------------------------
# # Expression
# An expression is a bit of code that results in a determined data type. When the program is executed, the expression is evaluated so that it has a value that can then be used in the program.

# the variable x is assigned the value of the expression 1 + 2
# x = 1 + 2

# the variable y is assigned the value of the expression '3 times x plus x squared'
# y = 3 * x + x**2

# ---------------------------------
# # Function

# print and input are function and we call them below to us it further in our code
# print("Hello")
# input("enter name")

# ---------------------------------
# # # Data type
# name = "ali"
# age = 29

# print(type(name))
# print(type(age))


# ---------------------------------
# # Syntax
# Similarly to natural languages, the syntax of a programming language determines how the code of a program should be written. Each programming language has its own specific syntax.

# ---------------------------------
# # Debugging
# If the syntax of the program is correct but the program still doesn't function as intended, there is a bug in the program.

# Bugs manifest in different ways. Some bugs cause an error during execution. For example, the following program

# x = 10
# y = 0
# result = x / y

# print(f"{x} divided by {y} is {result}")

# The problem here is mathematical in nature: division by zero is not allowed, and this halts the execution of the program.

# ---------------------------------
# number = input("Please type in a number: ")
# if number > 100:
#     print("The number was greater than one hundred")
#     number - 100
#     print("Now its value has decreased by one hundred")
#     print("Its value is now" + number)
#     print(number + " must be my lucky number!")
#     print("Have a nice day!")


# word = "Hello!"
# print(len(word))

# myWord = input("Please enter any word: ")
# print(f"There are {len(myWord)} letters in your word.")

# ---------------------------------
# # # Typecasting
# temprature = float(input("Enter temprature: "))
# print(f"Today's temprature is {int(temprature)}.")

# ---------------------------------
# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.
# num = float(input("Enter a floating number: "))
# print(int(num))
# print(float(num - int(num)))
# print(1.23 - 1)

# ---------------------------------
# # # Branching in conditional statement
# num = int(input("Enter any number: "))
# if num < 0:
#     print("Number is less than 0")
# elif num == 0:
#     print("Number is equal to 0")
# else:
#     print("Number is greater than 0")

# ---------------------------------
# Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print(f"first number {num1} is greater than second number {num2}.")
# elif num2 > num1:
#     print(f"first number {num2} is greater than second number {num1}.")
# elif num1 == num2:
#     print(f"first number {num2} is equal to second number {num1}.")
# else:
#     print("Given numbers are not valid!")

# ---------------------------------
# Python comparison operators can also be used on strings. String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if

# the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
# only the standard English alphabet of a to z, or A to Z, is used.
# Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

# You can assume all words will be typed in lowercase entirely.
# word1 = str(input("Enter any word: "))
# word2 = str(input("Enter any word: "))

# if word1 < word2:
#     print(f"{word2} is comes alphabetically last.")
# elif word2 > word1:
#     print(f"{word1} is comes alphabetically last.")
# elif word1 == word2:
#     print(f"{word2} and {word1} are same words.")
# else:
#     print("Given words are not valid!")

# ---------------------------------
# # Even and odd number finder
# num = int(input("Please enter number: "))

# if num % 2 == 0:
#     print("Given number is even!")
# else:
#     print("Given number is odd!")

# ---------------------------------
# # Logical operators
# Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

# In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

# username = input("Enter your name: ")
# if username == "Huey" or username == "Dewey" or username == "Louie":
#     print("I think you might be one of Donald's nephews.")
# elif username == "Morty" or username == "Ferdie":
#     print("I think you might be one of Mickey's nephews.")
# else:
#     print("I don't remember you!")

# # Not operator
# elder = True
# newElder = not elder

# print(elder)
# print(newElder)

# ----------------------------------
# # Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.
# num = int(input("Enter number: "))
# if num % 5 == 0 and num % 3 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print("Not sure!")

# ----------------------------------
# # # Nested conditionals

# # Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

# # Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Yes it's a leap year!")
#         else:
#             print("No it is not a leap year!")
#     else:
#         print("Yes it's a leap year!")
# else:
#     print("No it is not a leap year!")

# ----------------------------------------
# # # Simple loops
# while True:
#     num = int(input("Please type any number, or -1 to quit. "))

#     if num == -1:
#         break
#     print(num**2)

# print("This is from outside the loop!")

# while Tr

# ---------------------------------
# # This program should print out a countdown. The code is as follows:
# countdown = 10
# while True:

#     if countdown < 0:
#         break
#     else:
#         print(countdown)
#         countdown -= 1
# print("countdown stopped!")

# ----------------------------------
# # # Loops and helper variables
# # Let's make the PIN checking example a bit more realistic. This version gives the user only three attempts at typing in a PIN.

# # The program uses two helper variables. The variable attempts keeps track of how many times the user has typed in a PIN. The variable success is set to either True or False based on whether the user is successful in signing in.
# attempt = 0

# while True:
#     pin = int(input("Please enter your five digit pin: "))
#     attempt = attempt + 1

#     if pin == 12345:
#         success = True
#         break

#     if attempt >= 3:
#         success = False
#         break

#     print("Your pin is incorrect try again!")

# if success:
#     print("Your pin is correct!")
# else:
#     print("Too many attempts!")

# ----------------------------------------------
# # Please write a program which asks the user for a year, and prints out the next leap year.

# year = int(input("Enter a year: "))

# while True:
#     year += 1
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(year)
#                 break
#         else:
#             print(year)
#             break
# -------------------------------------------
# # # Concatenating strings with the + operator

# # Please write a program which keeps asking the user for words. If the user types in end or types in the same word twice in a row, the program should print out the story the words formed, and finish.
# story = ""
# prevWord = ""
# while True:
#     word = input("Enter your word here: ")

#     if word == "end":
#         print(story)
#         break
#     elif word == prevWord:
#         print(story)
#         break
#     else:
#         story = story + " " + word

#     prevWord = word

# ---------------------------------------
# # Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.
# # After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.
# # The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.
# # The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation.
# # The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.

# numbers = 0
# count = 0
# sum = 0
# pnum = 0
# nnum = 0

# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break

#     if number > 0:
#         pnum += 1
#     if number < 0:
#         nnum += 1

#     count += 1
#     sum = sum + number


# print(f"Count: {count}")
# print(f"Sum: {sum}")
# print(f"Mean: {int(sum/count)}")
# print(f"Positive number count: {pnum}")
# print(f"Negative number count: {nnum}")
# print(f"Mean: {int(sum/count)}")
