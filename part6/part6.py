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


# # The file matrix.txt contains a matrix in the format specified in the example below:
# # 1,2,3
# # 2,3,4
# # Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.
# # Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as
# # the function should return the list [6, 9].


# def matrix_sum():
#     result = 0
#     with open("matrix.txt") as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             elements = line.split(",")
#             for item in elements:
#                 result = result + int(item)
#     return result


# def matrix_max():
#     result = 0
#     with open("matrix.txt") as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             elements = line.split(",")
#             for item in elements:
#                 item = int(item)
#                 if item > result:
#                     result = int(item)
#     return result


# def row_sums():
#     result = []
#     with open("matrix.txt") as new_file:
#         for line in new_file:
#             line = line.replace("\n", "")
#             elements = line.split(",")
#             sum = 0
#             for item in elements:
#                 sum = sum + int(item)
#             result.append(sum)
#     return result


# print(matrix_sum())
# print(matrix_max())
# print(row_sums())

# # -------------------------------
# # # Course grading, part 1
# # This program works with two CSV files. One of them contains information about some students on a course.
# # The other contains the number of exercises each student has completed each week.
# # As you can see above, both CSV files also have a header row, which tells you what each column contains.
# # Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:

# # Sample output
# # Student information: students1.csv
# # Exercises completed: exercises1.csv
# # pekka peloton 21
# # jaana javanainen 27
# # liisa virtanen 35


# # # Course grading, part 2
# # Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file.
# # In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.
# # The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.
# # Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 10 points. The number of points awarded is always an integer number.

# students_info = input("Student information: ")
# exercises_info = input("Exercises completed: ")
# exam_info = input("Exam points: ")

# students = {}

# with open(students_info) as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         elements = line.split(";")

#         if elements[0] == "id":
#             continue

#         students[elements[0]] = [elements[1], elements[2]]

# with open(exercises_info) as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         elements = line.split(";")

#         if elements[0] == "id":
#             continue

#         student_id = elements.pop(0)
#         students[student_id].append(elements)

# with open(exam_info) as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         elements = line.split(";")

#         if elements[0] == "id":
#             continue

#         student_id = elements.pop(0)
#         students[student_id].append(elements)


# print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")

# for key in students:

#     # Total number of exercises completed
#     exercise_count = 0

#     for item in students[key][2]:
#         exercise_count += int(item)

#     # Exercise points
#     exercise_points = exercise_count // 4

#     # Exam points
#     exam_points = 0

#     for item in students[key][3]:
#         exam_points += int(item)

#     # Total points
#     total_points = exercise_points + exam_points

#     # Grade
#     if total_points <= 14:
#         grade = 0
#     elif total_points <= 17:
#         grade = 1
#     elif total_points <= 20:
#         grade = 2
#     elif total_points <= 23:
#         grade = 3
#     elif total_points <= 27:
#         grade = 4
#     else:
#         grade = 5

#     # Full name
#     name = students[key][0] + " " + students[key][1]

#     print(f"{name:30}{exercise_count:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")

# # Please write a program which asks the user to type in some text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them.
# # The case of the letters should be irrelevant to the functioning of your program.
# # The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.


# word_list = []
# with open("wordlist.txt") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         word_list.append(line.lower())


# text = input("Write text: ")
# feedback = ""

# i = 0
# word = ""
# while i < len(text):
#     if text[i] == " ":
#         if word.lower() in word_list:
#             feedback += word + " "
#         else:
#             feedback += f"*{word}*" + " "
#         word = ""
#         i += 1
#         continue
#     word = word + text[i]
#     i += 1

# print(feedback)


# # This exercise is about creating a program which allows the user to search for recipes based on their names, preparation times, or ingredients used. The program should read the recipes from a file submitted by the user.
# # Each recipe consists of three or more lines. The first line has the name of the recipe, the second line contains an integer number representing the preparation time in minutes, and the remaining line or lines contain the ingredients used, one on each line. The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file.

# # Part 1: Search for recipes based on the name of the recipe
# # Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose name contains the given search string. The names of these recipes are then returned in a list.

# # Part 2: Search for recipes based on the preparation time
# # Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments. The function should go through the file and select all recipes whose preparation time is at most the number given.
# # The names of these recipes are again returned in a list, but the preparation time should be appended to each name.

# # Part 3: Search for recipes based on the ingredients
# # Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose ingredients contain the given search string.
# # The names of these recipes are returned in a list just like in the second part, with the preparation time appended.

# all_recipes = []
# name = ""


# def read_file(filename: str):
#     with open(filename) as new_file:
#         single = []
#         for line in new_file:
#             line = line.replace("\n", "")

#             if line == "":
#                 all_recipes.append(single)
#                 single = []
#                 continue
#             single.append(line)
#         all_recipes.append(single)


# def search_by_name(filename: str, word: str):
#     read_file(filename)
#     result = []
#     for item in all_recipes:
#         if word.lower() in item[0].lower():
#             result.append(item[0])

#     return result


# # found_recipes = search_by_name("recipes1.txt", "cake")

# # for recipe in found_recipes:
# #     print(recipe)


# def search_by_time(filename: str, prep_time: int):
#     read_file(filename)
#     result = []
#     for item in all_recipes:
#         if int(item[1]) <= prep_time:
#             result.append(f"{item[0]}, preparation time {item[1]} min")
#     return result


# # found_recipes = search_by_time("recipes1.txt", 20)

# # for recipe in found_recipes:
# #     print(recipe)


# def search_by_ingredient(filename: str, ingredient: str):
#     read_file(filename)
#     result = []
#     for item in all_recipes:
#         i = 2
#         while i < len(item):
#             if item[i] == ingredient:
#                 result.append(f"{item[0]}, preparation time {item[1]} min")
#                 break
#             i += 1
#     return result


# found_recipes = search_by_ingredient("recipes1.txt", "eggs")

# for recipe in found_recipes:
#     print(recipe)


# # In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.
# # Part1: Distance between stations
# # First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary format
# # Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station. The first element in the tuple is the Longitude field, and the second is the Latitude field.
# # Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.
# # The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

# # Part 2: The greatest distance
# # Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other. The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.


# def get_station_data(filename: str):
#     result = {}
#     with open(filename) as new_file:
#         for line in new_file:
#             line = line.replace("/n", "")
#             element = line.split(";")
#             if element[0] == "Longitude":
#                 continue

#             result[element[3]] = (float(element[0]), float(element[1]))

#     return result


# import math


# def distance(stations: dict, station1: str, station2: str):
#     x_km = (stations[station1][0] - stations[station2][0]) * 55.26
#     y_km = (stations[station1][1] - stations[station2][1]) * 111.2

#     distance_km = math.sqrt(x_km**2 + y_km**2)

#     return distance_km


# def greatest_distance(stations: dict):
#     greatest = 0
#     station_a = ""
#     station_b = ""

#     for station1 in stations:
#         for station2 in stations:
#             d = distance(stations, station1, station2)

#             if d > greatest:
#                 greatest = d
#                 station_a = station1
#                 station_b = station2

#     return (station_a, station_b, greatest)


# stations = get_station_data("stations1.csv")
# print(stations)

# d1 = distance(stations, "Kaivopuisto", "Laivasillankatu")
# print(d1)
# d2 = distance(stations, "Kaivopuisto", "Kapteeninpuistikko")
# print(d2)

# result = greatest_distance(stations)
# print(result)
