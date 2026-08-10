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


# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.
# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.
# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.


def print_sudoku(sudoku: list):
    for row in sudoku:
        for i in range(len(row)):
            if row[i] == 0:
                print("_", end="")
            else:
                print(row[i], end="")

            if i == 2 or i == 5:
                print("  ", end="")
            else:
                print(" ", end="")

        print()

        if row == sudoku[2] or row == sudoku[5]:
            print()


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number


sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)
