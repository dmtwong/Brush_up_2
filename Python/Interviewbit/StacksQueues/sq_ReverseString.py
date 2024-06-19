# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:38:28 2024

@author: USER
"""

# Given a string S, reverse the string using stack.

# Example :

# Input : "abc"
# Return "cba"
# PROBLEM APPROACH :

# Complete solution in hints.

# class Solution:
	# @param A : string
	# @return a strings
# 	def reverseString(self, A):

def reverseString(A):
    from collections import deque
    deque_A = deque(A)
    result = ''
    # n_A = len(A)
    for i in deque_A:
        # print(i)
        result = i + result
    return result
reverseString('abc')
    