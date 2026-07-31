# ================ Part 1 ===================

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

# ================ Part 2 ===================
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

# ----------------------------------------------
# # # Loops with conditions
# num = int(input("Enter the number: "))

# while num < 5:
#     print(num)
#     num += 1

# # Please write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

# num = 2 + 2

# while num < 30:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# # Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.
# num = int(input("Enter your number: ")) - 1

# while num > 0:
#     print(num)
#     num -= 1

# # Please write a program which asks the user to type in an upper limit. The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. That is, the program prints out powers of two in order.
# # The execution of the program finishes when the next number to be printed would be greater than the limit set by the user. No numbers greater than the limit should be printed.

# upperlimit = int(input("Please enter an upper limit number: "))
# num = 1

# while num <= upperlimit:
#     print(num)
#     num = num * 2

# # Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user.
# # Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:

# sum = 0
# count = 1
# consum = str(count)
# limitnum = int(input("Please enter a limit number: "))

# while sum < limitnum:
#     sum += count
#     count += 1
#     if sum <= limitnum - 1:
#         consum += " + " + str(count)


# print(consum + " = " + str(sum))

# --------------------------------------------
# # # Working with strings
# # String operations

# word = "Nice"

# print(word + word)
# print(word * 5)

# # -----
# n = 10 # number of layers in the pyramid
# row = "*"

# while n > 0:
#     print(" " * n + row)
#     row += "**"
#     n -= 1

# -------------------------------
# # # The length and index of a string

# print(len("mustafa"))
# print(("mustafa")[3])
# print(("mustafa")[0])

# # Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".
# str1 = str(input("Please enter your first string: "))
# str2 = str(input("Please enter your second string: "))

# if len(str1) > len(str2):
#     print(f"{str1} is longer!")
# elif len(str2) > len(str1):
#     print(f"{str2} is longer!")
# elif len(str1) == len(str2):
#     print(f"{str1} and {str2} are equally long!")
# else:
#     print("Not sure!")

# # Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.
# str1 = str(input("Please enter your string: "))
# indx = len(str1) - 1
# while indx >= 0:
#     print(str1[indx])
#     indx -= 1

# # Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.
# str1 = str(input("Please enter your string: "))

# if str1[1] == str1[len(str1) - 2]:
#     print("YES, second and second last characters in your string are same!")
# else:
#     print("NO, second and second last characters in your string are same!")

# # Please write a program which prints out a rectangle of hash characters accordingly, the width and height of which is chosen by the user.

# width = int(input("Please enter the width: "))
# height = int(input("Please enter the height: "))
# count = 1

# while count <= height:
#     print("#" * int(width))
#     count += 1

# # Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.
# word = str(input("Please type something: "))

# while len(word) != 0:
#     print(word)
#     print("-" * len(word))
#     word = input("Please type something: ")

# # Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.
# userstr = str(input("Please enter your string: "))

# print("*" * int(20 - len(userstr)) + userstr)

# # Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.
# # If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.
# userstr = str(input("Please type your string: "))

# print("*" * 30)
# if int(len(userstr) % 2) == 0:
#     print(
#         "*"
#         + " " * int(int(28 - len(userstr)) / 2)
#         + userstr
#         + " " * int(int(28 - len(userstr)) / 2)
#         + "*"
#     )
# else:
#     print(
#         "*"
#         + " " * int(int(28 - len(userstr)) / 2)
#         + userstr
#         + " " * int(int(29 - len(userstr)) / 2)
#         + "*"
#     )
# print("*" * 30)

# -------------------------------------------------------
# # # Substrings and slices
# input_string = "presumptious"

# print(input_string[0:3])
# print(input_string[4:10])

# # if the beginning index is left out, it defaults to 0
# print(input_string[:3])

# # if the end index is left out, it defaults to the length of the string
# print(input_string[4:])

# # Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest.
# userstr = str(input("Please enter your string: "))
# count = 1
# while count <= len(userstr):
#     print(userstr[0:count])
#     count += 1

# # Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest.
# userstr = str(input("Please enter your string: "))
# count = len(userstr) - 1
# while count >= 0:
#     print(userstr[count : int(len(userstr))])
#     count -= 1

# -------------------------------------------------------
# # # Searching for substrings
# input_string = "test"

# print("t" in input_string)
# print("x" in input_string)
# print("es" in input_string)
# print("ets" in input_string)

# # Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.You may assume the input will be in lowercase entirely.
# inputstr = str(input("Enter your string: "))
# if "a" in inputstr:
#     print("a found in this string!")
# else:
#     print("a not found in this string!")
# if "e" in inputstr:
#     print("e found in this string!")
# else:
#     print("e not found in this string!")
# if "o" in inputstr:
#     print("o found in this string!")
# else:
#     print("o not found in this string!")

# # Please write a program which asks the user to type in a string and a single character. The program then prints all slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.
# userstr = str(input("Enter your string: "))
# userchr = str(input("Enter your character: "))
# count = 0
# while count <= int(len(userstr) - 3):
#     if str(userstr[count]) == userchr:
#         print(userstr[count : count + 3])
#     count += 1

# # Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.
# userStr = str(input("Please enter your string: "))
# userSubStr = str(input("Please enter your sub string: "))
# count = 0
# found = 0
# while count <= int(len(userStr) - len(userSubStr)):
#     if userSubStr == userStr[count : count + len(userSubStr)]:
#         found += 1
#     if found > 1:
#         print(f"The second occurrence of the substring is at index {count}.")
#         break
#     count += 1
# if found <= 1:
#     print("The substring does not occur twice in the string.")

# ------------------------------------------------------------
# # break and continued command

# sum = 0

# while True:
#     number = int(input("Please type in a number, -1 to exit: "))
#     if number == -1:
#         break
#     if number >= 10:
#         continue
#     sum += number

# print(f"The sum is {sum}")

# ------------------------------------------
# # # Nested loops
# # Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user.
# userNum = int(input("Please enter your +ve integer number: "))
# i = 1
# j = 1
# while i <= userNum:
#     while j <= userNum:
#         print(f"{i} X {j} = {i*j}")
#         j += 1
#     j = 1
#     i += 1

# # Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.
# sentence = str(input("Please enter your sentence: "))
# i = 0
# while i < len(sentence) - 1:
#     if i == 0:
#         print(sentence[0])
#     if sentence[i] == " ":
#         print(sentence[i + 1])
#     i += 1

# # Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.
# userNum = int(input("Please enter your number for factorial: "))
# factorial = 1
# i = 1
# j = 1
# while userNum <= 0:
#     while j <= userNum:
#         factorial = 5
#     print(factorial)
#     i += 1
#     userNum = int(input("Please enter your number for factorial: "))

# if userNum <= 0:
#     print("END!")

# # Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth.
# num = int(input("Please type in a number: "))

# i = 1

# while True:
#     if i > num:
#         break

#     if i + 1 <= num:
#         print(i + 1)
#         print(i)
#     else:
#         print(i)

#     i += 2
#     continue
#     print("hello")

# # # Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range
# num = int(input("Please type in a number: "))

# start = 1
# end = num

# while True:
#     if start > end:
#         break

#     print(start)

#     if start == end:
#         break

#     print(end)

#     start += 1
#     end -= 1
#     continue
#     print("hello")
