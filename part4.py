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
# # # Definite iteration

# # # The for loop
# my_list = [3, 2, 4, 5, 2]

# for item in my_list:
#     print(item)

# --------------------------------------
# # # for loop for string
# name = "Muhammad"

# for character in name:
#     print(character)

# # -------------------------------------
# # Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.

# inp_string = str(input("Please give your string: "))

# for character in inp_string:
#     print(character)
#     print("*")

# ----------------------------------------
# # The function range
# # range(5) means from 0 to 5  (note: 5 is excluded b/c indx start from 0).   range(3,7) means from 3 to 7 (note: 7 is excluded b/c indx start from 0).
# # range(1, 9, 2) last value is iteration means + 2, if range(9, 1, -1) it will change value -1 means give values in reverse order

# for i in range(5):
#     print(i)

# # --------------------------------------------
# # Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line.
# inp_num = int(input("Please enter a positive integer number: "))

# for num in range(-inp_num, inp_num + 1, 1):
#     if num == 0:
#         continue
#     print(num)

# # --------------------------------------
# # From a range to a list

# numbers = list(range(2, 7))
# print(numbers)


# # Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.


# def list_of_stars(int_list: list):
#     for num in int_list:
#         print("*" * int(num))


# list_of_stars([3, 7, 1, 1, 2])


# # Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.
# def anagrams(string1: str, string2: str):
#     sorted1 = sorted(string1)
#     sorted2 = sorted(string2)

#     if sorted1 == sorted2:
#         return True
#     else:
#         return False


# print(anagrams("tame", "meta"))  # True
# print(anagrams("tame", "mate"))  # True
# print(anagrams("tame", "team"))  # True
# print(anagrams("tabby", "batty"))  # False
# print(anagrams("python", "java"))  # False


# # Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.
# # Please also write a main program which asks the user to type in words until they type in a palindrome:


# def palindromes(my_string: str):
#     rev_string = ""
#     for i in range(len(my_string) - 1, -1, -1):
#         rev_string = rev_string + my_string[i]
#     if my_string == rev_string:
#         return True
#     else:
#         return False


# while True:
#     result = bool()

#     inp_string = str(input("Please type in a palindrome: "))
#     result = palindromes(inp_string)

#     if result == True:
#         print(f"{inp_string} is a palindrome")
#         break
#     elif result == False:
#         print("that wasn't a palindrome")


# # Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.


# def sum_of_positives(my_list: list):
#     sum = 0
#     for i in my_list:
#         if i > 0:
#             sum = sum + i
#     return sum


# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)

# # Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.


# def even_numbers(my_list: list):
#     even_list = []
#     for i in my_list:
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list


# my_list = [1, 2, 3, 4, 5]
# new_list = even_numbers(my_list)
# print("original", my_list)
# print("new", new_list)

# # Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items.


# def list_sum(my_list1: list, my_list2: list):
#     new_list = []
#     for i in range(0, len(my_list1)):
#         new_list.append(my_list1[i] + my_list2[i])
#     return new_list


# a = [1, 2, 3]
# b = [7, 8, 9]
# print(list_sum(a, b))  # [8, 10, 12]


# # Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
# def distinct_numbers(my_list: list):
#     new_list = []
#     for i in my_list:
#         if new_list.__contains__(i):
#             continue
#         else:
#             new_list.append(i)
#     new_list.sort()
#     return new_list


# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list))  # [1, 2, 3]

# -----------------------------------------------------------------
# Finding the best or the worst item in a list


# # Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.


# def length_of_longest(my_list: list):
#     if len(my_list) == 0:
#         return None
#     output = 0
#     for item in my_list:
#         if len(item) > output:
#             output = len(item)

#     return output


# my_list = ["first", "second", "fourth", "eleventh"]

# result = length_of_longest(my_list)
# print(result)
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = length_of_longest(my_list)
# print(result)

# my_list = []

# result = length_of_longest(my_list)
# print(result)

# # Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.


# def shortest(my_list: list):
#     if len(my_list) == 0:
#         return None

#     output = my_list[0]
#     for item in my_list:
#         if len(output) > len(item):
#             output = item
#     return output


# my_list = ["first", "second", "fourth", "eleventh"]

# result = shortest(my_list)
# print(result)

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = shortest(my_list)
# print(result)

# my_list = []

# result = shortest(my_list)
# print(result)


# # Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new list containing the longest string in the original list. If more than one are equally long, the function should return all of the longest strings.
# # The order of the strings in the returned list should be the same as in the original.


# def all_the_longest(my_list: list):
#     longest_length = 0

#     for item in my_list:
#         if longest_length < len(item):
#             longest_length = len(item)

#     new_list = []
#     for item in my_list:
#         if len(item) == longest_length:
#             new_list.append(item)

#     return new_list


# my_list = ["first", "second", "fourth", "eleventh"]

# result = all_the_longest(my_list)
# print(result)  # ['eleventh']

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = all_the_longest(my_list)
# print(result)  # ['dorothy', 'richard']

# -----------------------------------------------------
# # # Print statement formatting

# name = "Mark"
# age = 37

# # The first is the + operator for strings. It allows simple concatenation of string segments:
# print("Hi " + name + " your age is " + str(age) + " years")

# # The second method is considering each segment of the argument as a separate argument, and splitting them up with commas:
# print("Hi", name, "your age is", age, "years")

# # If need to remove the automatically added spaces, you can add a special named argument sep:
# print("Hi", name, "your age is", age, "years", sep="")
# print("Hi", name, "your age is", age, "years", sep="\n")
# print("Hi", name, "your age is", age, "years", sep=" #***# ")

# # ***note: By default print command always starts from a new line
# print("ali")
# print("Muhammad")
# # The keyword argument end specifies what is put at the end of a line.
# print("adil", end=" *** ")
# print("Muhammad")

# # The third method to prepare strings is f-strings.
# print(f"Hi {name} your age is {age} years")

# # The format specifier .2f states that we want to display 2 decimals.
# number = 1 / 3
# print(f"The number is {number:.2f}")

# # Here's another example, where we specify the amount of whitespace reserved for the variable in the printout. Both times the variable name is included in the resulting string, it has a space of 15 characters reserved. First the names are justified to the left, and then they are justified to the right:
# names = ["Steve", "Jean", "Katherine", "Paul"]
# for name in names:
#     print(f"{name:15} centre {name:>15}")

# # --------------------------------------------------------------------
# # Please write a function named formatted, which takes a list of floating point numbers as its argument. The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points. The order of the items in the list should remain unchanged.


# def formatted(my_list: list):
#     new_list = []
#     for item in my_list:
#         new_list.append(f"{item: .2f}")

#     return new_list


# my_list = [1.234, 0.3333, 0.11111, 3.446]
# new_list = formatted(my_list)
# print(new_list)


# # -----------------------------------------------------
# # # More strings and lists

# # List slicing
# my_list = [3, 4, 2, 4, 6, 1, 2, 4, 2]
# print(my_list[3:7])

# # In fact, the [] syntax works very similarly to the range function, which means we can also give it a step:
# my_string = "exemplary"
# print(my_string[0:7:2])

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(my_list[6:2:-1])

# # If we omit either of the indexes, the operator defaults to including everything. Among other things, this allows us to write a very short program to reverse a string:
# my_string = input("Please type in a string: ")
# print(my_string[::-1])

# # Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.


# def everything_reversed(my_list: list):
#     new_list = []
#     for item in my_list:
#         new_list.append(item[::-1])
#     return new_list[::-1]


# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)

# ---------------------------------------------
# # Strings are immutable
# my_string = "exemplary"
# my_string[0] = "a"

# # Strings themselves are immutable, but the variables holding them are not. A string can be replaced by another string.
# my_list = [1, 2, 3]
# my_list[0] = 10

# my_string = "Hey"
# my_string = my_string + "!"

# ----------------------------------------------
# # # More methods for lists and strings
# # .count(item) it return the total number of item in list or string
# my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
# print(my_string.count("ch"))

# my_list = [1, 2, 3, 1, 4, 5, 1, 6]
# print(my_list.count(1))

# # .replace(item,new_item) It replace all items similar to the given item with new_item in string
# my_string = "Python is fun, Use python"

# # Replaces the substring and stores the result in the same variable
# my_string = my_string.replace("Python", "Java")
# print(my_string)


# # Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.


# def most_common_character(my_string: str):
#     if len(my_string) == 0:
#         return None

#     result = my_string[0]
#     for char in my_string:
#         if my_string.count(result) < my_string.count(char):
#             result = char
#     return result


# first_string = "abcdbde"
# print(most_common_character(first_string))

# second_string = "exemplaryelementary"
# print(most_common_character(second_string))


# # Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.
# # You can assume the string will contain only characters from the lowercase English alphabet a...z.


# def no_vowels(my_string: str):
#     vowels = ["a", "e", "i", "o", "u"]
#     new_string = ""
#     for char in my_string:
#         if vowels.count(char) == 0:
#             new_string = new_string + char
#     return new_string


# inp_string = "this is an example"
# result = no_vowels(inp_string)
# print(result)

# # ---------------------------------------------------
# # The Python string method isupper() returns True if a string consists of only uppercase characters.
# print("XYZ".isupper())

# is_it_upper = "Abc".isupper()
# print(is_it_upper)


# # Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.


# def no_shouting(my_list: list):
#     new_list = []
#     for item in my_list:
#         if item.isupper() == False:
#             new_list.append(item)
#     return new_list


# my_list = [
#     "ABC",
#     "def",
#     "UPPER",
#     "ANOTHERUPPER",
#     "lower",
#     "another lower",
#     "Capitalized",
# ]
# pruned_list = no_shouting(my_list)
# print(pruned_list)

# --------------------------------------------------------
# # Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neghbours, and so would items 56 and 55.
# # Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.
# # For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

# def longest_series_of_neighbours(my_list:list):
# --------------------------------------------------------

# # # Long problem (Project):

# # In this exercise you will write a program for printing out grade statistics for a university course.
# # The program asks the user for results from different students on the course. These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.
# # Exam points are integers between 0 and 20. The number of exercises completed is an integer between 0 and 100.
# # The program keeps asking for input until the user types in an empty line. You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

# results = []

# while True:
#     std_result = input("Exam points and exercises completed: ")

#     if std_result == "":
#         break

#     std_result = std_result.split()
#     std_result[0] = int(std_result[0])
#     std_result[1] = int(std_result[1])
#     results.append(std_result)

# total_students = len(results)
# final_points = 0
# grade_0 = 0
# grade_1 = 0
# grade_2 = 0
# grade_3 = 0
# grade_4 = 0
# grade_5 = 0

# for student in results:
#     exam_points = student[0]
#     exercises = student[1]
#     exercise_points = exercises // 10
#     total_points = exercise_points + exam_points
#     final_points = final_points + total_points
#     if exam_points < 10:
#         grade = 0
#         grade_0 = grade_0 + 1
#     else:
#         if total_points >= 0 and total_points <= 14:
#             grade_0 = grade_0 + 1
#         elif total_points >= 15 and total_points <= 17:
#             grade_1 = grade_1 + 1
#         elif total_points >= 18 and total_points <= 20:
#             grade_2 = grade_2 + 1
#         elif total_points >= 21 and total_points <= 23:
#             grade_3 = grade_3 + 1
#         elif total_points >= 24 and total_points <= 27:
#             grade_4 = grade_4 + 1
#         elif total_points >= 28 and total_points <= 30:
#             grade_5 = grade_5 + 1

# point_average = final_points / total_students
# pass_students = total_students - grade_0
# pass_percentage = pass_students / total_students * 100

# print("Statistics: ")
# print(f"Point average: {point_average:.1f}")
# print(f"Pass percentage: {pass_percentage}")
# print(f"Grade distribution: ")
# print("5:" + "*" * grade_5)
# print("4:" + "*" * grade_4)
# print("3:" + "*" * grade_3)
# print("2:" + "*" * grade_2)
# print("1:" + "*" * grade_1)
# print("0:" + "*" * grade_0)
