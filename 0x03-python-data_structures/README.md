0x03. Python - Data Structures: Lists, Tuples
About
An introductory project on:

Lists, their methods, and how to use them
How to use lists as stacks and queues
List comprehensions and how to use them
Tuples and how to use them
Sequences
Tuple packing
Sequence unpacking
The del statement and how to use it
Requirements
Python Scripts
Python 3.4
pep8 1.7
C Files
Ubuntu 14.04 LTS
gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
Betty Style
File Descriptions
Mandatory
0-print_list_integer.py - Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):
Format: one integer per line
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
1-element_at.py - Write a function that retrieves an element from a list like on C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except
2-replace_in_list.py - Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use try/except
3-print_reversed_list_integer.py - Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
4-new_in_list.py - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except
5-no_c.py - Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
The function shoud return the new string
You are not allowed to import any module
You are not allowed to use str.replace()
6-print_matrix_integer.py - Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
7-add_tuple.py - Write a function that adds 2 tuples.
