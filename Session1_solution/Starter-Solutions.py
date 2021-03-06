"""
File: Starter-Solutions
Description: Part of the IEEExHKN Programming in the Sky Workshop on April
		     22, 2018. This file simply contains a few quick warmup exercises.
Editor:	Antony Nguyen, Godwin Pang
"""

"""
Comments
-----
These exercises will cover comments
"""

# TODO Comment this line out
#Comment me out

"""
Numbers
-----
These exercises will cover basic numbers
"""

# TODO Print any number
print(5)

# TODO Add any two numbers together
print(5+5)

"""
Strings
-----
These exercises will cover strings
"""

# TODO Print Hello World
print("Hello World")

# TODO Print the following sentence
# Chickens can't moo
print("Chickens can't moo")

# TODO Print the following sentence
# The cow says "Moo" (NOTICE THE QUOTATION MARKS)
print('The cow says "Moo"')

"""
Variables
"""

# TODO Print 'the sky' using the variables whats and up
whats = "the "
up = "sky"
print(whats + up)

# TODO Print 5 using the two variables
two = "2"
three = "3"
print(int(two)+int(three))

# TODO Print "Hello World" using the variable hello
hello = "Goodbye" # DO NOT DELETE OR CHANGE THIS LINE
hello = "Hello World"
print(hello) # DO NOT DELETE OR CHANGE THIS LINE

# TODO Print "My move is 0, 0" using row and col
row = 0
col = 0
print("My move is " + str(row) + ", " + str(col))

"""
List Comprehension
"""

list1 = [0,1,2,3,4]
list2 = [0,1,2,3,2,1,0]
list3 = [1,1]

#TODO Create a new list called newlist1 that contains all the integers from 0
#     to 4 inclusive

# Code goes directly below this line and above the if statement
newlist1 = [i for i in range(5)]

if(newlist1 == list1):
    print("You passed List Comprehension Exercise 1")
else:
    print("You failed List Comprehension Exercise 1")

#TODO Create a new list called newlist2 that contains all occurrences of 1 in
#     list2

# Code goes directly below this line and above the if statement
newlist2 = [i for i in list2 if i == 1]

if(newlist2 == list3):
    print("You passed List Comprehension Exercise 2")
else:
    print("You failed List Comprehension Exercise 2")
