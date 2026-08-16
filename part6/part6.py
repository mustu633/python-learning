# # # ====================== Part 6 =========================

# # # Reading files

# # Reading text files (.txt)

# with open("example.txt") as new_file:
#     contents = new_file.read()
#     print(contents)

# # ---------------------
# with open("example.txt") as new_file:
#     count = 0
#     total_length = 0

#     for line in new_file:
#         line = line.replace("\n", "")
#         count += 1
#         print("Line", count, line)
#         length = len(line)
#         total_length += length

# print("Total length of lines:", total_length)


# # The file numbers.txt contains integer numbers, one number per line.
# # Please write a function named largest, which reads the file and returns the largest number in the file.
# # Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.


# def largest():
#     with open("number.txt") as new_file:
#         result = 0
#         for line in new_file:

#             line = line.replace("\n", "")
#             line = int(line)
#             if line > result:
#                 result = line

#     return result


# print(largest())

# ---------------------------------------
# # Reading CSV files (.csv)

# text = "monkey,banana,harpsichord"
# words = text.split(",")
# print(words)
# for word in words:
#     print(word)

# # ---------------------------------------
# # example:

# with open("grades.csv") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         parts = line.split(";")
#         name = parts[0]
#         grades = parts[1:]
#         print("Name:", name)
#         print("Grades:", grades)


# # The file fruits.csv contains names of fruits, and their prices, in the format specified in this example:
# # Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents. In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float.


# def read_fruits():
#     new_dictionary = {}
#     with open("fruits.csv") as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             item = line.split(";")
#             new_dictionary[item[0]] = item[1]

#     return new_dictionary


# print(read_fruits())


# The file matrix.txt contains a matrix in the format specified in the example below:
# 1,2,3
# 2,3,4
# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.
# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as
# the function should return the list [6, 9].


def matrix_sum():
    result = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            elements = line.split(",")
            for item in elements:
                result = result + int(item)
    return result


def matrix_max():
    result = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            elements = line.split(",")
            for item in elements:
                item = int(item)
                if item > result:
                    result = int(item)
    return result


def row_sums():
    result = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            elements = line.split(",")
            sum = 0
            for item in elements:
                sum = sum + int(item)
            result.append(sum)
    return result


print(matrix_sum())
print(matrix_max())
print(row_sums())
