# # # ====================== Part 5 =========================

# # # Lists with different types of data

# names = ["ali", "ahmad", "asif", "adil"]
# measurments = [12.4, 56.7, 77.778, 45.6]
# random_numbers = [1, 4, 2, 3, 5, 67, 7]
# persons = [["Betty", 10, 1.37], ["Peter", 7, 1.25], ["Emily", 32, 1.64], ["Alan", 39, 1.78]]


# # Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.
# def longest(strings: list):
#     result = ""
#     for item in strings:
#         if len(item) > len(result):
#             result = item

#     return result


# inp_strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
# print(longest(inp_strings))

# -----------------------------------------
# # # Lists within lists

# my_list = [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
# print(my_list)
# print(my_list[1])
# print(my_list[1][0])

# persons = [
#     ["Betty", 10, 1.37],
#     ["Peter", 7, 1.25],
#     ["Emily", 32, 1.64],
#     ["Alan", 39, 1.78],
# ]

# for person in persons:
#     name = person[0]
#     age = person[1]
#     height = person[2]
#     print(f"{name}: age {age} years, height {height} meters")

# # ------------------------------------------
# # Matrices
# # A two-dimensional array, or a matrix, is also a natural application of a list within a list.

# my_matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]

# print(my_matrix[0][1])
# my_matrix[1][0] = 10
# print(my_matrix)
# print("----------------------")
# for row in my_matrix:
#     print(row)

# ---------------------------------------------------
# # Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer value as its arguments. The function then counts how many elements within the matrix match the argument value.


# def count_matching_elements(my_matrix: list, element: int):
#     counts = 0
#     for row in my_matrix:
#         for item in row:
#             if item == element:
#                 counts += 1

#     return counts


# m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
# print(count_matching_elements(m, 1))

# # In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces.

# # Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:

# # 0: empty square
# # 1: player 1 game piece
# # 2: player 2 game piece
# # The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.

# # The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0.


# def who_won(game_board: list):
#     player1 = 0
#     player2 = 0
#     for row in game_board:
#         for item in row:
#             if item == 1:
#                 player1 += 1
#             elif item == 2:
#                 player2 += 1

#     if player1 > player2:
#         return 1
#     elif player2 > player1:
#         return 2
#     else:
#         return 0


# board1 = [[1, 2, 0], [1, 1, 1], [0, 0, 0]]
# board2 = [[1, 2, 0], [1, 2, 2], [0, 0, 0]]
# board3 = [[1, 2, 2], [1, 1, 2], [0, 0, 0]]

# print(f"board1: {who_won(board1)}")
# print(f"board2: {who_won(board2)}")
# print(f"board3: {who_won(board3)}")

# # Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.

# # The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.


# def row_correct(sudoku: list, row_no: int):
#     found = []

#     for item in sudoku[row_no]:
#         if item == 0:
#             continue

#         if item in found:
#             return False

#         found.append(item)

#     return True


# sudoku = [
#     [9, 0, 0, 0, 8, 0, 3, 0, 0],
#     [2, 0, 0, 2, 5, 0, 7, 0, 0],
#     [0, 2, 0, 3, 0, 0, 0, 0, 4],
#     [2, 9, 4, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 7, 3, 0, 5, 6, 0],
#     [7, 0, 5, 0, 6, 0, 4, 0, 0],
#     [0, 0, 7, 8, 0, 3, 9, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 3],
#     [3, 0, 0, 0, 0, 0, 0, 0, 2],
# ]

# print(row_correct(sudoku, 0))
# print(row_correct(sudoku, 1))


# # Please write a function named column_correct(sudoku: list, column_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single column, as its arguments. Columns are indexed from 0.

# # The function should return True or False, depending on whether the column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

# def column_correct(sudoku: list, column_no: int):
#     found = []
#     i = 0

#     while i < len(sudoku):
#         if sudoku[i][column_no] == 0:
#             i += 1
#             continue

#         if sudoku[i][column_no] in found:
#             return False

#         found.append(sudoku[i][column_no])
#         i += 1

#     return True

# sudoku = [
#     [9, 0, 0, 0, 8, 0, 3, 0, 0],
#     [2, 0, 0, 2, 5, 0, 7, 0, 0],
#     [0, 2, 0, 3, 0, 0, 0, 0, 4],
#     [2, 9, 4, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 7, 3, 0, 5, 6, 0],
#     [7, 0, 5, 0, 6, 0, 4, 0, 0],
#     [0, 0, 7, 8, 0, 3, 9, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 3],
#     [3, 0, 0, 0, 0, 0, 0, 0, 2],
# ]

# print(column_correct(sudoku, 0))
# print(column_correct(sudoku, 1))


# # Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.

# # The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.

# # Notice that this function does not strictly follow the rules of sudoku. In a real game of sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). Such restrictions on indexes should not be implemented here.

# def block_correct(sudoku: list, row_no: int, column_no: int):
#     found = []
#     i = row_no

#     while i < row_no + 3:
#         j = column_no

#         while j < column_no + 3:
#             if sudoku[i][j] == 0:
#                 j += 1
#                 continue

#             if sudoku[i][j] in found:
#                 return False

#             found.append(sudoku[i][j])
#             j += 1

#         i += 1

#     return True

# sudoku = [
#     [9, 0, 0, 0, 8, 0, 3, 0, 0],
#     [2, 0, 0, 2, 5, 0, 7, 0, 0],
#     [0, 2, 0, 3, 0, 0, 0, 0, 4],
#     [2, 9, 4, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 7, 3, 0, 5, 6, 0],
#     [7, 0, 5, 0, 6, 0, 4, 0, 0],
#     [0, 0, 7, 8, 0, 3, 9, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 3],
#     [3, 0, 0, 0, 0, 0, 0, 0, 2],
# ]


# print(block_correct(sudoku, 0, 0))
# print(block_correct(sudoku, 1, 2))


# # Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above into your Python code file for this exercise.
# # The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False.
# # The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders. These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).


# def row_correct(sudoku: list, row_no: int):
#     found = []

#     for item in sudoku[row_no]:
#         if item == 0:
#             continue

#         if item in found:
#             return False

#         found.append(item)

#     return True


# def column_correct(sudoku: list, column_no: int):
#     found = []
#     i = 0

#     while i < len(sudoku):
#         if sudoku[i][column_no] == 0:
#             i += 1
#             continue

#         if sudoku[i][column_no] in found:
#             return False

#         found.append(sudoku[i][column_no])
#         i += 1

#     return True


# def block_correct(sudoku: list, row_no: int, column_no: int):
#     found = []
#     i = row_no

#     while i < row_no + 3:
#         j = column_no

#         while j < column_no + 3:
#             if sudoku[i][j] == 0:
#                 j += 1
#                 continue

#             if sudoku[i][j] in found:
#                 return False

#             found.append(sudoku[i][j])
#             j += 1

#         i += 1

#     return True


# def sudoku_grid_correct(sudoku: list):
#     i = 0

#     while i < 9:
#         if not row_correct(sudoku, i):
#             return False

#         if not column_correct(sudoku, i):
#             return False

#         i += 1

#     row = 0

#     while row < 9:
#         column = 0

#         while column < 9:
#             if not block_correct(sudoku, row, column):
#                 return False

#             column += 3

#         row += 3

#     return True


# sudoku1 = [
#     [9, 0, 0, 0, 8, 0, 3, 0, 0],
#     [2, 0, 0, 2, 5, 0, 7, 0, 0],
#     [0, 2, 0, 3, 0, 0, 0, 0, 4],
#     [2, 9, 4, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 7, 3, 0, 5, 6, 0],
#     [7, 0, 5, 0, 6, 0, 4, 0, 0],
#     [0, 0, 7, 8, 0, 3, 9, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 3],
#     [3, 0, 0, 0, 0, 0, 0, 0, 2],
# ]

# print(sudoku_grid_correct(sudoku1))


# sudoku2 = [
#     [2, 6, 7, 8, 3, 9, 5, 0, 4],
#     [9, 0, 3, 5, 1, 0, 6, 0, 0],
#     [0, 5, 1, 6, 0, 0, 8, 3, 9],
#     [5, 1, 9, 0, 4, 6, 3, 2, 8],
#     [8, 0, 2, 1, 0, 5, 7, 0, 6],
#     [6, 7, 4, 3, 2, 0, 0, 0, 5],
#     [0, 0, 0, 4, 5, 7, 2, 6, 3],
#     [3, 2, 0, 0, 8, 0, 0, 5, 7],
#     [7, 4, 5, 0, 0, 3, 9, 0, 1],
# ]

# print(sudoku_grid_correct(sudoku2))


# -------------------------------------------
# # # References

# name="ali"
# print(id(name))


# number = 1
# print(id(number))
# number += 10
# print(id(number))
# a = 1
# print(id(a))


# # # Multiple references to the same list
# list1 = [1, 2, 3, 4]
# list2 = list1

# list1[0] = 10
# list2[1] = 20

# print(list1)
# print(list2)
# print(id(list1))
# print(id(list2))


# # Please write a function named double_items(numbers: list), which takes a list of integers as its argument.
# # The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.


# def double_items(numbers: list):
#     new_list = []
#     for item in numbers:
#         new_list.append(item * 2)
#     return new_list


# numbers = [2, 4, 5, 3, 11, -4]
# numbers_doubled = double_items(numbers)
# print("original:", numbers)
# print("doubled:", numbers_doubled)


# # Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.
# # The functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.
# # The function should not have a return value - it should directly modify the list it receives as a parameter.


# def remove_smallest(numbers: list):
#     numbers.remove(min(numbers))


# numbers = [2, 4, 6, 1, 3, 5]
# remove_smallest(numbers)
# print(numbers)


# # In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.
# # The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.
# # The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.


# def print_sudoku(sudoku: list):
#     for row in sudoku:
#         for i in range(len(row)):
#             if row[i] == 0:
#                 print("_", end="")
#             else:
#                 print(row[i], end="")

#             if i == 2 or i == 5:
#                 print("  ", end="")
#             else:
#                 print(" ", end="")

#         print()

#         if row == sudoku[2] or row == sudoku[5]:
#             print()


# def add_number(sudoku: list, row_no: int, column_no: int, number: int):
#     sudoku[row_no][column_no] = number


# sudoku = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# print_sudoku(sudoku)
# add_number(sudoku, 0, 0, 2)
# add_number(sudoku, 1, 2, 7)
# add_number(sudoku, 5, 7, 3)
# print()
# print("Three numbers added:")
# print()
# print_sudoku(sudoku)


# # This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.
# # The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.


# def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
#     sudoku_new = []

#     for old_row in sudoku:
#         new_row = []

#         for item in old_row:
#             new_row.append(item)

#         sudoku_new.append(new_row)

#     sudoku_new[row_no][column_no] = number
#     return sudoku_new


# sudoku = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)

# # ------------------------------------------
# # Tic-Tac-Toe is played on a 3 by 3 grid, by two players who take turns inputting noughts and crosses. If either player succeeds in placing three of their own symbols on any row, column or diagonal, they win. If neither player manages this, it is a draw.
# # Please write a function named play_turn(game_board: list, x: int, y: int, piece: str), which places the given symbol at the given coordinates on the board. The values of the coordinates on the board are between 0 and 2.
# # NB: when compared to the sudoku exercises, the arguments the function takes are the other way around here. The column x comes first, and the row y second.


# def play_turn(game_board: list, x: int, y: int, piece: str):
#     i = 0
#     while i < len(game_board):
#         j = 0
#         while j < len(game_board[i]):
#             if i == x and j == y:
#                 if game_board[j][i] != "":
#                     return False
#                 game_board[j][i] = piece
#                 return True
#             j += 1
#         i += 1
#     return False


# game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
# print(play_turn(game_board, 2, 0, "X"))
# print(game_board)


# # Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.
# # You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.


# def transpose(matrix: list):
#     i = 0
#     while i < len(matrix):
#         j = i + 1
#         while j < len(matrix):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp
#             j += 1
#         i += 1


# inp_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(inp_matrix)
# transpose(inp_matrix)
# print(inp_matrix)

# # ---------------------------------------
# # # Side effects of functions
# # If a function takes a reference to a list as an argument, it will be able to modify that list. If direct modifications were not intended by the programmer, accidentally modifying the list received as a parameter could cause problems elsewhere in the program.
# # Let's take a look at a function which is supposed to find the second smallest item in a list:


# def second_smallest(my_list: list) -> int:
#     # in an ordered list, the second smallest item is at index 1
#     my_list.sort()
#     return my_list[1]


# numbers = [1, 4, 2, 5, 3, 6, 4, 7]
# print(second_smallest(numbers))
# print(numbers)


# # The function does find the second smallest item reliably, but it additionally sorts the list in place, changing the order of the items. If the order is significant elsewhere in the program, calling the function could cause errors. Unintentional modifications to an object accessed through a reference is called a side effect of a function.
# # We can avoid the side effect by making a small change to the function:


# def second_smallest(my_list: list) -> int:
#     list_copy = sorted(my_list)
#     return list_copy[1]


# numbers = [1, 4, 2, 5, 3, 6, 4, 7]
# print(second_smallest(numbers))
# print(numbers)

# # The function sorted returns a new, sorted copy of the list, so looking for the second smallest item no longer messes with the order of the original list.
# # It is generally considered a good programming practice to avoid causing side effects with functions. Side effects can make it more difficult to verify that the program functions as intended in all situations.

# # ----------------------------------------------------------
# # # Dictionary

# my_dictionary = {}

# my_dictionary["apina"] = "monkey"
# my_dictionary["banaani"] = "banana"
# my_dictionary["cembalo"] = "harpsichord"

# print(len(my_dictionary))
# print(my_dictionary)
# print(my_dictionary["apina"])

# word = input("Please type in a word: ")
# if word in my_dictionary:
#     print("Translation: ", my_dictionary[word])
# else:
#     print("Word not found")


# # Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. The keys of the dictionary should be the numbers between start_index and end_index inclusive
# # The value mapped to each key should be the key times ten.


# def times_ten(start_index: int, end_index: int):
#     new_dictionary = {}
#     i = start_index
#     while i <= end_index:
#         new_dictionary[i] = i * 10
#         i += 1

#     return new_dictionary


# d = times_ten(3, 6)
# print(d)

# # Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.
# # A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.


# def factorials(n: int):
#     new_dictionary = {}
#     i = 1
#     while i <= n:
#         j = i
#         val = 1
#         while j >= 1:
#             val = val * j
#             j -= 1
#         new_dictionary[i] = val
#         i += 1

#     return new_dictionary


# k = factorials(5)
# print(k[1])
# print(k[3])
# print(k[5])
# print(factorials(10))

# # -----------------------------------------------
# # # Traversing a dictionary
# my_dictionary = {}

# my_dictionary["apina"] = "monkey"
# my_dictionary["banaani"] = "banana"
# my_dictionary["cembalo"] = "harpsichord"

# # for key in my_dictionary:
# #     print("key:", key)
# #     print("value:", my_dictionary[key])


# # Sometimes you need to traverse the entire contents of a dictionary. The method items returns all the keys and values stored in the dictionary, one pair at a time:

# for key, value in my_dictionary.items():
#     print("key:", key)
#     print("value:", value)


# # Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.


# def histogram(inp_string: str):
#     new_dictionary = {}
#     i = 0
#     while i < len(inp_string):
#         new_dictionary[inp_string[i]] = "*" * inp_string.count(inp_string[i])
#         i += 1

#     print(f"Histogram for {inp_string} is : ")
#     print(f"--------------{"-"*len(inp_string)}-----")
#     for key, value in new_dictionary.items():
#         print(key, value)


# histogram("abba")
# histogram("statistically")

# ---------------------------------------
# # # Phone book, version 1

# phoneBook = {}

# while True:
#     command = int(input("command (1 search, 2 add, 3 quit): "))

#     if command == 1:
#         name = input("name: ")
#         if name in phoneBook:
#             print(phoneBook[name])
#         else:
#             print("no number")
#     elif command == 2:
#         name = input("name: ")
#         number = input("number: ")
#         phoneBook[name] = number
#         print("ok!")
#     elif command == 3:
#         print("quitting...")
#         break
#     else:
#         print("error!")


# ------------------------------------
# # Phone book, version 2

# phoneBook = {}

# while True:
#     command = int(input("command (1 search, 2 add, 3 quit): "))

#     if command == 1:
#         name = input("name: ")
#         if name in phoneBook:
#             for item in phoneBook[name]:
#                 print(item)
#         else:
#             print("no number")
#     elif command == 2:
#         name = input("name: ")
#         number = input("number: ")
#         if name in phoneBook:
#             phoneBook[name].append(number)
#         else:
#             phoneBook[name] = [number]
#         print("ok!")
#     elif command == 3:
#         print("quitting...")
#         break
#     else:
#         print("error!")


# # Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.

# def invert(dictionary: dict):
#     keys = []
#     values = []
#     for key in dictionary:
#         keys.append(key)
#         values.append(dictionary[key])
#     dictionary.clear()

#     i = 0
#     while i < len(keys):
#         dictionary[values[i]] = keys[i]
#         i += 1


# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# print(s)
# invert(s)
# print(s)


# # Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys. The value attached to each key should be the number spelled out in words.

# numbers_words = [
#     "zero",
#     "one",
#     "two",
#     "three",
#     "four",
#     "five",
#     "six",
#     "seven",
#     "eight",
#     "nine",
#     "ten",
#     "eleven",
#     "twelve",
#     "thirteen",
#     "fourteen",
#     "fifteen",
#     "sixteen",
#     "seventeen",
#     "eighteen",
#     "nineteen",
# ]

# tens_words = [
#     "twenty",
#     "thirty",
#     "forty",
#     "fifty",
#     "sixty",
#     "seventy",
#     "eighty",
#     "ninety",
# ]


# def dict_of_numbers():
#     numbers_dict = {}
#     i = 0
#     while i <= 99:
#         if i < 20:
#             numbers_dict[i] = numbers_words[i]
#             i += 1
#             continue
#         if i % 10 != 0:
#             numbers_dict[i] = tens_words[(i // 10) - 2] + "-" + numbers_words[i % 10]
#         else:
#             numbers_dict[i] = tens_words[(i // 10) - 2]
#         i += 1
#     return numbers_dict


# numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])
# print(dict_of_numbers())

# Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.
# The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.
# name
# director
# year
# runtime
# The values attached to these keys are given as arguments to the function.


# def add_movie(database: list, name: str, director: str, year: int, runtime: int):
#     movie = {}
#     movie["name"] = name
#     movie["director"] = director
#     movie["year"] = year
#     movie["runtime"] = runtime

#     database.append(movie)


# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)


# # Please write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise. The function should formulate a new list, which contains only the movies whose title includes the word searched for. Capitalisation is irrelevant here. A search for ana should return a list containing both Anaconda and Management.


# def find_movies(database: list, search_item: str):
#     found = []
#     for item in database:
#         if (item["name"].lower()).find((search_item).lower()) >= 0:
#             found.append(item)
#     return found


# database = [
#     {
#         "name": "Gone with the Python",
#         "director": "Victor Pything",
#         "year": 2017,
#         "runtime": 116,
#     },
#     {
#         "name": "Pythons on a Plane",
#         "director": "Renny Pytholin",
#         "year": 2001,
#         "runtime": 94,
#     },
#     {
#         "name": "Dawn of the Dead Programmers",
#         "director": "M. Night Python",
#         "year": 2011,
#         "runtime": 101,
#     },
# ]

# my_movies = find_movies(database, "python")
# print(my_movies)


# ===========================
# # # Tuple:

# Tuple is a data structure which is, in many ways, similar to a list. The most important differences between the two are:
# Tuples are enclosed in parentheses (), while lists are enclosed in square brackets []
# Tuples are immutable, while the contents of a list may change


# # Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:

# # The first element in the tuple is the smallest of the arguments
# # The second element in the tuple is the greatest of the arguments
# # The third element in the tuple is the sum of the arguments


# def create_tuple(x: int, y: int, z: int):
#     elements = []
#     elements.append(x)
#     elements.append(y)
#     elements.append(z)
#     new_tuple = (min(elements), max(elements), sum(elements))
#     return new_tuple


# print(create_tuple(5, 3, -1))

# # Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.

# def oldest_person(people: list):
#     result = people[0]
#     for item in people:
#         if item[1] < result[1]:
#             result = item

#     return result[0]

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))

# # In this exercise we are handling tuples just like the ones described in the previous exercise.
# # Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. The function should return the names of these people in a new list.


# def older_people(people: list, year: int):
#     result_list = []
#     for item in people:
#         if item[1] < year:
#             result_list.append(item[0])

#     return result_list


# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# older = older_people(people, 1979)
# print(older)

# # Because tuples are immutable, unlike lists, they can be used as keys in a dictionary. The following bit of code creates a dictionary, where the keys are coordinate points:

# points = {}
# points[(3, 5)] = "monkey"
# points[(5, 0)] = "banana"
# points[(1, 2)] = "harpsichord"
# print(points[(3, 5)])

# # ----------------------------------------------
# # # # Student database:

# # In this series of exercises you will create a simple student database. Before diving in, please spend a moment reading through the instructions and thinking about what sort of data structures are necessary for organising the data stored by your program.

# # part1: adding students
# # First write a function named add_student, which adds a new student to the database. Also write a preliminary version of the function print_student, which prints out the information of a single student.

# # Part 2: adding completed courses
# # Please write a function named add_course, which adds a completed course to the information of a specific student in the database. The course data is a tuple consisting of the name of the course and the grade:

# # Part 3: repeating courses
# # Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in the database in that specific student's information, the grade recorded in the database should never be lowered if the course is repeated.

# # Part 4: summary of database
# # Please write a function named summary, which prints out a summary based on all the information stored in the database.


# def add_student(database: dict, name: str):
#     database[name] = []


# def print_student(database: dict, name: str):
#     if name in database:
#         print(f"{name}: ")
#         if len(database[name]) > 0:
#             total_grade = 0
#             print(f"{len(database[name])} completed course: ")
#             for item in database[name]:
#                 print(item[0], item[1])
#                 total_grade = total_grade + item[1]
#             print(f"Average grade {total_grade/len(database[name])}")
#         else:
#             print("no completed course")
#     else:
#         print(f"{name}: no such person in the database")


# def add_course(database: dict, name: str, course: tuple):
#     if course[1] == 0:
#         return

#     if name not in database:
#         return

#     for item in database[name]:
#         if item[0] == course[0]:
#             if item[1] > course[1]:
#                 return
#             else:
#                 database[name].remove(item)
#                 database[name].append(course)
#                 return

#     database[name].append(course)


# def summary(database: dict):
#     total_students = len(database)
#     most_courses = 0
#     c_name = ""
#     best_avg = 0
#     b_name = ""

#     for key in database:
#         if len(database[key]) > most_courses:
#             most_courses = len(database[key])
#             c_name = key
#         if len(database[key]) > 0:
#             total_grade = 0
#             for item in database[key]:
#                 total_grade = total_grade + item[1]
#                 avg = total_grade / len(database[key])
#                 if best_avg < avg:
#                     best_avg = avg
#                     b_name = key

#     print(f"students {total_students}")
#     print(f"most courses completed {most_courses} {c_name}")
#     print(f"best average grade {best_avg} {b_name}")


# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)

# # ------------------------------------------------------------------
