# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:18:29 2024

@author: USER
"""

# Problem Description 

# Given a column title A as appears in an Excel sheet, return its corresponding column number.

# Problem Constraints
# 1 <= |A| <= 100

# Input Format
# First and only argument is string A.

# Output Format
# Return an integer

# Example Input
# Input 1:
#  "A"
# Input 2:
#  "AB"

# Example Output
# Output 1:
#  1
# Output 2:
#  28

# Example Explanation
# Explanation 1:
#  A -> 1
# Explanation 2:
# A  -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 


# class Solution:
# 	# @param A : string
# 	# @return an integer
# 	def titleToNumber(self, A):
import string
# alp_val = 1
# alp_num_dict = {}
# for i in string.ascii_uppercase:
#     alp_num_dict[i] = alp_val
#     alp_val += 1

def titleToNumber(A):
    chars = string.ascii_uppercase
    alp_val = 1
    alp_num_dict = {}
    for i in chars:
        alp_num_dict[i] = alp_val
        alp_val += 1        
    n_A = len(A)
    pw = n_A - 1
    result = 0
    for i in range(n_A):
        result += 26**pw * alp_num_dict[A[i]]
        pw -= 1
    return result
    
# Testing cases:

    titleToNumber('A')
titleToNumber('AB')
titleToNumber('ABC')


##############################
# Editoral:
    # Python
# class Solution:
# 	# @param A : string
# 	# @return an integer
# 	def titleToNumber(self, A):
# 	    T = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
# 	    return sum(T[ch] * 26**i for i, ch in enumerate(A[::-1]))

    # Scala
    
#     class Solution {
#     def titleToNumber(A: String): Int  = {
#         var sum = 0
#         for (ch <- A) sum = sum * 26 + (ch - 'A' + 1)
#         sum
#     }
# }
    
    # c++
    
#     int Solution::titleToNumber(string A) {
# int res=0;
# for (const auto& c:A) {res =res*26+c +1 - 'A';}return res;
# }
    