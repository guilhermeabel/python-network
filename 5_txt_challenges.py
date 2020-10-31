# 1 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Create a Python script that reads a text file into a list and then
# converts the list back into a string which is the entire file content.
# 1 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# with open('txt/banking.txt') as file:
#     main_list = file.read().splitlines()

# string = ', '.join(main_list)
# print(string)


# 2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Create a Python function called tail that reads the last n lines of a text file.
# The function has two arguments: the file name and n (the number of lines to read).
# This is similar to the Linux `tail` command.
# Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.
# 2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# def tail(name, n):
#     main_list = list()
#     with open(f'txt/{name}') as file:
#         main_list = file.readlines()
#         last_lines = main_list[-n:]
#     print(last_lines)

# tail('sample_file.txt', 5)


# 3 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Change the solution from the previous challenge so that the script that prints out
# the last n lines of the file refreshes the output every 3 seconds (as the file changes
# or updates). This is similar to `tail -f` Linux command
# 3 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# import time

# def tail(name, n):
#     main_list = list()
#     with open(f'txt/{name}') as file:
#         main_list = file.readlines()
#         last_lines = main_list[-n:]
#     print(last_lines)


# import time
# starttime = time.time()
# while True:
#     tail('sample_file.txt', 5)
#     time.sleep(3.0 - ((time.time() - starttime) % 3.0))


# 4 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Write a Python program to count the number of lines, words and characters in a text file.
# This is similar to the Linux `wc` command. Create a function if possible.
# 4 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# def wc(filename):
#     with open(f'txt/{filename}') as file:
#         n_char = 0
#         n_words = 0
#         lines = file.read().splitlines()
#         print(f'n of lines: {len(lines)}')
#         for line in lines:
#             n_char += len(line)
#         print(f'n of char: {n_char}')
#         for line in lines:
#             n_words += len(line.split())
#         print(f'n of words: {n_words}')

# wc('sample_file.txt')

# 5 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Write a Python program that calculates the net amount of a bank account based on the
# transactions saved in a text file.
# The file format is as following:
# D:50
# W:100
# D means deposit while W means withdrawal.
# Suppose that the banking.txt file is supplied to the program:
# D:300
# D:300
# W:500
# D:200
# Then, the output should be: 300
# 5 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# with open('txt/banking.txt') as file:
#    net = 0
#    for line in file:
#        net = file.readline()


# 6 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Write a Python script that compares two text files line by line
# and display the lines that differ.
# 6 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

with open('txt/banking.txt') as file1:
    with open('txt/sample_file.txt') as file2:
        difference = set(file1).difference(file2)

print(difference)

# 7 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Consider american-english.txt dictionary file.
# Write a Python script that reads the file in a dictionary. The words in the file
# will be the dictionary keys and the length of each word the corresponding values.
# 7 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# 8 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Consider american-english.txt dictionary file.
# Write a Python script that finds the first 100 longest words in the file.
# Tip: See 'dict_sort_by_value.py' on how to get a sorted view of a dictionary.
# 8 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# 9 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Consider american-english.txt dictionary file.
# Write a Python script that finds the number of occurrences of each letter of the alphabet
# in all the words in the dictionary.
# You want to see how many times do ‘a’, ‘b’, ‘c’ and so on appear in all the words in the
# dictionary.
# Which is the most frequently used letter in English words?
# 9 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# 10 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Continue the previous challenge and find the 3 most frequently used letters in all
# English Words.
# You should get: ('e', 67681), ('s', 50872), ('i', 50818)
# 10 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
