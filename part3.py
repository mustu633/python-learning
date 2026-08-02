# # # ====================== Part 3 =========================

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

# --------------------------------------------------
# # Functions


# def message():
#     print("Hello")


# message()

# # Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))


# def mean(a, b, c):
#     print((a + b + c) / 3)


# mean(num1, num2, num3)

# # Please write a function named print_many_times(text, times), which takes a string and an integer as arguments. The integer argument specifies how many times the string argument should be printed out:

# typed_text = str(input("Please type something: "))
# reptition_times = int(input("Repitition times: "))


# def print_many_times(text, times):
#     i = 1
#     while i <= times:
#         print(text)
#         i += 1


# print_many_times(typed_text, reptition_times)

# # Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.
# user_num = int(input("Please enter a number: "))


# def hash_square(num):
#     i = 1
#     while i <= num:
#         print("#" * num)
#         i += 1


# hash_square(user_num)

# # Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board.

# user_num = int(input("Enter number: "))


# def chessboard(num):
#     val = 1
#     row = ""
#     row_rev = ""
#     i = 1
#     while True:
#         row = row + str(val)
#         if val == 0:
#             val = 1
#         elif val == 1:
#             val = 0
#         row_rev = row_rev + str(val)

#         if len(row) == user_num:
#             break

#     printed_row = row
#     while i <= user_num:
#         print(printed_row)
#         if printed_row == row:
#             printed_row = row_rev
#         elif printed_row == row_rev:
#             printed_row = row
#         i += 1


# chessboard(user_num)
