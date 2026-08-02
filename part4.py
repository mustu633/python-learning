# # # ====================== Part 4 =========================

# # # The parameters and arguments of a function

# # Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.
# user_int = int(input("Enter a number: "))
# user_str = str(input("Enter a string: "))


# # This line named function  will also be useful for some more problems below :
# def line(num, text):
#     if len(text) > 0:
#         print(text[0] * num)
#     else:
#         print("*" * num)


# line(user_int, user_str)

# -------------------------------------------------
# # # Function calls within function calls

# # Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.
# # The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.

# inp_height = int(input("Enter height of reactangle: "))


# def box_of_hashes(height):
#     i = 1
#     while i <= height:
#         line(10, "#")
#         i += 1


# box_of_hashes(inp_height)

# # Please write a function named square_of_hashes, which draws a square of hash characters. The function takes one argument, which determines the length of the side of the square.
# # The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# inp_length = int(input("Please give lenght: "))


# def square_of_hashes(length):
#     i = 1
#     while i <= length:
#         line(length, "#")
#         i += 1


# square_of_hashes(inp_length)


# # Please write a function named square, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.
# # The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# user_length = int(input("Please enter length: "))
# user_char = str(input("Please enter a character: "))


# def square(length, char):
#     i = 1
#     while i <= length:
#         line(length, char)
#         i += 1


# square(user_length, user_char)

# # Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.
# # The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# user_length = int(input("Please enter triangle length: "))


# def triangle(length):
#     i = 1
#     while i <= length:
#         line(i, "#")
#         i += 1


# triangle(user_length)

# # Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.
# # The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

# inp_tri_length = int(input("Please enter height of triangle: "))
# inp_tri_char = str(input("Please enter char of triangle: "))
# inp_rect_width = int(input("Please enter width of rectangle: "))
# inp_rect_char = str(input("Please enter char of rectangle: "))


# def shape(inp1, inp2, inp3, inp4):
#     i = 0
#     while i <= inp1:
#         line(i, inp2)
#         i += 1
#     j = 0
#     while j <= inp3:
#         line(inp1, inp4)
#         j += 1


# shape(inp_tri_length, inp_tri_char, inp_rect_width, inp_rect_char)

# # Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
# inp_num = int(input("Please enter a number: "))


# def spruce(num):
#     i = 1
#     char = "*"
#     space = num
#     while i <= num + 1:
#         print(" " * space + char)
#         char = char + "**"
#         space -= 1
#         i += 1
#     print(" " * num + "*" + " " * num)


# spruce(inp_num)


# ----------------------------------------------
# # # The return value of a function
# def my_sum(a, b):
#     return a + b


# result = my_sum(2, 3)

# print("Sum:", result)

# # Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.
# inp1 = int(input("Please enter first value: "))
# inp2 = int(input("Please enter second value: "))
# inp3 = int(input("Please enter third value: "))


# def greatest_number(num1, num2, num3):
#     num = num1
#     if num < num2:
#         num = num2

#     if num < num3:
#         num = num3
#     return num


# result = greatest_number(inp1, inp2, inp3)
# print(result)

# # Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

# inp_str = str(input("Please write string: "))
# inp_num_1 = int(input("Please write first num: "))
# inp_num_2 = int(input("Please write second num: "))


# def same_chars(string, num1, num2):
#     if num1 >= len(string) or num2 >= len(string):
#         return False
#     elif string[num1] == string[num2]:
#         return True
#     else:
#         return False


# result = same_chars(inp_str, inp_num_1, inp_num_2)
# print(result)

# # Please write three functions: first_word, second_word and last_word. Each function takes a string argument.
# # As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.
# # In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

# inp_sentence = str(input("Please enter your sentence: "))


# def first_word(sentence):
#     if len(sentence) > 0:
#         i = 0
#         result = ""
#         while i < len(sentence):
#             if sentence[i] == " ":
#                 return result
#             result = result + sentence[i]
#             i += 1
#         return result


# def second_word(sentence):
#     i = 0
#     while i < len(sentence):
#         if sentence[i] == " ":
#             i += 1
#             result = ""
#             j = int(i)
#             while j < len(sentence):
#                 if sentence[j] == " ":
#                     return result
#                 result = result + sentence[j]
#                 j += 1
#             return result

#         i += 1


# def third_word(sentence):
#     i = 0
#     num = 0
#     while i < len(sentence):
#         if sentence[i] == " ":
#             num += 1
#             if num >= 2:
#                 i += 1
#                 result = ""
#                 j = int(i)
#                 while j < len(sentence):
#                     if sentence[j] == " ":
#                         return result
#                     result = result + sentence[j]
#                     j += 1
#                 return result
#         i += 1


# def last_word(sentence):
#     if len(sentence) > 0:
#         i = len(sentence) - 1
#         result = ""
#         while i >= 0:
#             if sentence[i] == " ":
#                 return result
#             result = sentence[i] + result
#             i -= 1
#         return result


# first = first_word(inp_sentence)
# second = second_word(inp_sentence)
# third = third_word(inp_sentence)
# last = last_word(inp_sentence)

# print(first)
# print(second)
# print(third)
# print(last)


# --------------------------
# # # Type Hints
# def print_many_times(message: str, times: int):
#     while times > 0:
#         print(message)
#         times -= 1


# print_many_times("ali", 2)
# print_many_times("ali", "ali")

# # # Similarly, the return value of a function can be hinted at in the function definition:

# def ask_for_name() -> str:
#     name = input("Mikä on nimesi? ")
#     return name

# # # note**:  Type hinting is literally just hinting about the type of the argument or the return value. It is not a guarantee of type, and definitely not a safeguard against type errors. If a function receives an argument or returns a value of the wrong type, the function is still executed, but it might not work correctly.

# -------------------------------------------------------
# # # Lists

# # Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.

# my_list = [1, 2, 3, 4, 5]

# while True:
#     indx = int(input("Please enter index value: "))
#     new_val = int(input("Please enter index value: "))

#     if indx == -1:
#         break
#     my_list[indx] = new_val
#     print(my_list)

# # ---------------------
# # # List methods
# append(item) use to add item in last of list
# insert(index,item) use to add item at specific index in list all other items already in list align respectively
# pop(index) remove the item from list using index and return the item
# remove(item) remove the first matched item from list
# sort() it sort the items in list from smallest to highest mean in acending order

# # Add item at specific location:  .insert() method used to add item at specific index
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.insert(0, 10)
# print(numbers)
# numbers.insert(2, 20)
# print(numbers)


# # Removing items from a list :
# # .pop() method take index and remove the value from that index it also return that value
# # #  .remove() method take actual value and remove the first matched value from the list
# my_list = [1, 2, 1, 2, 7, 8, 5]

# my_list.remove(1)
# print(my_list)
# my_list.remove(1)
# print(my_list)
# my_list.pop(3)
# print(my_list)


# # Please write a program which asks the user to choose between addition and removal. Depending on the choice, the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
# # The list is printed out in the beginning and after each operation.

# final_list = []
# i = 1
# operation = ""

# print(f"The list is now: {final_list}")
# while True:
#     operation = input("Please enter operation add(d) remove(r) exit(x): ")
#     if operation == "x":
#         print("Bye!")
#         break
#     elif operation == "d":
#         final_list.append(i)
#     elif operation == "r":
#         final_list.pop(len(final_list) - 1)
#     else:
#         print("Not a valid operation!")

#     print(f"The list is now: {final_list}")

# # Please write a program which asks the user for words. If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
# my_list = []
# word = ""
# same = False

# while True:
#     word = str(input("Please enter your word: "))
#     i = 0
#     while i < len(my_list):
#         if word == my_list[i]:
#             same = True
#             break
#         i += 1
#     if same == True:
#         print(f"No. of different words typed in: {len(my_list)}")
#         break
#     my_list.append(word)

# # Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:
# # in the order the items were added
# # ordered from smallest to greatest
# # The program exits when the user types in 0.

# # # Solution of this problem using .sort() method:
# actual_list = []
# ordered_list = []
# while True:
#     new_item = int(input("Please give new item: "))

#     if new_item == 0:
#         break

#     actual_list.append(new_item)
#     ordered_list.append(new_item)
#     ordered_list.sort()
#     print(f"The list now: {actual_list}")
#     print(f"The list in order: {ordered_list}")

# # Solution of this problem by manual sorting:
# my_list = []
# ordered_list = []
# while True:
#     new_item = int(input("Please give new item: "))

#     if new_item == 0:
#         break

#     my_list.append(new_item)
#     if len(ordered_list) > 0:
#         i = 0
#         insert = False
#         while i < len(ordered_list):
#             if new_item <= ordered_list[i]:
#                 ordered_list.insert(i, new_item)
#                 insert = True
#                 break
#             i += 1

#         if insert != True:
#             ordered_list.append(new_item)
#     else:
#         ordered_list.append(new_item)
#     print(f"The list now: {my_list}")
#     print(f"The list in order: {ordered_list}")

# ------------------------------------------------------
# # # # List functions
# # max(inp_list) is used to get greatest item from the inp_list
# # min(inp_list) is used to get smallest item from the inp_list
# # sum(inp_list) is used to get sum of all items in the inp_list


# my_list = [5, 2, 3, 1, 4]

# greatest = max(my_list)
# smallest = min(my_list)
# list_sum = sum(my_list)

# print("Smallest:", smallest)
# print("Greatest:", greatest)
# print("Sum:", list_sum)


# ========= methods vs function ============
# method is used using means using dot (.) eg: .method_name(input_value)
# function is called and give some value, some times function also take list as an input eg: max(inp_list) it give the greatest item from inp_list
# ==========================================


# # A list as an argument or a return value
# def median(my_list: list):
#     ordered = sorted(my_list)
#     list_centre = len(ordered) // 2
#     return ordered[list_centre]

# shoe_sizes = [45, 44, 36, 39, 40]
# print("The median of the shoe sizes is", median(shoe_sizes))

# ages = [1, 56, 34, 22, 5, 77, 5]
# print("The median of the ages is", median(ages))

# -------------------------------------------------
# # Please write a function named length which takes a list as its argument and returns the length of the list.


# def length(my_list:list):
#     return len(my_list)


# my_list = [1, 2, 3, 4, 5]
# result = length(my_list)
# print("The length is", result)

# result = length([1, 1, 1, 1])
# print("The length is", result)


# # Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.
# def mean(my_list: list):
#     my_list.sort()
#     return my_list[int((len(my_list) - 1) / 2)]


# my_list = [1, 2, 3, 4, 5]
# result = mean(my_list)
# print("mean value is", result)


# # Please write a function named range_of_list, which takes a list of integers as an argument. The function returns the difference between the smallest and the largest value in the list.


# def range_of_list(my_list: list):
#     return max(my_list) - min(my_list)


# my_list = [1, 2, 3, 4, 5]
# result = range_of_list(my_list)
# print("The range of the list is", result)

# ----------------------------------------------------
# # Definite iteration
