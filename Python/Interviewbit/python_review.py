# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:00:47 2024

@author: USER
"""

# Updated: 2024/05/24
# # keyboard hotkey: 
# 1. shrink tab: ctrl + [ 
# 2. switch to console command: ctrl + shift + i
# 3. switch to editor: " " + e

# Updated: 2024/05/27:
# 1. checkly review day 1 part (basic, flow control & function, strings)

import datetime
print(datetime.datetime.now().strftime("%D"))
help(datetime.MAXYEAR) # variable
datetime.MAXYEAR.numerator
datetime.MINYEAR.numerator
datetime.MAXYEAR.denominator
datetime.MINYEAR.denominator
help(datetime.date) # class
datetime.date.weekday(datetime.date.today()) #function, 0 as monday and so on
datetime.__name__ # reference object 

# Sect 1: Basics of Python
# # # 1.1 Input and Output

x = input()
print("Hello", x)

# # 1.2 Variables and Types

# Assign values to the following variable as described above
# Don't change the variable name
my_string1 = "InterviewBit"
my_string2 = "Don't change the variable name"
my_int = 11
my_float = 20.5
# Don't change the below code
print("String1: %s" % my_string1)
print("String2: %s" % my_string2)

print("Integer: %d" % my_int)
print("Integer: %f" % my_int)
print("Integer: %s" % my_int)

print("Float: %f" % my_float)
print("Float: %s" % my_float)
print("Float: %d" % my_float)

# 1.3 Arithmetic operators on Numbers
A = int(input())
B = int(input())
# Print seven lines as described above
print(A+B)
print(A-B)
print(A*B)
# print(int((A-A%B)/B))    
print(A//B)
print(A/B)
print(A%B)
print(A**B)
6/2
7//2

# 1.4 Arithmetic operators on Strings
print("InterviewBit"*100)

# Sect 2: Flow Control & Functions
       
# # 2.1 Conditions and If-Else

# Given an integer num denoting percentage of a student, calculate the grade according to the below rules:
# If num >= 90, grade A.
# If num >= 80, grade B.
# If num >= 70, grade C.
# If num >= 60, grade D.
# If num >= 50, grade E.
# Else grade will be F.
# Print a string consisting of single character denoting the grade.
num = int(input())
# YOUR CODE GOES HERE
if (num >= 90):
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
elif num >= 50:
    print("E")
else:
    print("F")
    
# # 2.2 Loops and Jump statements

# Now, let’s dive into Jump statemets.
# break
# continue
# break is used to exit a for loop or a while loop, whereas continue is used to 
# skip the current block, and return to the “for” or “while” statement. A few examples
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
        
count = 0
for x in range(10):
    print(count)
    count += 1
    if count >= 5:
        break
    
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
    
# Try the following example in the editor below.
# You are given an integer N, print all the odd values, for all i, where 0 <= i < N. 
# Print each values on a seperate line.
N = int(input())
# YOUR CODE GOES HERE
for i in range(1, N):
    if i%2 == 1:
        print(i)
    else:
       continue 

# # 2.3 Functions
# example: 
#     def my_function(name):
#         print("Hello %s" %name)
def my_function(name):
    print("Hello %s" %name)
my_function('AbC')


# # Sect 3: Strings

# 3.1 String Formatting
# Note : F-strings are faster than the two most commonly used string formatting mechanisms, 
# which are % formatting and str.format().
# 3.1a print
# Python uses C-style string formatting to create new, formatted strings. 
# The ”%” operator is used to format a set of variables enclosed in a “tuple” (a fixed size list), 
my_string = "InterviewBit"
greet = "how are you"

print("Hello %s" %my_string)
print("Hello %s, %s" %(my_string, greet))
qty = 10
item_name = "chocolate"
rs = 100
print("You can buy %d %s in %d rupees" % (qty, item_name, rs))
# together with a format string, which contains normal text together with “argument specifiers”, 
# special symbols like "%s" and "%d".
# Any object which is not a string CAN ALSO be formatted using the %s operator as well. 
# The string which returns from the “repr” method of that object is formatted as the string. For example:
my_list = [1, 2, 3]
print("Given list: %s" %my_list)
print("Given list: %s, %s" %(my_list, greet))

# Here are some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
# The placeholders can be identified using 
# named indexes {price}, 
print("You can buy {quantity} {item} in {amt} rupees".format(quantity = qty, item = item_name, amt = rs))
# numbered indexes {0}, or 
print("You can buy {0} {1} in {2} rupees".format(qty, item_name, rs))
# even empty placeholders {}.
print("You can buy {} {} in {} rupees".format(qty, item_name, rs))
"You can buy {} {} in {} rupees".format(qty, item_name, rs)
"Given list: %s, %s" %(my_list, greet)

# 3.1b f-string
# PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation 
# or more commonly as F-strings (because of the leading f character preceding the string literal).
# The idea behind f-strings is to make string interpolation simpler.

# F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.") 
# prints Hello, My name is Tushar and I'm 23 years old.
# Try the following example in the editor below.
# You will need to write a format string which prints out the data using the following syntax: 
    # Hello Robin. You are currently left with 10 chocolates.
data = ("Robin", 10, "chocolates")
a,b,c = data
format_string = "Hello %s. You are currently left with %d %s."
print(format_string %data)
print(f"Hello {a}. You are currently left with {b} {c}")
f"Hello {a}. You are currently left with {b} {c}"

# 3.2 String Operations
S = input()

#Print length of the string S
print(len(S))
#Print the first occurence of the letter 'a' in S
print(S.find("a"))
#Note it is guaranteed that letter a is present in the string S
#print(S.index("a"))
#Print all the characters with even index in S
result = []
for i in range(len(S)):
    if i % 2 == 0:
        result += S[i]
result
print("".join(result))
print("__".join(result))   
# 3.3 String Validators
# 3.3a: str.isalnum() # alphanumeric (a-z, A-Z and 0-9).# 
print('ab123'.isalnum())
#prints True
print('ab123#'.isalnum())
#prints False

# 3.3b: str.isalpha()   alphabetical (a-z and A-Z).
print('abcD'.isalpha())
#prints True
print('abcd1'.isalpha())
#prints False

# 3.3c: str.isdigit()  
# 3.3d: str.islower()  
# 3.3e: str.isupper()  

# Try the following example in the editor below.
# You are given a string S. Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Output Format
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

S = input()

    # In the first line, print True if S has any alphanumeric characters. Otherwise, print False.

isTrue_1 = False
n_S, i_S = (len(S), 0)
cur_i_S = None
while isTrue_1 == False:
    if i_S == n_S:
        break
    cur_i_S = S[i_S]
    i_S += 1
    if (cur_i_S.isalnum()):
        isTrue_1 = True
    if isTrue_1 == True:
        break
print(isTrue_1)

    # In the second line, print True if S has any alphabetical characters. Otherwise, print False.

isTrue_2, i_S = (False, 0)
while isTrue_2 == False:
    if i_S == n_S:
        break
    cur_i_S = S[i_S]
    i_S += 1
    if (cur_i_S.isalpha()):
        isTrue_2 = True
    if isTrue_2 == True:
        break
print(isTrue_2)

    # In the third line, print True if S has any digits. Otherwise, print False.

isTrue_2, i_S = (False, 0)
# print(i_S)
while isTrue_2 == False:
    #print(i_S)
    if i_S == n_S:
        break
    cur_i_S = S[i_S]
    #print(cur_i_S)
    i_S += 1
    if (cur_i_S.isdigit()):
        isTrue_2 = True
    if isTrue_2 == True:
        break
print(isTrue_2)

    # In the fourth line, print True if S has any lowercase characters. Otherwise, print False.

isTrue_2, i_S = (False, 0)
while isTrue_2 == False:
    if i_S == n_S:
        break
    cur_i_S = S[i_S]
    # print(cur_i_S, cur_i_S.islower())
    i_S += 1
    if (cur_i_S.islower()):
        isTrue_2 = True
    if isTrue_2 == True:
        break
print(isTrue_2)

    # In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

isTrue_2, i_S = (False, 0)    
while isTrue_2 == False:
    #print('i_S is ', i_S)
    if i_S == n_S:
        #print('yep!')
        break
    cur_i_S = S[i_S]
    i_S += 1
    # print(cur_i_S)
    if (cur_i_S.isupper()):
        #print("heppty")
        isTrue_2 = True
    if isTrue_2 == True:
        break
#pitn("Asd")
print(isTrue_2)

# Sect 4: Containers & Classes

# # 4.1: Lists  

# Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish.

# List is a collection which is ordered and changeable. Allows duplicate members.

# Lists can also be iterated over in a very simple manner. Below is an example to build a list.

# my_list = []
# # append insert the element at the end of the list
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print(my_list[0]) # prints 1
# print(my_list[1]) # prints 2
# print(my_list[2]) # prints 3
# Accessing an index which does not exist generates an exception (an error).

# my_list = [1,2,3]
# print(my_list[5]) # Gives an error
# Negative Indexing

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

# my_list = [1, 2, 3]
# print(my_list[-1]) #prints 3
# print(my_list[-2]) #prints 2
# Try the following example in the editor below:

# You are given an empty list named names, you have to insert “Robin”, “Aman”, “Rahul” at the end of list one after other.

def main():
    names = []
    # YOUR CODE GOES HERE
    names_tb_added = ('Robin', 'Aman', 'Rahul')
    for i in names_tb_added:
        names.append(i)
    
    print(names)
    return 0

if __name__ == '__main__':
    main()

# # 4.2: Tuples
# Python Collections

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Set is a collection which is unordered and unindexed. No duplicate members.

# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# We will discuss all four collection one by one, we had discussed List in one of the previous article.

# Tuple

# Tuple is similar to a list but once the tuple is created we can’t change the elements directly.

# Creating a Tuple

my_tuple = ('one', 'two', 'three')
print(my_tuple)
print ('one', 'two', 'three')
# You can access tuple items by referring to the index number, inside square brackets:

my_tuple = ('one', 'two', 'three')
print(my_tuple[1])
# print two
# Is there any way to change Tuple Values?

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#  But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# Self Note: but then it is a new tuple instance

my_tuple = ('one', 'two', 'three')
my_list = list(my_tuple)
my_list[2] = 'two'
my_tuple = tuple(my_list)
print(my_tuple)
# print ('one', 'two', 'two')
# Create Tuple with One item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

my_tuple = ("one",)
print(type(my_tuple))

# NOT a tuple
my_tuple = ("one")
print(type(my_tuple))
# Join Two Tuples

# To join two or more tuples you can use the + operator:

my_tuple1 = ('one', 'two', 'three')
my_tuple2 = ('1', '2', '3')
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3)
# Try the following example in the editor below.

# Given two tuples called tuple1 and tuple2, perform the operations described in comments in the editor.
def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    
    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    to_be_added = ("number", )
    tuple1 = to_be_added + tuple1[1:]
    tuple2 = to_be_added + tuple2[1:]
    print(tuple1)
    print(tuple2)
    
    return 0

if __name__ == '__main__':
    main()  

# # 4.3: dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
print(my_dict)
# Dictionary with the use of Mixed Keys.
my_dict = {'One' : 'Robin', 2 : 'Rahul'}
print(my_dict)
# Accessing Items

# You can access the items of a dictionary by referring to its key name, inside square brackets.

# There is also a method called get() that will give you the same result.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
val = my_dict[2]
print(val) # print 'Rahul'

# using get()
val = my_dict.get(2)
print(val) # print 'Rahul'
# Change Values

# You can change the value of a specific item by referring to its key name.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
my_dict[2] = 'Rohan'
val = my_dict[2]
print(val) # print 'Rohan'
# Loop through a Dictionary

# You can loop through a dictionary by using a for loop.
 # When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
for x in my_dict:
    print(x)    # print 1 2 3

# values() method to return values of a dictionary
for x in my_dict.values():
    print(x)    # print 'Robin' 'Rahul' 'Aman'

# Loop through both keys and values, by using the items() method
for key, val in my_dict.items():
    print(key, val)
# Adding Items

# Adding an item to the dictionary is done by using a new index key and assigning a value to it.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
my_dict[4] = 'Shivam'  # Added item key is 4 and value is 'Shivam'
print(my_dict)
# Removing Items

# There are several methods to remove items from a dictionary.

# The pop() method removes the item with the specified key name.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
temp = my_dict.pop(2) # Removes item with key 2 and value 'Rahul'
print(my_dict)
# The del keyword removes the item with the specified key name.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
del my_dict[2] # Removes item with key 2 and value 'Rahul'
print(my_dict)
# Dict() constructor

# It is also possible to use the dict() constructor to make a new dictionary.

my_dict = dict(1 = 'Robin', 2 = 'Rahul', 3 = 'Aman') # Note that this may not work
# note the use of equals rather than colon for the assignment
print(my_dict)
# Try the following exercise in the editor below.

# Given a dictionary called ‘my_dict’, perform the operations described in the comments:

# update value for key "Sunday" to 7
# adding another item with key "Default" having value 0

def main():
    my_dict = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 0
    }

    # update value for key "Sunday" to 7
    my_dict["Sunday"] = 7
        
    # adding another item with key "Default" having value 0
    my_dict["Default"] = 0
    
    for i in sorted(my_dict):
        print ("(\'" + i + "\',", str(my_dict[i]) + ")")

    return 0

if __name__ == '__main__':
    main()
    
# # 4.4: Set

# A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets. 
 # A set cannot contain duplicates.

my_set = {'one', 'two', 'three'}
print(my_set)

# using set()

my_set = set(['one', 'two', 'three'])
print(my_set)
# Sets are unordered, so you cannot be sure in which order the items will appear.

# Access Items

# You cannot access items in a set by referring to an index or a key.
 # But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

my_set = {'one', 'two', 'three'}
for val in my_set:
    print(val)
# NOTE: Once set is created, you cannot change its items, but you can add new items.
 # Below is an example:
my_set = {'one', 'two', 'three'}
id(my_set)
my_set.add('four')
id(my_set) # same instance
# update is used to update set with another sequence
my_set.update(['four', 'five', 'six'])
id_temp = id(my_set)
print(my_set)
# my_set will contain {'one', 'two', 'three', 'four', 'five', 'six'}
# Since there will be no duplicates. 
# Remove Item

# You can remove an item in a set, use the remove(), or the discard() method.

# NOTE: If the item to remove does not exist, remove() will raise an error, but discard() will NOT raise any error.

my_set = {'one', 'two', 'three', 'four'}
id_temp = id(my_set) 
my_set.remove('one') # removes 'one' from my_set
my_set
id_temp == id(my_set)
my_set.discard('three') # removes 'three' from my_set
id_temp == id(my_set)
# my_set.remove('five') # throws an error
my_set.discard('five') # Will not throw an error
id_temp == id(my_set)

# Try the following example in the editor given below.

# Given a set called ‘my_set’, perform the operations described in the comments.

def main():
    my_set = set([1, 3, 2, 4, 1, 3, 3, 0])
    
    # add 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 to my_set
    to_be_added = [i for i in range(10, 24)]
    to_be_added.pop(1)
    my_set.update(to_be_added)
    # delete 2 and 3 from my_set
    my_set.discard(2)
    my_set.discard(3)
    
    li = list(my_set)
    li.sort()

    print(li)
    return 0

if __name__ == '__main__':
    main()
    
    
# 4.5 Set operations

s = set("Scaler")
print(s.union("Academy"))

print(s.intersection("Academy"))
print(s.difference("Academy"))

# Try the following excercise in the editor below.
# You are given three sets X, Y, Z where X contains the children id who loves to play Football, 
# Y contains the children id who loves to play Cricket, 
# and Z contains the children id who loves to play BasketBall. You need to perform operations on these sets as decribed in comments.

# Note: You are only required to add your code, no need to change any of the given statements.

'''
def printset(setx):
    li = list(setx)
    li.sort()
    print(li)
'''

def main():
    # Below are the three sets 
    
    X = set([1, 3, 7, 5, 6, 10, 20, 21, 22, 23, 55, 51, 2, 19, 9, 17, 27, 26, 25, 35])
    Y = set([2, 10, 13, 18, 17, 22, 28, 27, 5, 49, 46, 43, 3])
    Z = set([21, 1, 32, 25, 12, 11, 8, 10, 26, 16, 31, 20, 30, 14])
    
    # 'set1' contains the student who loves to play all three sports
    set1 = X.intersection(Y).intersection(Z)
        
    printset(set1)
    
    # 'set2' contains the student who loves to play both Football and Cricket, but don't play Basketball
    set2 = X.intersection(Y).difference(Z)
    
    printset(set2)
    
    # 'set3' contains the student who loves to play Cricket, but don't loves any other sport
    set3 = Y.difference(X).difference(Z)
    
    printset(set3)
    return 0

if __name__ == '__main__':
    main()
    
    # 4.6 Nested List
# A list can contain any sort object, even another list (sublist), which in turn can contain sublists themselves, and so on. 
# This is known as nested list.

# You can use them to arrange data into hierarchical structures.

# Creating a Nested List

my_list = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
for i in my_list:
    print(i)
# Access Nested List

# You can access individual items in a nested list using multiple indexes.
print(my_list[2])  
print(my_list[2][2])  
print(my_list[2][2][0])  

# Add items

# To add new values to the end of the nested list, use append() method.

# When you want to insert an item at a specific position in a nested list, use insert() method.

# You can merge one list into another by using extend() method.

my_list = ['a', ['bb', 'cc'], 'd']
my_list[1].append('xx')
print(my_list)
# Prints ['a', ['bb', 'cc', 'xx'], 'd']

my_list = ['a', ['bb', 'cc'], 'd']
my_list[1].insert(0,'xx')
print(my_list)
# Prints ['a', ['xx', 'bb', 'cc'], 'd']

my_list = ['a', ['bb', 'cc'], 'd']
my_list[1].extend([1,2,3])
print(my_list)
# Prints ['a', ['bb', 'cc', 1, 2, 3], 'd']
# Remove items

# If you know the index of the item you want, you can use pop() method. It modifies the list and returns the removed item.

# If you’re not sure where the item is in the list, use remove() method to delete it by value.

my_list = ['a', ['bb', 'cc', 'dd'], 'e']
x = my_list[1].pop(1)
print(my_list)
my_list.remove('fff')
my_list[1].remove('bb')
my_list
# Prints ['a', ['bb', 'dd'], 'e']

# removed item
print(x)
# Prints cc

my_list = ['a', ['bb', 'cc', 'dd'], 'e']
my_list[1].remove('cc')
print(my_list)
# Prints ['a', ['bb', 'dd'], 'e']
# Try the following example in the editor below.

# You are given a nested list named ‘my_list’, perform the operations as defined in the comments.

# NOTE: You don’t need to change/remove any code. Only add the line of code, wherever needed.

def main():
    my_list = [['a', 'b'], ['cc', 'dd', ['eee', 'fff']], ['g', 'h']]
    
    # insert a new list [1, 2, 3] at the end of my_list
    # Your code goes here
    to_be_added = [1,2,3]
    my_list.append(to_be_added)
    print(my_list)
    
    # Delete 'eee' from the list
    # Your code goes here
    my_list[1][2].remove('eee')
    print(my_list)
    return 0
    
if __name__ == '__main__':
    main()

    # 4.7 List Comprehensions
# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.

# Suppose, we want to separate the letters of the word InterviewBit and add the letters as items of a list.

# The first thing that comes in mind would be using for loop.

S = 'Interviewbit'
letter_S = []
for l in S:
    letter_S.append(l)
print(letter_S)
# However, Python has an easier way to solve this issue using List Comprehension. List comprehension is an elegant way to define and create lists based on existing lists.

S = 'InterviewBit'
letter_S = [l for l in S]
print(letter_S)
# Conditions in Comprehension

# Using if

# Create a list of odd numbers in the range of 1 to 10

my_list = [x for x in range(1, 10) if x%2 == 1]
print(my_list)
# Try the following example in the editor below.

# You are given a list of strings, using list comprehensions create a new list of strings called ‘my_list’, which only contain the strings that have odd length.


def main():
    str_list = ['given', 'intern', 'InterviewBit', 'network', 'local', 'multiple', 'define', 'nodes', 'algorithm', 'allows', 'community', 'phase', 'single']
    my_list = [x for x in str_list if len(x) % 2 == 1]
    
    print(my_list)
    return 0

if __name__ == '__main__':
    main()

    # 4.8 Classes and Objects
# Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.

# Objects are an encapsulation of variables and functions into a single entity.

# Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

# To create a class, use the keyword class

class my_class:
    my_var = "InterviewBit"
    def my_function(self):
        print("Welcome to " + self.my_var)
        
# Create an object of the above class

my_obj = my_class()
my_obj.my_function()
# prints Welcome to InterviewBit
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The init() Function

# To understand the meaning of classes we have to understand the built-in __init__() function.

# __init__() is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
obj = Student("Robin", "CSE")
print(obj.name)
print(obj.branch)
# Try the following example in the editor below

# We have a class defined for Student. Create two new object for students called stud1 and stud2. 
# Set stud1 name as ‘Robin’ and branch ‘CSE’ and stud2 name as ‘Rahul’ and branch as ‘ECE’.

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
    def printfunction(self):
        print(self.name + " " + self.branch)

def main():
    #Your code goes here
    stud1 = Student("Robin", "CSE")
    stud2 = Student("Rahul", "ECE")
    stud1.printfunction()
    stud2.printfunction()
    return 0

if __name__ == '__main__':
    main()
    

    # 4.9 Numpy arrays

# Numpy arrays are great alternatives to Python Lists. 
# Some of the key advantages of Numpy arrays are that they are fast, easy to work with, 
# and give users the opportunity to perform calculations across entire arrays.

# The array object in NumPy is called ndarray. We can create a NumPy ndarray object by using the array() function.

import numpy as np
my_arr = np.array([1, 2, 3, 4, 5])

print(my_arr)

type(my_arr)
#  It shows that my_arr is numpy.ndarray type.
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array(42)
a
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
c
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
d
print(a.ndim) # prints 0 # constant
print(b.ndim) # prints 1 
print(c.ndim) # prints 2 # matrix
print(d.ndim) # prints 3 # 3d
# Access Array Elements

# 1-D Array

# Array indexing is the same as accessing an array element.

my_arr = np.array([1, 2, 3, 4])

print(my_arr[0]) # prints 1
# 2-D Array

# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

# Access the 5th element on 2nd dimension:

my_arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd dimension: ', my_arr[1, 4]) # prints 10
# Negative Indexing

# Use negative indexing to access an array from the end.

my_arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', my_arr[1, -1]) # prints 10
# Searching array

# You can search an array for a certain value, and return the indexes that get a match.
 # To search an array, use the where() method.

my_arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(my_arr == 4)
list(my_arr == 4)

print(x) # Finds all the indexes of 4

# Try the following example in the editor below.

# You are given a list of integers called ‘arr’, convert this into ndarray and use where to find all the occurences of 2 in the array and assign that to x.

# import numpy as np
def main():
    arr = [1, 3, 2, 2, 5, 3, 8, 2]
    
    # Convert the above array into ndarray
    arr = np.array(arr)
    
    print(type(arr))
    
    # Use where to find all the indexes of 2
    x = np.where(arr == 2)
    
    print(x)
    return 0

if __name__ == '__main__':
    main()