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