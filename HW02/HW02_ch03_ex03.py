#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body
def do_twice(f,val):
	""" Calls a function with one argument twice"""
	f(val)
	f(val)


def do_four(f,val):
	""" Calls a function with one argument twice"""
	do_twice(f,val)
	f(val)
	f(val)


def print_row_boundary(n):
	""" Prints the row boundary of the grid based on its dimensions """
	row_boundary = "+" + "-" * 4
	print((row_boundary*n)+"+")

def print_cell_area(n):
	""" Prints the column boundary and the cell area of the grid based on its dimensions """
	cell_area = " " * 4
	column_boundary = "|"
	print((column_boundary+cell_area) * (n + 1),)



def two_by_two():
	
	n=2 # Dimension of the square grid
	
	print_row_boundary(n)
	do_four(print_cell_area,n)
	print_row_boundary(n)
	do_four(print_cell_area,n)
	print_row_boundary(n)

def four_by_four():

	n=4 # Dimension of the square grid
	
	print_row_boundary(n)
	do_four(print_cell_area,n)
	print_row_boundary(n)
	do_four(print_cell_area,n)
	print_row_boundary(n)



# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    two_by_two()
    four_by_four()
    



if __name__ == "__main__":
    main()